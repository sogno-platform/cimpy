from .Curve import Curve


class GrossToNetActivePowerCurve(Curve):
	'''
	Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.

	:GeneratingUnit: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit. Default: None
		'''

	cgmesProfile = Curve.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'GeneratingUnit': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Curve: \n' + Curve.__doc__ 

	def __init__(self, GeneratingUnit = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.GeneratingUnit = GeneratingUnit
		
	def __str__(self):
		str = 'class=GrossToNetActivePowerCurve\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
