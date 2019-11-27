from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class PowerSystemResource(IdentifiedObject):
	'''
	A power system resource can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated.

	:Location: Location of this power system resource. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.EQ.value, cgmesProfile.GL.value, cgmesProfile.SSH.value, ],
						'Location': [cgmesProfile.GL.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Location = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Location = Location
		
	def __str__(self):
		str = 'class=PowerSystemResource\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
