from .Base import Base


class RegularTimePoint(Base):
	'''
	Time point for a schedule where the time between the consecutive points is constant.

	:IntervalSchedule: Regular interval schedule containing this time point. Default: None
	:sequenceNumber: The position of the regular time point in the sequence. Note that time points don`t have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the associated regular interval schedule`s time step with the regular time point sequence number and adding the associated schedules start time. Default: 0
	:value1: The first value at the time. The meaning of the value is defined by the derived type of the associated schedule. Default: 0.0
	:value2: The second value at the time. The meaning of the value is defined by the derived type of the associated schedule. Default: 0.0
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'IntervalSchedule': [cgmesProfile.EQ.value, ],
						'sequenceNumber': [cgmesProfile.EQ.value, ],
						'value1': [cgmesProfile.EQ.value, ],
						'value2': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, IntervalSchedule = None, sequenceNumber = 0, value1 = 0.0, value2 = 0.0,  ):
	
		self.IntervalSchedule = IntervalSchedule
		self.sequenceNumber = sequenceNumber
		self.value1 = value1
		self.value2 = value2
		
	def __str__(self):
		str = 'class=RegularTimePoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
