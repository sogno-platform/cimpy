from cimpy.output.IdentifiedObject import IdentifiedObject


class WindPlantFreqPcontrolIEC(IdentifiedObject):
	'''
	Frequency and active power controller model.  Reference: IEC Standard 61400-27-1 Annex E.

	:WindDynamicsLookupTable: The frequency and active power wind plant control model with which this wind dynamics lookup table is associated. Default: 
	:dprefmax: Maximum ramp rate of  request from the plant controller to the wind turbines (). It is project dependent parameter. Default: 
	:dprefmin: Minimum (negative) ramp rate of  request from the plant controller to the wind turbines (). It is project dependent parameter. Default: 
	:kiwpp: Plant P controller integral gain (). It is type dependent parameter. Default: 
	:kpwpp: Plant P controller proportional gain (). It is type dependent parameter. Default: 
	:prefmax: Maximum  request from the plant controller to the wind turbines (). It is type dependent parameter. Default: 
	:prefmin: Minimum  request from the plant controller to the wind turbines (). It is type dependent parameter. Default: 
	:tpft: Lead time constant in reference value transfer function (). It is type dependent parameter. Default: 
	:tpfv: Lag time constant in reference value transfer function (). It is type dependent parameter. Default: 
	:twpffilt: Filter time constant for frequency measurement (). It is type dependent parameter. Default: 
	:twppfilt: Filter time constant for active power measurement (). It is type dependent parameter. Default: 
	:WindPlantIEC: Wind plant model with which this wind plant frequency and active power control is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dprefmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dprefmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kiwpp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kpwpp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'prefmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'prefmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpft': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpfv': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'twpffilt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'twppfilt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindPlantIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindDynamicsLookupTable = , dprefmax = , dprefmin = , kiwpp = , kpwpp = , prefmax = , prefmin = , tpft = , tpfv = , twpffilt = , twppfilt = , WindPlantIEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		self.dprefmax = dprefmax
		self.dprefmin = dprefmin
		self.kiwpp = kiwpp
		self.kpwpp = kpwpp
		self.prefmax = prefmax
		self.prefmin = prefmin
		self.tpft = tpft
		self.tpfv = tpfv
		self.twpffilt = twpffilt
		self.twppfilt = twppfilt
		self.WindPlantIEC = WindPlantIEC
		
	def __str__(self):
		str = 'class=WindPlantFreqPcontrolIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
