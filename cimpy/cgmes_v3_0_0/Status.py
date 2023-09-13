from .Base import Base


class Status(Base):
	'''
	Current status information relevant to an entity.

	:value: Status value at `dateTime`; prior status changes may have been kept in instances of activity records associated with the object to which this status applies. Default: ''
	:dateTime: Date and time for which status `value` applies. Default: ''
	:remark: Pertinent information regarding the current `value`, as free form text. Default: ''
	:reason: Reason code or explanation for why an object went to the current status `value`. Default: ''
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.GL.value, ],
						'value': [cgmesProfile.GL.value, ],
						'dateTime': [cgmesProfile.GL.value, ],
						'remark': [cgmesProfile.GL.value, ],
						'reason': [cgmesProfile.GL.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = '', dateTime = '', remark = '', reason = '',  ):
	
		self.value = value
		self.dateTime = dateTime
		self.remark = remark
		self.reason = reason
		
	def __str__(self):
		str = 'class=Status\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
