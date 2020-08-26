from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovCT1(TurbineGovernorDynamics):
	'''
	General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units. This model can be used to represent a variety of prime movers controlled by PID governors.  It is suitable, for example, for representation of     Additional information on this model is available in the 2012 IEEE report, , section 3.1.2.3 page 3-4 (GGOV1).

	:mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 
	:r: Permanent droop (R).  Typical Value = 0.04. Default: 
	:rselect: Feedback signal for droop (Rselect).  Typical Value = electricalPower. Default: 
	:tpelec: Electrical power transducer time constant (Tpelec) (>0).  Typical Value = 1. Default: 
	:maxerr: Maximum value for speed error signal (maxerr).  Typical Value = 0.05. Default: 
	:minerr: Minimum value for speed error signal (minerr).  Typical Value = -0.05. Default: 
	:kpgov: Governor proportional gain (Kpgov).  Typical Value = 10. Default: 
	:kigov: Governor integral gain (Kigov).  Typical Value = 2. Default: 
	:kdgov: Governor derivative gain (Kdgov).  Typical Value = 0. Default: 
	:tdgov: Governor derivative controller time constant (Tdgov).  Typical Value = 1. Default: 
	:vmax: Maximum valve position limit (Vmax).  Typical Value = 1. Default: 
	:vmin: Minimum valve position limit (Vmin).  Typical Value = 0.15. Default: 
	:tact: Actuator time constant (Tact).  Typical Value = 0.5. Default: 
	:kturb: Turbine gain (Kturb) (>0).  Typical Value = 1.5. Default: 
	:wfnl: No load fuel flow (Wfnl).  Typical Value = 0.2. Default: 
	:tb: Turbine lag time constant (Tb) (>0).  Typical Value = 0.5. Default: 
	:tc: Turbine lead time constant (Tc).  Typical Value = 0. Default: 
	:wfspd: Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical Value = true. Default: 
	:teng: Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical Value = 0. Default: 
	:tfload: Load Limiter time constant (Tfload) (>0).  Typical Value = 3. Default: 
	:kpload: Load limiter proportional gain for PI controller (Kpload).  Typical Value = 2. Default: 
	:kiload: Load limiter integral gain for PI controller (Kiload).  Typical Value = 0.67. Default: 
	:ldref: Load limiter reference value (Ldref).  Typical Value = 1. Default: 
	:dm: Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical Value = 0. Default: 
	:ropen: Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 0.10. Default: 
	:rclose: Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -0.1. Default: 
	:kimw: Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0.01. Default: 
	:aset: Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 0.01. Default: 
	:ka: Acceleration limiter gain (Ka).  Typical Value = 10. Default: 
	:ta: Acceleration limiter time constant (Ta) (>0).  Typical Value = 0.1. Default: 
	:db: Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this value be set to zero.  Typical Value = 0. Default: 
	:tsa: Temperature detection lead time constant (Tsa).  Typical Value = 4. Default: 
	:tsb: Temperature detection lag time constant (Tsb).  Typical Value = 5. Default: 
	:rup: Maximum rate of load limit increase (Rup).  Typical Value = 99. Default: 
	:rdown: Maximum rate of load limit decrease (Rdown).  Typical Value = -99. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'r': [cgmesProfile.DY.value, ],
						'rselect': [cgmesProfile.DY.value, ],
						'tpelec': [cgmesProfile.DY.value, ],
						'maxerr': [cgmesProfile.DY.value, ],
						'minerr': [cgmesProfile.DY.value, ],
						'kpgov': [cgmesProfile.DY.value, ],
						'kigov': [cgmesProfile.DY.value, ],
						'kdgov': [cgmesProfile.DY.value, ],
						'tdgov': [cgmesProfile.DY.value, ],
						'vmax': [cgmesProfile.DY.value, ],
						'vmin': [cgmesProfile.DY.value, ],
						'tact': [cgmesProfile.DY.value, ],
						'kturb': [cgmesProfile.DY.value, ],
						'wfnl': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'wfspd': [cgmesProfile.DY.value, ],
						'teng': [cgmesProfile.DY.value, ],
						'tfload': [cgmesProfile.DY.value, ],
						'kpload': [cgmesProfile.DY.value, ],
						'kiload': [cgmesProfile.DY.value, ],
						'ldref': [cgmesProfile.DY.value, ],
						'dm': [cgmesProfile.DY.value, ],
						'ropen': [cgmesProfile.DY.value, ],
						'rclose': [cgmesProfile.DY.value, ],
						'kimw': [cgmesProfile.DY.value, ],
						'aset': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'db': [cgmesProfile.DY.value, ],
						'tsa': [cgmesProfile.DY.value, ],
						'tsb': [cgmesProfile.DY.value, ],
						'rup': [cgmesProfile.DY.value, ],
						'rdown': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , r = , rselect = , tpelec = , maxerr = , minerr = , kpgov = , kigov = , kdgov = , tdgov = , vmax = , vmin = , tact = , kturb = , wfnl = , tb = , tc = , wfspd = , teng = , tfload = , kpload = , kiload = , ldref = , dm = , ropen = , rclose = , kimw = , aset = , ka = , ta = , db = , tsa = , tsb = , rup = , rdown = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.r = r
		self.rselect = rselect
		self.tpelec = tpelec
		self.maxerr = maxerr
		self.minerr = minerr
		self.kpgov = kpgov
		self.kigov = kigov
		self.kdgov = kdgov
		self.tdgov = tdgov
		self.vmax = vmax
		self.vmin = vmin
		self.tact = tact
		self.kturb = kturb
		self.wfnl = wfnl
		self.tb = tb
		self.tc = tc
		self.wfspd = wfspd
		self.teng = teng
		self.tfload = tfload
		self.kpload = kpload
		self.kiload = kiload
		self.ldref = ldref
		self.dm = dm
		self.ropen = ropen
		self.rclose = rclose
		self.kimw = kimw
		self.aset = aset
		self.ka = ka
		self.ta = ta
		self.db = db
		self.tsa = tsa
		self.tsb = tsb
		self.rup = rup
		self.rdown = rdown
		
	def __str__(self):
		str = 'class=GovCT1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
