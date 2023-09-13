from .IdentifiedObject import IdentifiedObject


class PowerSystemResource(IdentifiedObject):
	'''
	A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated.

	:Location: Location of this power system resource. Default: None
	:Controls: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator. Default: "list"
	:Measurements: The measurements associated with this power system resource. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.GL.value, cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.OP.value, cgmesProfile.EQ.value, cgmesProfile.EQBD.value, cgmesProfile.SC.value, ],
						'Location': [cgmesProfile.GL.value, ],
						'Controls': [cgmesProfile.OP.value, ],
						'Measurements': [cgmesProfile.OP.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Location = None, Controls = "list", Measurements = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Location = Location
		self.Controls = Controls
		self.Measurements = Measurements
		
	def __str__(self):
		str = 'class=PowerSystemResource\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
