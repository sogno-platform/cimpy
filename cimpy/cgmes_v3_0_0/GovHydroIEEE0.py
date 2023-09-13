from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroIEEE0(TurbineGovernorDynamics):
	'''
	IEEE simplified hydro governor-turbine model.  Used for mechanical-hydraulic and electro-hydraulic turbine governors, with or without steam feedback. Typical values given are for mechanical-hydraulic turbine-governor. Ref<font color="#0f0f0f">erence: IEEE Transactions on Power Apparatus and Systems, November/December 1973, Volume PAS-92, Number 6, <i><u>Dynamic Models for Steam and Hydro Turbines in Power System Studies</u></i>, page 1904.</font>

	:mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
	:k: Governor gain (<i>K)</i>. Default: 0.0
	:t1: Governor lag time constant (<i>T1</i>) (&gt;= 0).  Typical value = 0,25. Default: 0
	:t2: Governor lead time constant (<i>T2)</i> (&gt;= 0).  Typical value = 0. Default: 0
	:t3: Gate actuator time constant (<i>T3</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:t4: Water starting time (<i>T4</i>) (&gt;= 0). Default: 0
	:pmax: Gate maximum (<i>Pmax</i>) (&gt; GovHydroIEEE0.pmin). Default: 0.0
	:pmin: Gate minimum (<i>Pmin</i>) (&lt; GovHydroIEEE.pmax). Default: 0.0
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, k = 0.0, t1 = 0, t2 = 0, t3 = 0, t4 = 0, pmax = 0.0, pmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.k = k
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.pmax = pmax
		self.pmin = pmin
		
	def __str__(self):
		str = 'class=GovHydroIEEE0\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
