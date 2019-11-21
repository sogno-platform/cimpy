from cimpy.cgmes_v2_4_15_flat.EnergyConsumer import EnergyConsumer


class StationSupply(EnergyConsumer):
	'''
	Station supply with load derived from the station output.

		'''

	possibleProfileList = {'class': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class EnergyConsumer: \n' + EnergyConsumer.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=StationSupply\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
