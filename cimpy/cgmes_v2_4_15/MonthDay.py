from cimpy.cgmes_v2_4_15.Base import Base


class MonthDay(Base):
	'''
	MonthDay format as "--mm-dd", which conforms with XSD data type gMonthDay.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=MonthDay\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
