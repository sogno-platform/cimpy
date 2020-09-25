from .IdentifiedObject import IdentifiedObject


class ValueAliasSet(IdentifiedObject):
	'''
	Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->"Invalid", 1->"Open", 2->"Closed", 3->"Intermediate". Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.

	:Commands: The Commands using the set for translation. Default: "list"
	:Discretes: The Measurements using the set for translation. Default: "list"
	:RaiseLowerCommands: The Commands using the set for translation. Default: "list"
	:Values: The ValueAliasSet having the ValueToAlias mappings. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Commands': [cgmesProfile.EQ.value, ],
						'Discretes': [cgmesProfile.EQ.value, ],
						'RaiseLowerCommands': [cgmesProfile.EQ.value, ],
						'Values': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Commands = "list", Discretes = "list", RaiseLowerCommands = "list", Values = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Commands = Commands
		self.Discretes = Discretes
		self.RaiseLowerCommands = RaiseLowerCommands
		self.Values = Values
		
	def __str__(self):
		str = 'class=ValueAliasSet\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
