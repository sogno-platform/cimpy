from  import Base


class RegularTimePoint(Base):
	'''
	Time point for a schedule where the time between the consecutive points is constant.

	:IntervalSchedule: Regular interval schedule containing this time point. Default: 
	:sequenceNumber: The position of the regular time point in the sequence. Note that time points don`t have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the associated regular interval schedule`s time step with the regular time point sequence number and adding the associated schedules start time. Default: 
	:value1: The first value at the time. The meaning of the value is defined by the derived type of the associated schedule. Default: 
	:value2: The second value at the time. The meaning of the value is defined by the derived type of the associated schedule. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'IntervalSchedule': [cgmesProfile.EQ.value, ],
						'sequenceNumber': [cgmesProfile.EQ.value, ],
						'value1': [cgmesProfile.EQ.value, ],
						'value2': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, IntervalSchedule = , sequenceNumber = , value1 = , value2 = ,  ):
	
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
