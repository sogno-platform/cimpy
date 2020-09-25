from .IdentifiedObject import IdentifiedObject


class PowerSystemResource(IdentifiedObject):
	'''
	A power system resource can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated.

	:Controls: Regulating device governed by this control output. Default: "list"
	:Measurements: The power system resource that contains the measurement. Default: "list"
	:Location: Location of this power system resource. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.GL.value, cgmesProfile.DY.value, cgmesProfile.EQ_BD.value, ],
						'Controls': [cgmesProfile.EQ.value, ],
						'Measurements': [cgmesProfile.EQ.value, ],
						'Location': [cgmesProfile.GL.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Controls = "list", Measurements = "list", Location = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Controls = Controls
		self.Measurements = Measurements
		self.Location = Location
		
	def __str__(self):
		str = 'class=PowerSystemResource\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
