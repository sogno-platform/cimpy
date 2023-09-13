from .IdentifiedObject import IdentifiedObject


class MeasurementValueSource(IdentifiedObject):
	'''
	MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are defined in IEC 61970-301.

	:MeasurementValues: The MeasurementValues updated by the source. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.OP.value, ],
						'MeasurementValues': [cgmesProfile.OP.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, MeasurementValues = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.MeasurementValues = MeasurementValues
		
	def __str__(self):
		str = 'class=MeasurementValueSource\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
