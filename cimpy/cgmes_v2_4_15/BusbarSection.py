from cimpy.cgmes_v2_4_15.Connector import Connector


class BusbarSection(Connector):
	'''
	A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.

	:ipMax: Maximum allowable peak short-circuit current of busbar (Ipmax in the IEC 60909-0).  Mechanical limit of the busbar in the substation itself. Used for short circuit data exchange according to IEC 60909 Default: 0.0
		'''

	cgmesProfile = Connector.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'ipMax': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class Connector: \n' + Connector.__doc__ 

	def __init__(self, ipMax = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ipMax = ipMax
		
	def __str__(self):
		str = 'class=BusbarSection\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
