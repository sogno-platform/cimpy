from cimpy.cgmes_v2_4_15.Connector import Connector


class Junction(Connector):
	'''
	A point where one or more conducting equipments are connected with zero resistance.

		'''

	cgmesProfile = Connector.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class Connector: \n' + Connector.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=Junction\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
