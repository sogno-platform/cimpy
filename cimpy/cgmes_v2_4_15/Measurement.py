from .IdentifiedObject import IdentifiedObject


class Measurement(IdentifiedObject):
	'''
	A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  If both a Terminal and PSR are associated, and the PSR is of type ConductingEquipment, the associated Terminal should belong to that ConductingEquipment instance. When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.

	:measurementType: Specifies the type of measurement.  For example, this specifies if the measurement represents an indoor temperature, outdoor temperature, bus voltage, line flow, etc. Default: ''
	:phases: Indicates to which phases the measurement applies and avoids the need to use `measurementType` to also encode phase information (which would explode the types). The phase information in Measurement, along with `measurementType` and `phases` uniquely defines a Measurement for a device, based on normal network phase. Their meaning will not change when the computed energizing phasing is changed due to jumpers or other reasons. If the attribute is missing three phases (ABC) shall be assumed. Default: None
	:unitSymbol: The unit of measure of the measured quantity. Default: None
	:unitMultiplier: The unit multiplier of the measured quantity. Default: None
	:Terminal: One or more measurements may be associated with a terminal in the network. Default: None
	:PowerSystemResource: The measurements associated with this power system resource. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'measurementType': [cgmesProfile.EQ.value, ],
						'phases': [cgmesProfile.EQ.value, ],
						'unitSymbol': [cgmesProfile.EQ.value, ],
						'unitMultiplier': [cgmesProfile.EQ.value, ],
						'Terminal': [cgmesProfile.EQ.value, ],
						'PowerSystemResource': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, measurementType = '', phases = None, unitSymbol = None, unitMultiplier = None, Terminal = None, PowerSystemResource = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.measurementType = measurementType
		self.phases = phases
		self.unitSymbol = unitSymbol
		self.unitMultiplier = unitMultiplier
		self.Terminal = Terminal
		self.PowerSystemResource = PowerSystemResource
		
	def __str__(self):
		str = 'class=Measurement\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
