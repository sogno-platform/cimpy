from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class LoadMotor(IdentifiedObject):
	'''
	Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as "induction motor load".  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  If  = 0. or  = , or  = 0.,  only one cage is represented. Magnetic saturation is not modelled. Either a "one-cage" or "two-cage" model of the induction machine can be modelled. Magnetic saturation is not modelled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.  This model treats a fraction of the constant power part of a load as a motor. During initialisation, the initial power drawn by the motor is set equal to  times the constant  part of the static load.  The remainder of the load is left as static load.  The reactive power demand of the motor is calculated during initialisation as a function of voltage at the load bus. This reactive power demand may be less than or greater than the constant  component of the load.  If the motor's reactive demand is greater than the constant  component of the load, the model inserts a shunt capacitor at the terminal of the motor to bring its reactive demand down to equal the constant  reactive load.   If a motor model and a static load model are both present for a load, the motor  is assumed to be subtracted from the power flow constant  load before the static load model is applied.  The remainder of the load, if any, is then represented by the static load model.

	:LoadAggregate: Aggregate load to which this aggregate motor (dynamic) load belongs. Default: None
	:pfrac: Fraction of constant-power load to be represented by this motor model (Pfrac) (>=0.0 and <=1.0).  Typical Value = 0.3. Default: 0.0
	:lfac: Loading factor - ratio of initial P to motor MVA base (Lfac).  Typical Value = 0.8. Default: 0.0
	:ls: Synchronous reactance (Ls).  Typical Value = 3.2. Default: 0.0
	:lp: Transient reactance (Lp).  Typical Value = 0.15. Default: 0.0
	:lpp: Subtransient reactance (Lpp).  Typical Value = 0.15. Default: 0.0
	:ra: Stator resistance (Ra).  Typical Value = 0. Default: 0.0
	:tpo: Transient rotor time constant (Tpo) (not=0).  Typical Value = 1. Default: 0.0
	:tppo: Subtransient rotor time constant (Tppo).  Typical Value = 0.02. Default: 0.0
	:h: Inertia constant (H) (not=0).  Typical Value = 0.4. Default: 0.0
	:d: Damping factor (D).  Unit = delta P/delta speed.  Typical Value = 2. Default: 0.0
	:vt: Voltage threshold for tripping (Vt).  Typical Value = 0.7. Default: 0.0
	:tv: Voltage trip pickup time (Tv).  Typical Value = 0.1. Default: 0.0
	:tbkr: Circuit breaker operating time (Tbkr).  Typical Value = 0.08. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'LoadAggregate': [cgmesProfile.DY.value, ],
						'pfrac': [cgmesProfile.DY.value, ],
						'lfac': [cgmesProfile.DY.value, ],
						'ls': [cgmesProfile.DY.value, ],
						'lp': [cgmesProfile.DY.value, ],
						'lpp': [cgmesProfile.DY.value, ],
						'ra': [cgmesProfile.DY.value, ],
						'tpo': [cgmesProfile.DY.value, ],
						'tppo': [cgmesProfile.DY.value, ],
						'h': [cgmesProfile.DY.value, ],
						'd': [cgmesProfile.DY.value, ],
						'vt': [cgmesProfile.DY.value, ],
						'tv': [cgmesProfile.DY.value, ],
						'tbkr': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, LoadAggregate = None, pfrac = 0.0, lfac = 0.0, ls = 0.0, lp = 0.0, lpp = 0.0, ra = 0.0, tpo = 0.0, tppo = 0.0, h = 0.0, d = 0.0, vt = 0.0, tv = 0.0, tbkr = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LoadAggregate = LoadAggregate
		self.pfrac = pfrac
		self.lfac = lfac
		self.ls = ls
		self.lp = lp
		self.lpp = lpp
		self.ra = ra
		self.tpo = tpo
		self.tppo = tppo
		self.h = h
		self.d = d
		self.vt = vt
		self.tv = tv
		self.tbkr = tbkr
		
	def __str__(self):
		str = 'class=LoadMotor\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
