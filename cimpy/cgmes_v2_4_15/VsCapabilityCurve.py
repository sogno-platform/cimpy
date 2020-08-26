from cimpy.output.Curve import Curve


class VsCapabilityCurve(Curve):
	'''
	The P-Q capability curve for a voltage source converter, with P on x-axis and Qmin and Qmax on y1-axis and y2-axis.

	:VsConverterDCSides: Capability curve of this converter. Default: 
		'''

	cgmesProfile = Curve.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'VsConverterDCSides': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Curve: \n' + Curve.__doc__ 

	def __init__(self, VsConverterDCSides = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.VsConverterDCSides = VsConverterDCSides
		
	def __str__(self):
		str = 'class=VsCapabilityCurve\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
