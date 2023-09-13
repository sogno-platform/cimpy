from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovCT1(TurbineGovernorDynamics):
	'''
	General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units. This model can be used to represent a variety of prime movers controlled by PID governors.  It is suitable, for example, for the representation of:  <ul> 	<li>gas turbine and single shaft combined cycle turbines</li> </ul> <ul> 	<li>diesel engines with modern electronic or digital governors  </li> </ul> <ul> 	<li>steam turbines where steam is supplied from a large boiler drum or a large header whose pressure is substantially constant over the period under study</li> 	<li>simple hydro turbines in dam configurations where the water column length is short and water inertia effects are minimal.</li> </ul> Additional information on this model is available in the 2012 IEEE report, <i><u>Dynamic Models for Turbine-Governors in Power System Studies</u></i>, 3.1.2.3 pages 3-4 (GGOV1).

	:mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
	:r: Permanent droop (<i>R</i>).  Typical value = 0,04. Default: 0.0
	:rselect: Feedback signal for droop (<i>Rselect</i>).  Typical value = electricalPower. Default: None
	:tpelec: Electrical power transducer time constant (<i>Tpelec</i>) (&gt; 0).  Typical value = 1. Default: 0
	:maxerr: Maximum value for speed error signal (<i>maxerr</i>) (&gt; GovCT1.minerr).  Typical value = 0,05. Default: 0.0
	:minerr: Minimum value for speed error signal (<i>minerr</i>) (&lt; GovCT1.maxerr).  Typical value = -0,05. Default: 0.0
	:kpgov: Governor proportional gain (<i>Kpgov</i>).  Typical value = 10. Default: 0.0
	:kigov: Governor integral gain (<i>Kigov</i>).  Typical value = 2. Default: 0.0
	:kdgov: Governor derivative gain (<i>Kdgov</i>).  Typical value = 0. Default: 0.0
	:tdgov: Governor derivative controller time constant (<i>Tdgov</i>) (&gt;= 0).  Typical value = 1. Default: 0
	:vmax: Maximum valve position limit (<i>Vmax</i>) (&gt; GovCT1.vmin).  Typical value = 1. Default: 0.0
	:vmin: Minimum valve position limit (<i>Vmin</i>) (&lt; GovCT1.vmax).  Typical value = 0,15. Default: 0.0
	:tact: Actuator time constant (<i>Tact</i>) (&gt;= 0).  Typical value = 0,5. Default: 0
	:kturb: Turbine gain (<i>Kturb</i>) (&gt; 0).  Typical value = 1,5. Default: 0.0
	:wfnl: No load fuel flow (<i>Wfnl</i>).  Typical value = 0,2. Default: 0.0
	:tb: Turbine lag time constant (<i>Tb</i>) (&gt; 0).  Typical value = 0,5. Default: 0
	:tc: Turbine lead time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:wfspd: Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (<i>Wfspd</i>). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical value = true. Default: False
	:teng: Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (<i>Teng</i>) (&gt;= 0).  <i>Teng</i> should be zero in all but special cases where this transport delay is of particular concern.  Typical value = 0. Default: 0
	:tfload: Load-limiter time constant (<i>Tfload</i>) (&gt; 0).  Typical value = 3. Default: 0
	:kpload: Load limiter proportional gain for PI controller (<i>Kpload</i>).  Typical value = 2. Default: 0.0
	:kiload: Load limiter integral gain for PI controller (<i>Kiload</i>).  Typical value = 0,67. Default: 0.0
	:ldref: Load limiter reference value (<i>Ldref</i>).  Typical value = 1. Default: 0.0
	:dm: Speed sensitivity coefficient (<i>Dm</i>).  <i>Dm</i> can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical value = 0. Default: 0.0
	:ropen: Maximum valve opening rate (<i>Ropen</i>).  Unit = PU / s.  Typical value = 0.10. Default: 0.0
	:rclose: Minimum valve closing rate (<i>Rclose</i>).  Unit = PU / s.  Typical value = -0,1. Default: 0.0
	:kimw: Power controller (reset) gain (<i>Kimw</i>).  The default value of 0,01 corresponds to a reset time of 100 s.  A value of 0,001 corresponds to a relatively slow-acting load controller.  Typical value = 0,01. Default: 0.0
	:aset: Acceleration limiter setpoint (<i>Aset</i>).  Unit = PU / s.  Typical value = 0,01. Default: 0.0
	:ka: Acceleration limiter gain (<i>Ka</i>).  Typical value = 10. Default: 0.0
	:ta: Acceleration limiter time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,1. Default: 0
	:db: Speed governor deadband in PU speed (<i>db</i>).  In the majority of applications, it is recommended that this value be set to zero.  Typical value = 0. Default: 0.0
	:tsa: Temperature detection lead time constant (<i>Tsa</i>) (&gt;= 0).  Typical value = 4. Default: 0
	:tsb: Temperature detection lag time constant (<i>Tsb</i>) (&gt;= 0).  Typical value = 5. Default: 0
	:rup: Maximum rate of load limit increase (<i>Rup</i>).  Typical value = 99. Default: 0.0
	:rdown: Maximum rate of load limit decrease (<i>Rdown</i>).  Typical value = -99. Default: 0.0
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

	def __init__(self, mwbase = 0.0, r = 0.0, rselect = None, tpelec = 0, maxerr = 0.0, minerr = 0.0, kpgov = 0.0, kigov = 0.0, kdgov = 0.0, tdgov = 0, vmax = 0.0, vmin = 0.0, tact = 0, kturb = 0.0, wfnl = 0.0, tb = 0, tc = 0, wfspd = False, teng = 0, tfload = 0, kpload = 0.0, kiload = 0.0, ldref = 0.0, dm = 0.0, ropen = 0.0, rclose = 0.0, kimw = 0.0, aset = 0.0, ka = 0.0, ta = 0, db = 0.0, tsa = 0, tsb = 0, rup = 0.0, rdown = 0.0,  *args, **kw_args):
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
