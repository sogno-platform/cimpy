from cimpy.cgmes_v2_4_15.Curve import Curve


class ReactiveCapabilityCurve(Curve):
	'''
	Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.

	:EquivalentInjection: The reactive capability curve used by this equivalent injection. Default: "many"
	:InitiallyUsedBySynchronousMachines: The default reactive capability curve for use by a synchronous machine. Default: "many"
		'''

	cgmesProfile = Curve.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'EquivalentInjection': [cgmesProfile.EQ.value, ],
						'InitiallyUsedBySynchronousMachines': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class Curve: \n' + Curve.__doc__ 

	def __init__(self, EquivalentInjection = "many", InitiallyUsedBySynchronousMachines = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EquivalentInjection = EquivalentInjection
		self.InitiallyUsedBySynchronousMachines = InitiallyUsedBySynchronousMachines
		
	def __str__(self):
		str = 'class=ReactiveCapabilityCurve\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
