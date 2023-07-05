from .IdentifiedObject import IdentifiedObject


class WindPlantReactiveControlIEC(IdentifiedObject):
	'''
	Simplified plant voltage and reactive power control model for use with type 3 and type 4 wind turbine models. Reference: IEC 61400-27-1:2015, Annex D.

	:WindDynamicsLookupTable: The wind dynamics lookup table associated with this voltage and reactive power wind plant model. Default: "list"
	:WindPlantIEC: Wind plant reactive control model associated with this wind plant. Default: None
	:dxrefmax: Maximum positive ramp rate for wind turbine reactive power/voltage reference (<i>dx</i><i><sub>refmax</sub></i>) (&gt; WindPlantReactiveControlIEC.dxrefmin). It is a project-dependent parameter. Default: 0.0
	:dxrefmin: Maximum negative ramp rate for wind turbine reactive power/voltage reference (<i>dx</i><i><sub>refmin</sub></i>) (&lt; WindPlantReactiveControlIEC.dxrefmax). It is a project-dependent parameter. Default: 0.0
	:kiwpx: Plant Q controller integral gain (<i>K</i><i><sub>IWPx</sub></i>). It is a project-dependent parameter. Default: 0.0
	:kiwpxmax: Maximum reactive power/voltage reference from integration (<i>K</i><i><sub>IWPxmax</sub></i>) (&gt; WindPlantReactiveControlIEC.kiwpxmin). It is a project-dependent parameter. Default: 0.0
	:kiwpxmin: Minimum reactive power/voltage reference from integration (<i>K</i><i><sub>IWPxmin</sub></i>) (&lt; WindPlantReactiveControlIEC.kiwpxmax). It is a project-dependent parameter. Default: 0.0
	:kpwpx: Plant Q controller proportional gain (<i>K</i><i><sub>PWPx</sub></i>). It is a project-dependent parameter. Default: 0.0
	:kwpqref: Reactive power reference gain (<i>K</i><i><sub>WPqref</sub></i>). It is a project-dependent parameter. Default: 0.0
	:kwpqu: Plant voltage control droop (<i>K</i><i><sub>WPqu</sub></i>). It is a project-dependent parameter. Default: 0.0
	:tuqfilt: Filter time constant for voltage-dependent reactive power (<i>T</i><i><sub>uqfilt</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
	:twppfiltq: Filter time constant for active power measurement (<i>T</i><i><sub>WPpfiltq</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
	:twpqfiltq: Filter time constant for reactive power measurement (<i>T</i><i><sub>WPqfiltq</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
	:twpufiltq: Filter time constant for voltage measurement (<i>T</i><i><sub>WPufiltq</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
	:txft: Lead time constant in reference value transfer function (<i>T</i><i><sub>xft</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
	:txfv: Lag time constant in reference value transfer function (<i>T</i><i><sub>xfv</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
	:uwpqdip: Voltage threshold for UVRT detection in Q control (<i>u</i><i><sub>WPqdip</sub></i>). It is a project-dependent parameter. Default: 0.0
	:windPlantQcontrolModesType: Reactive power/voltage controller mode (<i>M</i><i><sub>WPqmode</sub></i>). It is a case-dependent parameter. Default: None
	:xrefmax: Maximum <i>x</i><sub>WTref</sub> (<i>q</i><i><sub>WTref</sub></i> or delta<i> u</i><i><sub>WTref</sub></i>) request from the plant controller (<i>x</i><i><sub>refmax</sub></i>) (&gt; WindPlantReactiveControlIEC.xrefmin). It is a case-dependent parameter. Default: 0.0
	:xrefmin: Minimum <i>x</i><i><sub>WTref</sub></i> (<i>q</i><i><sub>WTref</sub></i> or delta <i>u</i><i><sub>WTref</sub></i>) request from the plant controller (<i>x</i><i><sub>refmin</sub></i>) (&lt; WindPlantReactiveControlIEC.xrefmax). It is a project-dependent parameter. Default: 0.0
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.DY.value, ],
						'WindPlantIEC': [cgmesProfile.DY.value, ],
						'dxrefmax': [cgmesProfile.DY.value, ],
						'dxrefmin': [cgmesProfile.DY.value, ],
						'kiwpx': [cgmesProfile.DY.value, ],
						'kiwpxmax': [cgmesProfile.DY.value, ],
						'kiwpxmin': [cgmesProfile.DY.value, ],
						'kpwpx': [cgmesProfile.DY.value, ],
						'kwpqref': [cgmesProfile.DY.value, ],
						'kwpqu': [cgmesProfile.DY.value, ],
						'tuqfilt': [cgmesProfile.DY.value, ],
						'twppfiltq': [cgmesProfile.DY.value, ],
						'twpqfiltq': [cgmesProfile.DY.value, ],
						'twpufiltq': [cgmesProfile.DY.value, ],
						'txft': [cgmesProfile.DY.value, ],
						'txfv': [cgmesProfile.DY.value, ],
						'uwpqdip': [cgmesProfile.DY.value, ],
						'windPlantQcontrolModesType': [cgmesProfile.DY.value, ],
						'xrefmax': [cgmesProfile.DY.value, ],
						'xrefmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindDynamicsLookupTable = "list", WindPlantIEC = None, dxrefmax = 0.0, dxrefmin = 0.0, kiwpx = 0.0, kiwpxmax = 0.0, kiwpxmin = 0.0, kpwpx = 0.0, kwpqref = 0.0, kwpqu = 0.0, tuqfilt = 0, twppfiltq = 0, twpqfiltq = 0, twpufiltq = 0, txft = 0, txfv = 0, uwpqdip = 0.0, windPlantQcontrolModesType = None, xrefmax = 0.0, xrefmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		self.WindPlantIEC = WindPlantIEC
		self.dxrefmax = dxrefmax
		self.dxrefmin = dxrefmin
		self.kiwpx = kiwpx
		self.kiwpxmax = kiwpxmax
		self.kiwpxmin = kiwpxmin
		self.kpwpx = kpwpx
		self.kwpqref = kwpqref
		self.kwpqu = kwpqu
		self.tuqfilt = tuqfilt
		self.twppfiltq = twppfiltq
		self.twpqfiltq = twpqfiltq
		self.twpufiltq = twpufiltq
		self.txft = txft
		self.txfv = txfv
		self.uwpqdip = uwpqdip
		self.windPlantQcontrolModesType = windPlantQcontrolModesType
		self.xrefmax = xrefmax
		self.xrefmin = xrefmin
		
	def __str__(self):
		str = 'class=WindPlantReactiveControlIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
