from  import Base


class Quality61850(Base):
	'''
	Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.

	:badReference: Measurement value may be incorrect due to a reference being out of calibration. Default: 
	:estimatorReplaced: Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience. Default: 
	:failure: This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure. Default: 
	:oldData: Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval. Default: 
	:operatorBlocked: Measurement value is blocked and hence unavailable for transmission. Default: 
	:oscillatory: To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier `oscillatory` is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status `questionable` is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status `questionable` is reset and `invalid` is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status `invalid` is set immediately in addition to the detail quality identifier `oscillatory` (used for status information only). Default: 
	:outOfRange: Measurement value is beyond a predefined range of value. Default: 
	:overFlow: Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero. Default: 
	:source: Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted. Default: 
	:suspect: A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator. Default: 
	:test: Measurement value is transmitted for test purposes. Default: 
	:validity: Validity of the measurement value. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'badReference': [cgmesProfile.EQ.value, ],
						'estimatorReplaced': [cgmesProfile.EQ.value, ],
						'failure': [cgmesProfile.EQ.value, ],
						'oldData': [cgmesProfile.EQ.value, ],
						'operatorBlocked': [cgmesProfile.EQ.value, ],
						'oscillatory': [cgmesProfile.EQ.value, ],
						'outOfRange': [cgmesProfile.EQ.value, ],
						'overFlow': [cgmesProfile.EQ.value, ],
						'source': [cgmesProfile.EQ.value, ],
						'suspect': [cgmesProfile.EQ.value, ],
						'test': [cgmesProfile.EQ.value, ],
						'validity': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, badReference = , estimatorReplaced = , failure = , oldData = , operatorBlocked = , oscillatory = , outOfRange = , overFlow = , source = , suspect = , test = , validity = ,  ):
	
		self.badReference = badReference
		self.estimatorReplaced = estimatorReplaced
		self.failure = failure
		self.oldData = oldData
		self.operatorBlocked = operatorBlocked
		self.oscillatory = oscillatory
		self.outOfRange = outOfRange
		self.overFlow = overFlow
		self.source = source
		self.suspect = suspect
		self.test = test
		self.validity = validity
		
	def __str__(self):
		str = 'class=Quality61850\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
