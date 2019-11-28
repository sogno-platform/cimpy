from cimpy.cgmes_v2_4_15.Curve import Curve


class VsCapabilityCurve(Curve):
	'''
	The P-Q capability curve for a voltage source converter, with P on x-axis and Qmin and Qmax on y1-axis and y2-axis.

	:VsConverterDCSides: Capability curve of this converter. Default: "many"
		'''

	cgmesProfile = Curve.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'VsConverterDCSides': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class Curve: \n' + Curve.__doc__ 

	def __init__(self, VsConverterDCSides = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.VsConverterDCSides = VsConverterDCSides
		
	def __str__(self):
		str = 'class=VsCapabilityCurve\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
