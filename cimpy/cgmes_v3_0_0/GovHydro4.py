from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydro4(TurbineGovernorDynamics):
	'''
	Hydro turbine and governor. Represents plants with straight-forward penstock configurations and hydraulic governors of the traditional 'dashpot' type.  This model can be used to represent simple, Francis/Pelton or Kaplan turbines.

	:mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
	:tg: Gate servo time constant (<i>Tg</i>) (&gt; 0).  Typical value = 0,5. Default: 0
	:tp: Pilot servo time constant (<i>Tp</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:uo: Max gate opening velocity (<i>Uo</i>).  Typical value = 0,2. Default: 0.0
	:uc: Max gate closing velocity (<i>Uc</i>).  Typical value = 0,2. Default: 0.0
	:gmax: Maximum gate opening, PU of <i>MWbase</i> (<i>Gmax</i>) (&gt; GovHydro4.gmin).  Typical value = 1. Default: 0.0
	:gmin: Minimum gate opening, PU of <i>MWbase</i> (<i>Gmin</i>) (&lt; GovHydro4.gmax).  Typical value = 0. Default: 0.0
	:rperm: Permanent droop (<i>Rperm</i>) (&gt;= 0).  Typical value = 0,05. Default: 0
	:rtemp: Temporary droop (<i>Rtemp</i>) (&gt;= 0).  Typical value = 0,3. Default: 0
	:tr: Dashpot time constant (<i>Tr</i>) (&gt;= 0).  Typical value = 5. Default: 0
	:tw: Water inertia time constant (<i>Tw</i>) (&gt; 0).  Typical value = 1. Default: 0
	:at: Turbine gain (<i>At</i>).  Typical value = 1,2. Default: 0.0
	:dturb: Turbine damping factor (<i>Dturb</i>).  Unit = delta P (PU of <i>MWbase</i>) / delta speed (PU).  Typical value for simple = 0,5, Francis/Pelton = 1,1, Kaplan = 1,1. Default: 0.0
	:hdam: Head available at dam (<i>hdam</i>).  Typical value = 1. Default: 0.0
	:qnl: No-load flow at nominal head (<i>Qnl</i>). Typical value for simple = 0,08, Francis/Pelton = 0, Kaplan = 0. Default: 0.0
	:db1: Intentional deadband width (<i>db1</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
	:eps: Intentional db hysteresis (<i>eps</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
	:db2: Unintentional dead-band (<i>db2</i>).  Unit = MW.  Typical value = 0. Default: 0.0
	:gv0: Nonlinear gain point 0, PU gv (<i>Gv0</i>) (= 0 for simple).  Typical for Francis/Pelton = 0,1, Kaplan = 0,1. Default: 0.0
	:pgv0: Nonlinear gain point 0, PU power (<i>Pgv0</i>) (= 0 for simple).  Typical value = 0. Default: 0.0
	:gv1: Nonlinear gain point 1, PU gv (<i>Gv1</i>) (= 0 for simple, &gt; GovHydro4.gv0 for Francis/Pelton and Kaplan). Typical value for Francis/Pelton = 0,4, Kaplan = 0,4. Default: 0.0
	:pgv1: Nonlinear gain point 1, PU power (<i>Pgv1</i>) (= 0 for simple). Typical value for Francis/Pelton = 0,42, Kaplan = 0,35. Default: 0.0
	:gv2: Nonlinear gain point 2, PU gv (<i>Gv2</i>) (= 0 for simple, &gt; GovHydro4.gv1 for Francis/Pelton and Kaplan). Typical value for Francis/Pelton = 0,5, Kaplan = 0,5. Default: 0.0
	:pgv2: Nonlinear gain point 2, PU power (<i>Pgv2</i>) (= 0 for simple). Typical value for Francis/Pelton = 0,56, Kaplan = 0,468. Default: 0.0
	:gv3: Nonlinear gain point 3, PU gv (<i>Gv3</i>)  (= 0 for simple, &gt; GovHydro4.gv2 for Francis/Pelton and Kaplan). Typical value for Francis/Pelton = 0,7, Kaplan = 0,7. Default: 0.0
	:pgv3: Nonlinear gain point 3, PU power (<i>Pgv3</i>) (= 0 for simple). Typical value for Francis/Pelton = 0,8, Kaplan = 0,796. Default: 0.0
	:gv4: Nonlinear gain point 4, PU gv (<i>Gv4</i>)  (= 0 for simple, &gt; GovHydro4.gv3 for Francis/Pelton and Kaplan). Typical value for  Francis/Pelton = 0,8, Kaplan = 0,8. Default: 0.0
	:pgv4: Nonlinear gain point 4, PU power (<i>Pgv4</i>) (= 0 for simple). Typical value for Francis/Pelton = 0,9, Kaplan = 0,917. Default: 0.0
	:gv5: Nonlinear gain point 5, PU gv (<i>Gv5</i>)  (= 0 for simple, &lt; 1 and &gt; GovHydro4.gv4 for Francis/Pelton and Kaplan). Typical value for Francis/Pelton = 0,9, Kaplan = 0,9. Default: 0.0
	:pgv5: Nonlinear gain point 5, PU power (<i>Pgv5</i>) (= 0 for simple).  Typical value for Francis/Pelton = 0,97, Kaplan = 0,99. Default: 0.0
	:bgv0: Kaplan blade servo point 0 (<i>Bgv0</i>) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0. Default: 0.0
	:bgv1: Kaplan blade servo point 1 (<i>Bgv1</i>) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0. Default: 0.0
	:bgv2: Kaplan blade servo point 2 (<i>Bgv2</i>) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0,1. Default: 0.0
	:bgv3: Kaplan blade servo point 3 (<i>Bgv3</i>) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0,667. Default: 0.0
	:bgv4: Kaplan blade servo point 4 (<i>Bgv4</i>) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0,9. Default: 0.0
	:bgv5: Kaplan blade servo point 5 (<i>Bgv5</i>) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 1. Default: 0.0
	:bmax: Maximum blade adjustment factor (<i>Bmax</i>)  (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 1,1276. Default: 0.0
	:tblade: Blade servo time constant (<i>Tblade</i>) (&gt;= 0).  Typical value = 100. Default: 0
	:model: The kind of model being represented (simple, Francis/Pelton or Kaplan). Default: None
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'tg': [cgmesProfile.DY.value, ],
						'tp': [cgmesProfile.DY.value, ],
						'uo': [cgmesProfile.DY.value, ],
						'uc': [cgmesProfile.DY.value, ],
						'gmax': [cgmesProfile.DY.value, ],
						'gmin': [cgmesProfile.DY.value, ],
						'rperm': [cgmesProfile.DY.value, ],
						'rtemp': [cgmesProfile.DY.value, ],
						'tr': [cgmesProfile.DY.value, ],
						'tw': [cgmesProfile.DY.value, ],
						'at': [cgmesProfile.DY.value, ],
						'dturb': [cgmesProfile.DY.value, ],
						'hdam': [cgmesProfile.DY.value, ],
						'qnl': [cgmesProfile.DY.value, ],
						'db1': [cgmesProfile.DY.value, ],
						'eps': [cgmesProfile.DY.value, ],
						'db2': [cgmesProfile.DY.value, ],
						'gv0': [cgmesProfile.DY.value, ],
						'pgv0': [cgmesProfile.DY.value, ],
						'gv1': [cgmesProfile.DY.value, ],
						'pgv1': [cgmesProfile.DY.value, ],
						'gv2': [cgmesProfile.DY.value, ],
						'pgv2': [cgmesProfile.DY.value, ],
						'gv3': [cgmesProfile.DY.value, ],
						'pgv3': [cgmesProfile.DY.value, ],
						'gv4': [cgmesProfile.DY.value, ],
						'pgv4': [cgmesProfile.DY.value, ],
						'gv5': [cgmesProfile.DY.value, ],
						'pgv5': [cgmesProfile.DY.value, ],
						'bgv0': [cgmesProfile.DY.value, ],
						'bgv1': [cgmesProfile.DY.value, ],
						'bgv2': [cgmesProfile.DY.value, ],
						'bgv3': [cgmesProfile.DY.value, ],
						'bgv4': [cgmesProfile.DY.value, ],
						'bgv5': [cgmesProfile.DY.value, ],
						'bmax': [cgmesProfile.DY.value, ],
						'tblade': [cgmesProfile.DY.value, ],
						'model': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, tg = 0, tp = 0, uo = 0.0, uc = 0.0, gmax = 0.0, gmin = 0.0, rperm = 0, rtemp = 0, tr = 0, tw = 0, at = 0.0, dturb = 0.0, hdam = 0.0, qnl = 0.0, db1 = 0.0, eps = 0.0, db2 = 0.0, gv0 = 0.0, pgv0 = 0.0, gv1 = 0.0, pgv1 = 0.0, gv2 = 0.0, pgv2 = 0.0, gv3 = 0.0, pgv3 = 0.0, gv4 = 0.0, pgv4 = 0.0, gv5 = 0.0, pgv5 = 0.0, bgv0 = 0.0, bgv1 = 0.0, bgv2 = 0.0, bgv3 = 0.0, bgv4 = 0.0, bgv5 = 0.0, bmax = 0.0, tblade = 0, model = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.tg = tg
		self.tp = tp
		self.uo = uo
		self.uc = uc
		self.gmax = gmax
		self.gmin = gmin
		self.rperm = rperm
		self.rtemp = rtemp
		self.tr = tr
		self.tw = tw
		self.at = at
		self.dturb = dturb
		self.hdam = hdam
		self.qnl = qnl
		self.db1 = db1
		self.eps = eps
		self.db2 = db2
		self.gv0 = gv0
		self.pgv0 = pgv0
		self.gv1 = gv1
		self.pgv1 = pgv1
		self.gv2 = gv2
		self.pgv2 = pgv2
		self.gv3 = gv3
		self.pgv3 = pgv3
		self.gv4 = gv4
		self.pgv4 = pgv4
		self.gv5 = gv5
		self.pgv5 = pgv5
		self.bgv0 = bgv0
		self.bgv1 = bgv1
		self.bgv2 = bgv2
		self.bgv3 = bgv3
		self.bgv4 = bgv4
		self.bgv5 = bgv5
		self.bmax = bmax
		self.tblade = tblade
		self.model = model
		
	def __str__(self):
		str = 'class=GovHydro4\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
