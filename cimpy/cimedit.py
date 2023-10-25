import importlib
import uuid
import datetime
import cimpy.cgmes_v2_4_15

def node_breaker_to_bus_branch(import_result):
    """TODO: Add documentation
    """
    res = import_result['topology']
    breaker_list = []
    terminals_list = []
    operational_limit_set_list = []
    voltage_limit_list = []
    diagram_objects_list = []
    diagram_object_points_list = []
    connect_nodes = []
    for mRID in res.keys():
        class_name = res[mRID].__class__.__name__
        if class_name == "Breaker":
            breaker_list.append(mRID)
        elif class_name == "OperationalLimitSet":
            operational_limit_set_list.append(mRID)
        elif class_name == "Terminal":
            terminals_list.append(mRID)
        elif class_name == "VoltageLimit":
            voltage_limit_list.append(mRID)
        elif class_name == "DiagramObject":
            diagram_objects_list.append(mRID)
        elif class_name == "DiagramObjectPoint":
            diagram_object_points_list.append(mRID)
        elif class_name == 'ConnectivityNode':
            connect_nodes.append(mRID)

    # search for open breakers
    open_breakers = []
    for breaker in breaker_list:
        if res[breaker].open:
            if not res[breaker].retained:
                open_breakers.append(breaker)

    # check terminals for reference to open breakers and delete references to Connectivity Nodes
    del_terminals_list = []
    for terminal in terminals_list:
        cond_eq = res[terminal].ConductingEquipment
        if cond_eq.mRID in open_breakers:
            del_terminals_list.append(terminal)
        else:
            res[terminal].ConnectivityNode = None

    # check for OperationalLimitSet with references to deleted Terminals
    del_operationallimitset = []
    for operational_limit in operational_limit_set_list:
        if res[operational_limit].Terminal.mRID in del_terminals_list:
            del_operationallimitset.append(operational_limit)

    del_voltage_limit = []
    for voltage in voltage_limit_list:
        if res[voltage].OperationalLimitSet.mRID in del_operationallimitset:
            del_voltage_limit.append(voltage)

    del_diagram_object = []

    for diagram_object in diagram_objects_list:
        keep_diagram = []
        if res[diagram_object].IdentifiedObject is None:
            continue
        if 'ConnectivityNode' in str(type(res[diagram_object].IdentifiedObject)):
            if res[diagram_object].IdentifiedObject.TopologicalNode is not None:
                keep_diagram.append(res[diagram_object].IdentifiedObject.TopologicalNode)
        elif res[diagram_object].IdentifiedObject.mRID in (open_breakers + del_terminals_list):
            del_diagram_object.append(diagram_object)

    del_diagram_object_points = []
    for diagram_point in diagram_object_points_list:
        if res[diagram_point].DiagramObject is None:
            continue
        if res[diagram_point].DiagramObject.mRID in del_diagram_object:
            del_diagram_object_points.append(diagram_point)

    del_list = open_breakers + del_diagram_object_points + del_diagram_object + del_voltage_limit + \
               del_operationallimitset + del_terminals_list + connect_nodes

    for key in del_list:
        del res[key]

    import_result['topology'] = res

    return import_result


def add_external_network_injection(import_result, version, mRID, voltage_set_point):
    """TODO: Add documentation
    """
    res = import_result['topology']
    TopologicalNode = ''
    if mRID in res:
        if 'TopologicalNode' in str(type(res[mRID])):
            TopologicalNode = res[mRID]
        elif 'ConnectivityNode' in str(type(res[mRID])):
            TopologicalNode = res[mRID].TopologicalNode.mRID

    if TopologicalNode != '':
        i = 1
        while 'Injection ' + str(i) in res.keys():
            i += 1
        inj_name = 'Injection ' + str(i)
        reg_name = 'Regulating Control ' + str(i)
        terminal_name = 'Terminal Injection ' + str(i)

        #module_name = "cimpy." + version + ".Equipment."
        module_name = "cimpy." + version + "."
        
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal_name] = terminal_class(mRID=terminal_name,
                                            name=terminal_name,
                                            TopologicalNode=TopologicalNode)

        regulating_control_module = importlib.import_module(module_name + 'RegulatingControl')
        regulating_control_class = getattr(regulating_control_module, 'RegulatingControl')
        res[reg_name] = regulating_control_class(mRID=reg_name,
                                                 name=reg_name,
                                                 targetValue=voltage_set_point,
                                                 Terminal=res[terminal_name])

        network_injection_module = importlib.import_module(module_name + 'ExternalNetworkInjection')
        network_injection_class = getattr(network_injection_module, 'ExternalNetworkInjection')
        res[inj_name] = network_injection_class(mRID=inj_name,
                                                name=inj_name,
                                                RegulatingControl=res[reg_name],
                                                Terminals=[res[terminal_name]])

        res[reg_name].RegulatingCondEq = res[inj_name]
        res[terminal_name].ConductingEquipment = res[inj_name]
        res[terminal_name].RegulatingControl = res[reg_name]

        # Append the Terminal List of the TopologicalNode
        res[mRID].Terminal.append(res[terminal_name])
    else:
        print('No Terminal with mRID ', mRID, ' found in object list!')

    import_result['topology'] = res

    return import_result


def add_ACLineSegment(cim_topology, version, name, mRID="", mRID_node1="", node1_name="", mRID_node2="", node2_name="", r=0, x=0, bch=0, gch=0, baseVoltage=0):
    """
    Function to add ACLineSegment objects to existing cim topology

    ...

    Parameters
    ----------
    cim_topology : dict
        existing cim topology
    version : str
        cgmes version. Actually only version 2.4.15 is supported
    name : str
        name of the ACLineSegment to be added
    mRID : str
        uuid for the synchronous machine. If mRID=="", it will be automatically generate
    mRID_node1 : str
        uuid of the first node to which this ACLineSegment has to be connected
    mRID_node2 : str
        uuid of the second node to which this ACLineSegment machine has to be connecteds
    r : float
        Positive sequence series resistance of the entire line section. Unit: Ohm
    x : float
        Positive sequence series reactance of the entire line section. Unit: Ohm
    bch : float
        Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. This value represents the full charging over the full length of the line. Unit: S
    gch : float
        Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section. Unit: S
    baseVoltage: float
        Nominal Voltage of this line
        
    Returns
    ------- 
    import_result
    dict containing the modified cim topology
    """
    
    res = cim_topology['topology']
    
    if name in res:
        print('WARN: ACLineSegment mRID={} is already included in the cim topology, object will be not be addd to cim topology"', mRID)
        return cim_topology

    # Creating random mRID using uuid4()
    if mRID == "":
        mRID = str(uuid.uuid4())
        
    if (mRID_node1==""):
        for uuid_, obj in res.items():
            if hasattr(obj, "name"):
                if (obj.name==node1_name):
                    mRID_node1=uuid_
    if (mRID_node2==""):
        for uuid_, obj in res.items():
            if hasattr(obj, "name"):
                if (obj.name==node2_name):
                    mRID_node2=uuid_
    
    # look for topological nodels connected to line            
    TopologicalNode1 = None
    TopologicalNode2 = None
    if mRID_node1 in res:
        if 'TopologicalNode' in str(type(res[mRID_node1])):
            TopologicalNode1 = res[mRID_node1]
        elif 'ConnectivityNode' in str(type(res[mRID_node1])):
            TopologicalNode1 = res[mRID_node1].TopologicalNode

    if mRID_node2 in res:
        if 'TopologicalNode' in str(type(res[mRID_node2])):
            TopologicalNode2 = res[mRID_node2]
        elif 'ConnectivityNode' in str(type(res[mRID_node2])):
            TopologicalNode2 = res[mRID_node2].TopologicalNode
    
    if (TopologicalNode1 is not None) and (TopologicalNode2 is not None):
        
        module_name = "cimpy." + version + "."

        # create terminals for this line
        terminal1_mRID = str(uuid.uuid4())
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal1_mRID] = terminal_class(mRID=terminal1_mRID,
                                            name='Terminal_1_' + name,
                                            sequenceNumber=1,
                                            TopologicalNode=TopologicalNode1)
        terminal2_mRID = str(uuid.uuid4())
        res[terminal2_mRID] = terminal_class(mRID=terminal2_mRID,
                                            name='Terminal_2_' + name,
                                            sequenceNumber=2,
                                            TopologicalNode=TopologicalNode2)

        # create object of  type ACLineSegment
        ACLineSegment_module = importlib.import_module((module_name + 'ACLineSegment'))
        ACLineSegment_class = getattr(ACLineSegment_module, 'ACLineSegment')
        res[mRID] = ACLineSegment_class(mRID= mRID,
                                        name= name,
                                        r = r,
                                        x = x,
                                        bch = bch,
                                        gch = gch,
                                        BaseVoltage = create_BaseVoltage(res, baseVoltage),
                                        Terminals = [res[terminal1_mRID], res[terminal2_mRID]])
        # Connect Equipment to Terminal
        res[terminal1_mRID].ConductingEquipment = res[mRID]
        res[terminal2_mRID].ConductingEquipment = res[mRID]

        # Append the Terminal List of the TopologicalNodes
        res[mRID_node1].Terminal.append(res[terminal1_mRID])
        res[mRID_node2].Terminal.append(res[terminal2_mRID])

        cim_topology['topology'] = res
        return cim_topology

    elif TopologicalNode1 is None:
        print('WARN: No Topological with mRID={} found in cim topology, ACLineSegment name={} will be not added to cim topology!'.format(mRID_node1, name))
        
    if TopologicalNode2 is None:
        print('WARN: No Topological with mRID={} found in cim topology, ACLineSegment name={} will be not added to cim topology!'.format(mRID_node2, name))

    cim_topology['topology'] = res

    return cim_topology


def add_Terminal(cim_topology, version, TopologicalNode, ConductingEquipment, pInjection = 0, qInjection = 0, mRID = ''):
    res = cim_topology['topology']
    
    if mRID == "":
        mRID = str(uuid.uuid4())

    #module_name = "cimpy." + version + ".Equipment."
    module_name = "cimpy." + version + "."

    terminal_module = importlib.import_module((module_name + 'Terminal'))
    terminal_class = getattr(terminal_module, 'Terminal')
    res[mRID] = terminal_class(mRID='Terminal',
                                name='Terminal',
                                TopologicalNode=TopologicalNode,
                                ConductingEquipment= ConductingEquipment,
                                pInjection= pInjection,
                                qInjection= qInjection)

    cim_topology['topology'] = res

    return cim_topology
        
def add_TopologicalNode(cim_topology, version, name, mRID="", baseVoltage=0, v=0.0, angle=0.0):		
  
    res = cim_topology['topology']
    
    if mRID in res:
        print("mRID", mRID, "is already included")
        return cim_topology

    # Creating random mRID using uuid4()
    if mRID == "":
        mRID = str(uuid.uuid4())

    # get module name
    module_name = "cimpy." + version + "."
    TopologicalNode_module = importlib.import_module((module_name + 'TopologicalNode'))
    
    # create topological node object
    TopologicalNode_class = getattr(TopologicalNode_module, 'TopologicalNode')
    res[mRID] = TopologicalNode_class(mRID= mRID,
                                name= name,
                                BaseVoltage=baseVoltage,
                                Terminal = [])
    
    # create SV object
    if isinstance(v, float) and isinstance(angle, float):
        SvVoltage_name = name + "-sv"
        SvVoltage_module = importlib.import_module((module_name + 'SvVoltage'))
        SvVoltage_class = getattr(SvVoltage_module, 'SvVoltage')
        res[SvVoltage_name] = SvVoltage_class(v=v,
                                            angle=angle,
                                            TopologicalNode=res[mRID])
        res[mRID].SvVoltage = res[SvVoltage_name]
    
    cim_topology['topology'] = res
    return cim_topology

    
def add_SynchronousMachine(cim_topology, version, name, mRID_node="", node_name="", mRID="", ratedS=0, ratedU=0, p=0, q=0, targetValue=0, initialP=0):          
    """
    #TODO: baseVoltage?
    Function to add synchronous machine to existing cim topology

    ...

    Parameters
    ----------
    cim_topology : dict
        existing cim topology
    version : str
        cgmes version. Actually only version 2.4.15 is supported
    name : str
        name of the synchronous machine to be added
    mRID_node : str
        uuid of the node to which this synchronous machine has to be connected
    mRID : str
        uuid for the synchronous machine. If mRID=="", it will be automatically generated
    ratedS : float
        apparent power rating for the unit. The attribute shall have a positive value. Unit: MVA
    ratedU : float
        Rated voltage. It is primarily used for short circuit data exchange according to IEC 60909. Unit: kV
    p : float
        Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Unit: MW
    q : float
        Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Unit: MVAr
    targetValue : float
        uuid for the synchronous machine. If mRID=="", it will be automatically generated. Unit: kV
    initialP : float
        Default initial active power which is used to store a powerflow result for the initial active power for this unit in this network configuration. Unit: MW

        
    Returns
    ------- 
    import_result
    dict containing the modified cim topology
    """
        
    # TODO: RotatingMachine without paramameters?
    
    res = cim_topology['topology']

    if mRID in res:
        print('WARN: Synchronous Machine mRID="{}" is already included in the cim topology, object will be not be addd to cim topology"', mRID)
        return cim_topology
    
    # Creating random mRID using uuid4()
    if mRID == "":
        mRID = str(uuid.uuid4())
                
    if (mRID_node==""):
        for uuid_, obj in res.items():
            if isinstance(obj, cimpy.cgmes_v2_4_15.TopologicalNode):
                if (obj.name==node_name):
                    mRID_node=uuid_
                  
    TopologicalNode = None
    if 'TopologicalNode' in str(type(res[mRID_node])):
        TopologicalNode = res[mRID_node]
    elif 'ConnectivityNode' in str(type(res[mRID_node])):
        TopologicalNode = res[mRID_node].TopologicalNode.mRID

    if TopologicalNode is not None:
        
        module_name = "cimpy." + version + "."
        
        # add terminal for this SM
        terminal_mRID = str(uuid.uuid4())
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal_mRID] = terminal_class(mRID=terminal_mRID,
                                            name='Terminal_' + name,
                                            TopologicalNode=TopologicalNode)
        
        # add terminal for this SM
        generating_unit_mRID = str(uuid.uuid4())
        GeneratingUnit_module = importlib.import_module((module_name + 'GeneratingUnit'))
        GeneratingUnit_class = getattr(GeneratingUnit_module, 'GeneratingUnit')
        res[generating_unit_mRID] = GeneratingUnit_class(mRID=generating_unit_mRID,
                                                        name='GeneratingUnit_' + name,
                                                        initialP=initialP)
        
        # add terminal for this SM
        regulating_control_mRID = str(uuid.uuid4())
        RegulatingControl_module = importlib.import_module((module_name + 'RegulatingControl'))
        RegulatingControl_class = getattr(RegulatingControl_module, 'RegulatingControl')
        res[regulating_control_mRID] = RegulatingControl_class(mRID=regulating_control_mRID,
                                                              name='RegulatingControl_' + name,
                                                              targetValue=targetValue,
                                                              mode='http://iec.ch/TC57/2013/CIM-schema-cim16#RegulatingControlModeKind.voltage#')
        # ADD targetValueUnitMultiplier --> fix class in cimpy
        
        # create Synchronous machine object
        SynchronousMachine_module = importlib.import_module((module_name + 'SynchronousMachine'))
        SynchronousMachine_class = getattr(SynchronousMachine_module, 'SynchronousMachine')
        res[mRID] = SynchronousMachine_class(mRID=mRID,
                                            name=name,
                                            p=p,
                                            q=q,
                                            ratedS=ratedS,
                                            ratedU=ratedU,
                                            RegulatingControl=res[regulating_control_mRID],
                                            GeneratingUnit=res[regulating_control_mRID],
                                            Terminals=[res[terminal_mRID]])
        
        # connect terminal with synchronous machine
        res[terminal_mRID].ConductingEquipment = res[mRID]
       
        # Append the Terminal to the terminals list of the TopologicalNode
        res[mRID_node].Terminal.append(res[terminal_mRID])
        
        cim_topology['topology'] = res
        return cim_topology

    else:
        print('WARN: No Topological with mRID={} found in cim topology, Synchronous Machine name={} will be not added to cim topology!'.format(mRID_node, name))
        return cim_topology

def extend_SynchronousMachineTimeConstantReactance(cim_topology, version, name="", mRID="", SynchronousMachine_mRID="", 
                                                   damping=0, inertia=0, statorResistance=0, statorLeakageReactance=0, 
                                                   tpdo=0, tpqo=0, tppdo=0, tppqo=0, xDirectSubtrans=0, xDirectSync=0, 
                                                   xDirectTrans=0, xQuadSubtrans=0, xQuadSync=0, xQuadTrans=0):
    """
    Function to add element of type SynchronousMachineTimeConstantReactance to existing cim topology

    ...

    Parameters
    ----------
    cim_topology : dict
        existing cim topology
    version : str
        cgmes version. Actually only version 2.4.15 is supported
    name : str
        name of the synchronous machine to be added
    mRID : str
        uuid for the synchronous machine. If mRID=="", it will be automatically generated
    SynchronousMachine_mRID : str
        uuid of the synchronous machine to which this object belongs

    Returns
    ------- 
    import_result
    dict containing the modified cim topology
    """
    
    res = cim_topology['topology']
    
    if mRID in res:
        print('WARN: SynchronousMachineTimeConstantReactance mRID="{}" is already included in the cim topology, object will be not be addd to cim topology"'.format(mRID))
        return cim_topology
    
    # search for the synchonous machine
    synchronous_machine = None
    if SynchronousMachine_mRID in res.keys():
        synchronous_machine = res[SynchronousMachine_mRID]
    else:
        print('WARN: SynchronousMachine mRID={} coud not be found in the cim topology, object of type SynchronousMachineTimeConstantReactance will be not addd to cim topology'.format(SynchronousMachine_mRID))
        return cim_topology
    
    if name == "":
        name = synchronous_machine.name + "_TimeConstantReactance"
    
    if mRID == "":
        mRID = str(uuid.uuid4())
        
    module_name = "cimpy." + version + "."

    # create object of type SynchronousMachineTimeConstantReactance
    SynchronousMachineTCR_module = importlib.import_module((module_name + 'SynchronousMachineTimeConstantReactance'))
    SynchronousMachineTCR_class = getattr(SynchronousMachineTCR_module, 'SynchronousMachineTimeConstantReactance')
    res[name] = SynchronousMachineTCR_class(mRID=mRID,
                                    name=name,
                                    SynchronousMachine=synchronous_machine,
                                    damping=damping,
                                    inertia=inertia,
                                    statorResistance=statorResistance,
                                    statorLeakageReactance=statorLeakageReactance,
                                    tpdo=tpdo,
                                    tpqo=tpqo,
                                    tppdo=tppdo,
                                    tppqo=tppqo,
                                    xDirectSubtrans=xDirectSubtrans,
                                    xDirectSync=xDirectSync,
                                    xDirectTrans=xDirectTrans,
                                    xQuadSubtrans=xQuadSubtrans,
                                    xQuadSync=xQuadSync,
                                    xQuadTrans=xQuadTrans)
    # TODO: Add <cim:SynchronousMachineTimeConstantReactance.modelType rdf:resource="http://iec.ch/TC57/2013/CIM-schema-cim16#SynchronousMachineModelKind.subtransient" />
    # TODO: Add <cim:SynchronousMachineTimeConstantReactance.rotorType rdf:resource="http://iec.ch/TC57/2013/CIM-schema-cim16#RotorKind.salientPole" 
    
    cim_topology['topology'] = res

    return cim_topology


def add_EnergyConsumer(cim_topology, version, name, mRID="", mRID_node="", node_name="", p_nom=0, q_nom=0, 
                        p_init=0, q_init=0, baseVoltage=""):
    """
    Function to add element of type SynchronousMachineTimeConstantReactance to existing cim topology

    ...

    Parameters
    ----------
    cim_topology : dict
        existing cim topology
    version : str
        cgmes version. Actually only version 2.4.15 is supported
    name : str
        name of the synchronous machine to be added
    mRID_node : str
        uuid of the node to which this synchronous machine has to be connected
    mRID : str
        uuid for the synchronous machine. If mRID=="", it will be automatically generated
    SynchronousMachine_mRID : str
        uuid of the synchronous machine to which this object belongs
    p_nom: float 
        Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Unit: MW
    q_nom: float 
        Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Unit: MVA
    p_init : float
        Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Unit: MW
    q_init : float
        Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Unit: MVAr
    baseVoltage: float 
        Unit: kV
    Returns
    ------- 
    import_result
    dict containing the modified cim topology
    """
    
    res = cim_topology['topology']
    TopologicalNode = ''
    
    if mRID in res:
        print('WARN: EnergyConsumer mRID={} is already included in the cim topology, object will be not be addd to cim topology'.format(mRID))
        return cim_topology
    
    if mRID == "":
        mRID = str(uuid.uuid4())

    if (node_name!="" and mRID_node==""):
        for uuid_, obj in res.items():
            if isinstance(obj, cimpy.cgmes_v2_4_15.TopologicalNode):
                if (obj.name==node_name):
                    mRID_node=uuid_
                
    # search for the node mRID_node
    TopologicalNode = None
    if 'TopologicalNode' in str(type(res[mRID_node])):
        TopologicalNode = res[mRID_node]
    elif 'ConnectivityNode' in str(type(res[mRID_node])):
        TopologicalNode = res[mRID_node].TopologicalNode
                   

    if TopologicalNode is not None:
        #module_name = "cimpy." + version + ".Equipment."
        module_name = "cimpy." + version + "."
        
        # create terminal for this energyConsumer
        terminal_mRID = str(uuid.uuid4())
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal_mRID] = terminal_class(mRID='Terminal_' + name,
                                            name=terminal_mRID,
                                            TopologicalNode=TopologicalNode)

        # create terminal for this energyConsumer
        EnergyConsumer_module = importlib.import_module((module_name + 'EnergyConsumer'))
        EnergyConsumer_class = getattr(EnergyConsumer_module, 'EnergyConsumer')
        res[mRID] = EnergyConsumer_class(mRID=mRID,
                                        name=name,
                                        p=p_nom,
                                        q=q_nom,
                                        BaseVoltage=create_BaseVoltage(res, baseVoltage),
                                        Terminals=[res[terminal_mRID]])
        
        # create SvPowerFlow for this energyConsumer
        SvPowerFlow_module = importlib.import_module((module_name + 'SvPowerFlow'))
        SvPowerFlow_class = getattr(SvPowerFlow_module, 'SvPowerFlow')
        res[str(uuid.uuid4())] = SvPowerFlow_class(p=p_init,
                                              q=q_init,
                                              Terminal = res[terminal_mRID])
        
        # set conductingEquipment of the terminal
        res[terminal_mRID].ConductingEquipment = res[mRID]

        # Append the Terminal to the terminals list of the TopologicalNode
        res[mRID_node].Terminal.append(res[terminal_mRID])
   
        cim_topology['topology'] = res
        return cim_topology    
    else:
        print('WARN: TopologicalNode mRID={} coud not be found in the cim topology, object of type EnergyConsumer will be not addd to cim topology'.format(mRID_node))
        
        return cim_topology


def add_PowerTransfomer(cim_topology, version, name, mRID="", mRID_node1="", node1_name="", mRID_node2="", node2_name="", r=0, x=0, nominal_voltage_end1=0, nominal_voltage_end2=0):
    """
    Function to add PowerTransfomer objects to existing cim topology

    ...

    Parameters
    ----------
    cim_topology : dict
        existing cim topology
    version : str
        cgmes version. Actually only version 2.4.15 is supported
    name : str
        name of the PowerTransfomer to be added
    mRID : str
        uuid for the PowerTransfomer. If mRID=="", it will be automatically generate
    mRID_node1 : str
        uuid of the first node to which this PowerTransfomer has to be connected
    mRID_node2 : str
        uuid of the second node to which this PowerTransfomer machine has to be connecteds
    r : float
       Resistance (star-model) of the transformer end. The attribute shall be equal or greater than zero for non-equivalent transformers.
       It has to be referred to the node mRID_node1. Unit: Ohm
    x : float
        Positive sequence series reactance (star-model) of the transformer end.
        It has to be referred to the node mRID_node1. Unit: Ohm
    bch : float
        Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. This value represents the full charging over the full length of the line. Unit: S
    gch : float
        Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section. Unit: S
    nominal_voltage_end1: float
        Nominal Voltage of the node mRID_node1
    nominal_voltage_end2: float
        Nominal Voltage of this line
        
    Returns
    ------- 
    import_result
    dict containing the modified cim topology
    """
    
    res = cim_topology['topology']
    
    if name in res:
        print('WARN: PowerTransformer mRID="{}" is already included in the cim topology, object will be not be addd to cim topology"', mRID)
        return cim_topology

    # Creating random mRID using uuid4()
    if mRID == "":
        mRID = str(uuid.uuid4())
        
    if (node1_name!="" and mRID_node1==""):
        for uuid_, obj in res.items():
            if hasattr(obj, 'name'):
                if (obj.name==node1_name):
                    mRID_node1=uuid_
    if (node2_name!="" and mRID_node2==""):
        for uuid_, obj in res.items():
            if hasattr(obj, 'name'):
                if (obj.name==node2_name):
                    mRID_node2=uuid_
    
    # look for topological nodels connected to line            
    TopologicalNode1 = None
    TopologicalNode2 = None
    if mRID_node1 in res:
        if 'TopologicalNode' in str(type(res[mRID_node1])):
            TopologicalNode1 = res[mRID_node1]
        elif 'ConnectivityNode' in str(type(res[mRID_node1])):
            TopologicalNode1 = res[mRID_node1].TopologicalNode

    if mRID_node2 in res:
        if 'TopologicalNode' in str(type(res[mRID_node2])):
            TopologicalNode2 = res[mRID_node2]
        elif 'ConnectivityNode' in str(type(res[mRID_node2])):
            TopologicalNode2 = res[mRID_node2].TopologicalNode
             
    if (TopologicalNode1 is not None) and (TopologicalNode2 is not None):       

        module_name = "cimpy." + version + "."        
        
        # create terminals for this Trafo
        terminal1_mRID = str(uuid.uuid4())
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal1_mRID] = terminal_class(mRID=terminal1_mRID,
                                            name='Terminal_1_' + name,
                                            sequenceNumber=1,
                                            TopologicalNode=TopologicalNode1)
        terminal2_mRID = str(uuid.uuid4())
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        res[terminal2_mRID] = terminal_class(mRID=terminal2_mRID,
                                            name='Terminal_2_' + name,
                                            sequenceNumber=2,
                                            TopologicalNode=TopologicalNode2)
        
        # create PowerTransformer object
        PowerTransformer_module = importlib.import_module((module_name + 'PowerTransformer'))
        PowerTransformer_class = getattr(PowerTransformer_module, 'PowerTransformer')
        res[mRID] = PowerTransformer_class(mRID=mRID,
                                           name=name,
                                           Terminals = [res[terminal1_mRID], res[terminal2_mRID]])
        
        # create PowerTransformerEnd objects
        End1_mRID = str(uuid.uuid4())
        PowerTransformerEnd_module = importlib.import_module((module_name + 'PowerTransformerEnd'))
        PowerTransformerEnd_class = getattr(PowerTransformerEnd_module, 'PowerTransformerEnd')
        res[End1_mRID] = PowerTransformerEnd_class(mRID=End1_mRID,
                                                   name=name+"1",
                                                   ratedU=nominal_voltage_end1,
                                                   r=r,
                                                   x=x,
                                                   endNumber=1,
                                                   Terminal=res[terminal1_mRID],
                                                   PowerTransformer=res[mRID])
        End2_mRID = str(uuid.uuid4())
        res[End2_mRID] = PowerTransformerEnd_class(mRID=End2_mRID,
                                                   name=name+"2",
                                                   ratedU=nominal_voltage_end2,
                                                   endNumber=2,
                                                   Terminal=res[terminal2_mRID],
                                                   PowerTransformer=res[mRID])
        
        res[mRID].PowerTransformerEnd = [res[End1_mRID], res[End2_mRID]]

        res[terminal1_mRID].ConductingEquipment = res[mRID]
        res[terminal2_mRID].ConductingEquipment = res[mRID]
   
        # Append the Terminal List of the TopologicalNodes
        res[mRID_node1].Terminal.append(res[terminal1_mRID])
        res[mRID_node2].Terminal.append(res[terminal2_mRID])
        
        cim_topology['topology'] = res

    elif TopologicalNode1 is None:
        print('WARN: No Topological with mRID={} found in cim topology, PowerTransformer name={} will be not added to cim topology!'.format(mRID_node1, name))
        
    if TopologicalNode2 is None:
        print('WARN: No Topological with mRID={} found in cim topology, PowerTransformer name={} will be not added to cim topology!'.format(mRID_node2, name))

    return cim_topology


def create_BaseVoltage(cim_topology, nominalVoltage):
    """
    Function to add element of type BaseVoltage to existing cim topology

    ...

    Parameters
    ----------
    cim_topology : dict
        existing cim topology
    version : str
        cgmes version. Actually only version 2.4.15 is supported
    name : float
        nominalVoltage: The power system resource's base voltage. Unit: kV


    Returns
    ------- 
    mRID:
        str containing the mRID of the BaseVoltage
    cim_topology:
        dict containing the modified cim topology
    """
    # check if this voltage already exists in the topoplogy
    for mRID, obj in cim_topology.items():
        if isinstance(obj, cimpy.cgmes_v2_4_15.BaseVoltage):
            if (obj.nominalVoltage == nominalVoltage):
                return mRID
    
    name = 'Base Voltage {:.2f}kV'.format(nominalVoltage)
    mRID = str(uuid.uuid4())
    
    # create object of type BaseVoltage
    module_name = "cimpy." + "cgmes_v2_4_15" + "."
    BaseVoltage_module = importlib.import_module((module_name + 'BaseVoltage'))
    BaseVoltage_class = getattr(BaseVoltage_module, 'BaseVoltage')
    BaseVoltage = BaseVoltage_class(name=name, 
                                    mRID=mRID,
                                    nominalVoltage=nominalVoltage)
    cim_topology[mRID] = BaseVoltage

    return BaseVoltage

# Switch Module with infinity Conductance to simulate a short circuit in network "import_result" at the node with name "mRID"
def add_ShortCircuit_Switch(import_result, version, mRID, name = "ShortCircuit_Switch"):
    res = import_result['topology']
    TopologicalNode = ''
    
    if name in res:
        print(name, "is already included, ... create ShortCircuit_Switch with new mRID")
        name = name + str(list(res.keys()).count("ShortCircuit_Switch") + 1)

    if mRID in res:
        if 'TopologicalNode' in str(type(res[mRID])):
            TopologicalNode = res[mRID]
        elif 'ConnectivityNode' in str(type(res[mRID])):
            TopologicalNode = res[mRID].TopologicalNode

    if TopologicalNode != '':
        # Add two Topological Nodes
        BaseVoltage = TopologicalNode.BaseVoltage
        v = TopologicalNode.SvVoltage.v
        angle = TopologicalNode.SvVoltage.angle
        Node_name = "Node_" + name
        import_result = add_TopologicalNode(import_result, "cgmes_v2_4_15", BaseVoltage, v, angle, Node_name)

        terminal_name = 'Terminal_' + name
        SwitchSchedule_name = 'Schedule_' + name 
        GroundingImpedance_name = 'GroundingImpedance_' + name

        # module_name = "cimpy." + version + ".Equipment."
        module_name = "cimpy." + version + "."
        
        # Create Terminals
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal_name] = terminal_class(mRID=terminal_name,
                                            name=terminal_name,
                                            TopologicalNode=TopologicalNode)
        
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal_name + "1"] = terminal_class(mRID=terminal_name + "1",
                                            name=terminal_name + "1",
                                            TopologicalNode=res[Node_name])
        
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal_name + "2"] = terminal_class(mRID=terminal_name + "2",
                                            name=terminal_name + "2",
                                            TopologicalNode=res[Node_name])
        

        # Create Components
        SwitchSchedule_module = importlib.import_module((module_name + 'SwitchSchedule'))
        SwitchSchedule_class = getattr(SwitchSchedule_module, 'SwitchSchedule')
        res[SwitchSchedule_name] = SwitchSchedule_class(mRID=SwitchSchedule_name,
                                name=SwitchSchedule_name,
                                startTime = datetime.datetime.now(),
                               # timeStep = 0.5,    # The time between each pair of subsequent regular time points in sequence order.
                                endTime = datetime.datetime.now() + datetime.timedelta(seconds=10))       # The time for the last time point
        
        switch_module = importlib.import_module((module_name + 'Switch'))
        switch_class = getattr(switch_module, 'Switch')
        res[name] = switch_class(mRID=name,
                                name=name,
                                SwitchSchedules = [res[SwitchSchedule_name]],
                                Terminals = [res[terminal_name], res[terminal_name + "1"]])
        
        GroundingImpedance_module = importlib.import_module((module_name + 'GroundingImpedance'))
        GroundingImpedance_class = getattr(GroundingImpedance_module, 'GroundingImpedance')
        res[GroundingImpedance_name] = GroundingImpedance_class(mRID=GroundingImpedance_name,
                                name=GroundingImpedance_name,
                                r = 10e-10,
                                Terminals = [res[terminal_name + "2"]])
        
        
        res[terminal_name].ConductingEquipment = res[name]
        res[terminal_name + "1"].ConductingEquipment = res[name]
        res[terminal_name + "2"].ConductingEquipment = res[GroundingImpedance_name] 

        # Append the Terminal List of the TopologicalNode
        res[mRID].Terminal.append(res[terminal_name])
        res[Node_name].Terminal.append(res[terminal_name + "1"])
        res[Node_name].Terminal.append(res[terminal_name + "2"])

    else:
        print('No Terminal with mRID ', mRID, ' found in object list!')
        return 0

    import_result['topology'] = res

    return import_result

# Switch Module with zero Conductance to simulate an open clamp in network "import_result" at the node with name "mRID"
def add_OpenClamp_Switch(import_result, version, mRID, name = "OpenClamp_Switch"):
    res = import_result['topology']
    TopologicalNode = ''
    
    if name in res:
        print(name, "is already included, ... create OpenClamp_Switch with new mRID")
        name = name + str(list(res.keys()).count("OpenClamp_Switch") + 1)

    if mRID in res:
        if 'TopologicalNode' in str(type(res[mRID])):
            TopologicalNode = res[mRID]
        elif 'ConnectivityNode' in str(type(res[mRID])):
            TopologicalNode = res[mRID].TopologicalNode

    if TopologicalNode != '':
        # Add two Topological Nodes
        BaseVoltage = TopologicalNode.BaseVoltage
        v = TopologicalNode.SvVoltage.v
        angle = TopologicalNode.SvVoltage.angle
        Node_name = "Node_" + name
        import_result = add_TopologicalNode(import_result, "cgmes_v2_4_15", BaseVoltage, v, angle, Node_name)

        terminal_name = 'Terminal_' + name
        SwitchSchedule_name = 'Schedule_' + name 
        GroundingImpedance_name = 'GroundingImpedance_' + name

        # module_name = "cimpy." + version + ".Equipment."
        module_name = "cimpy." + version + "."
        
        # Create Terminals
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal_name] = terminal_class(mRID=terminal_name,
                                            name=terminal_name,
                                            TopologicalNode=TopologicalNode)
        
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal_name + "1"] = terminal_class(mRID=terminal_name + "1",
                                            name=terminal_name + "1",
                                            TopologicalNode=res[Node_name])
        
        terminal_module = importlib.import_module((module_name + 'Terminal'))
        terminal_class = getattr(terminal_module, 'Terminal')
        res[terminal_name + "2"] = terminal_class(mRID=terminal_name + "2",
                                            name=terminal_name + "2",
                                            TopologicalNode=res[Node_name])
        

        # Create Components
        SwitchSchedule_module = importlib.import_module((module_name + 'SwitchSchedule'))
        SwitchSchedule_class = getattr(SwitchSchedule_module, 'SwitchSchedule')
        res[SwitchSchedule_name] = SwitchSchedule_class(mRID=SwitchSchedule_name,
                                name=SwitchSchedule_name,
                                timeStep = 0.5,    # The time between each pair of subsequent regular time points in sequence order.
                                endTime = 1)       # The time for the last time point
        
        switch_module = importlib.import_module((module_name + 'Switch'))
        switch_class = getattr(switch_module, 'Switch')
        res[name] = switch_class(mRID=name,
                                name=name,
                                SwitchSchedules = [res[SwitchSchedule_name]],
                                Terminals = [res[terminal_name], res[terminal_name + "1"]])
        
        GroundingImpedance_module = importlib.import_module((module_name + 'GroundingImpedance'))
        GroundingImpedance_class = getattr(GroundingImpedance_module, 'GroundingImpedance')
        res[GroundingImpedance_name] = GroundingImpedance_class(mRID=GroundingImpedance_name,
                                name=GroundingImpedance_name,
                                r = 10e10,
                                Terminals = [res[terminal_name + "2"]])
        
        
        res[terminal_name].ConductingEquipment = res[name]
        res[terminal_name + "1"].ConductingEquipment = res[name]
        res[terminal_name + "2"].ConductingEquipment = res[GroundingImpedance_name] 

        # Append the Terminal List of the TopologicalNode
        res[mRID].Terminal.append(res[terminal_name])
        res[Node_name].Terminal.append(res[terminal_name + "1"])
        res[Node_name].Terminal.append(res[terminal_name + "2"])

    else:
        print('No Terminal with mRID ', mRID, ' found in object list!')
        return 0

    import_result['topology'] = res

    return import_result