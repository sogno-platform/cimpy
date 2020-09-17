import importlib

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
    else:
        print('No Terminal with mRID ', mRID, ' found in object list!')

    import_result['topology'] = res

    return import_result
