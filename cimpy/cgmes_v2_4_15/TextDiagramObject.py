from .DiagramObject import DiagramObject


class TextDiagramObject(DiagramObject):
	'''
	A diagram object for placing free-text or text derived from an associated domain object.

	:text: The text that is displayed by this text diagram object. Default: ''
		'''

	cgmesProfile = DiagramObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DL.value, ],
						'text': [cgmesProfile.DL.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DiagramObject: \n' + DiagramObject.__doc__ 

	def __init__(self, text = '',  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.text = text
		
	def __str__(self):
		str = 'class=TextDiagramObject\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
