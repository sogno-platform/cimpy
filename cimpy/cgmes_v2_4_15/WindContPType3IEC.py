from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class WindContPType3IEC(IdentifiedObject):
	'''
	P control model Type 3.  Reference: IEC Standard 61400-27-1 Section 6.6.5.3.

	:dpmax: Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 
	:dtrisemaxlvrt: Limitation of torque rise rate during LVRT for S (d). It is project dependent parameter. Default: 
	:kdtd: Gain for active drive train damping (). It is type dependent parameter. Default: 
	:kip: PI controller integration parameter (). It is type dependent parameter. Default: 
	:kpp: PI controller proportional gain (). It is type dependent parameter. Default: 
	:mplvrt: Enable LVRT power control mode (M true = 1: voltage control false = 0: reactive power control.  It is project dependent parameter. Default: 
	:omegaoffset: Offset to reference value that limits controller action during rotor speed changes (omega). It is case dependent parameter. Default: 
	:pdtdmax: Maximum active drive train damping power (). It is type dependent parameter. Default: 
	:rramp: Ramp limitation of torque, required in some grid codes (). It is project dependent parameter. Default: 
	:tdvs: Timedelay after deep voltage sags (T). It is project dependent parameter. Default: 
	:temin: Minimum electrical generator torque (). It is type dependent parameter. Default: 
	:tomegafilt: Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 
	:tpfilt: Filter time constant for power measurement (). It is type dependent parameter. Default: 
	:tpord: Time constant in power order lag (). It is type dependent parameter. Default: 
	:tufilt: Filter time constant for voltage measurement (). It is type dependent parameter. Default: 
	:tuscale: Voltage scaling factor of reset-torque (T). It is project dependent parameter. Default: 
	:twref: Time constant in speed reference filter (). It is type dependent parameter. Default: 
	:udvs: Voltage limit for hold LVRT status after deep voltage sags (). It is project dependent parameter. Default: 
	:updip: Voltage dip threshold for P-control ().  Part of turbine control, often different (e.g 0.8) from converter thresholds. It is project dependent parameter. Default: 
	:wdtd: Active drive train damping frequency (omega). It can be calculated from two mass model parameters. It is type dependent parameter. Default: 
	:zeta: Coefficient for active drive train damping (zeta). It is type dependent parameter. Default: 
	:WindGenTurbineType3IEC: Wind turbine type 3 model with which this Wind control P type 3 model is associated. Default: 
	:WindDynamicsLookupTable: The P control type 3 model with which this wind dynamics lookup table is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'dpmax': [cgmesProfile.DY.value, ],
						'dtrisemaxlvrt': [cgmesProfile.DY.value, ],
						'kdtd': [cgmesProfile.DY.value, ],
						'kip': [cgmesProfile.DY.value, ],
						'kpp': [cgmesProfile.DY.value, ],
						'mplvrt': [cgmesProfile.DY.value, ],
						'omegaoffset': [cgmesProfile.DY.value, ],
						'pdtdmax': [cgmesProfile.DY.value, ],
						'rramp': [cgmesProfile.DY.value, ],
						'tdvs': [cgmesProfile.DY.value, ],
						'temin': [cgmesProfile.DY.value, ],
						'tomegafilt': [cgmesProfile.DY.value, ],
						'tpfilt': [cgmesProfile.DY.value, ],
						'tpord': [cgmesProfile.DY.value, ],
						'tufilt': [cgmesProfile.DY.value, ],
						'tuscale': [cgmesProfile.DY.value, ],
						'twref': [cgmesProfile.DY.value, ],
						'udvs': [cgmesProfile.DY.value, ],
						'updip': [cgmesProfile.DY.value, ],
						'wdtd': [cgmesProfile.DY.value, ],
						'zeta': [cgmesProfile.DY.value, ],
						'WindGenTurbineType3IEC': [cgmesProfile.DY.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, dpmax = , dtrisemaxlvrt = , kdtd = , kip = , kpp = , mplvrt = , omegaoffset = , pdtdmax = , rramp = , tdvs = , temin = , tomegafilt = , tpfilt = , tpord = , tufilt = , tuscale = , twref = , udvs = , updip = , wdtd = , zeta = , WindGenTurbineType3IEC = , WindDynamicsLookupTable = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.dpmax = dpmax
		self.dtrisemaxlvrt = dtrisemaxlvrt
		self.kdtd = kdtd
		self.kip = kip
		self.kpp = kpp
		self.mplvrt = mplvrt
		self.omegaoffset = omegaoffset
		self.pdtdmax = pdtdmax
		self.rramp = rramp
		self.tdvs = tdvs
		self.temin = temin
		self.tomegafilt = tomegafilt
		self.tpfilt = tpfilt
		self.tpord = tpord
		self.tufilt = tufilt
		self.tuscale = tuscale
		self.twref = twref
		self.udvs = udvs
		self.updip = updip
		self.wdtd = wdtd
		self.zeta = zeta
		self.WindGenTurbineType3IEC = WindGenTurbineType3IEC
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		
	def __str__(self):
		str = 'class=WindContPType3IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
