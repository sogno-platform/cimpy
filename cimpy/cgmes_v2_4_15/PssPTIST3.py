from cimpy.cgmes_v2_4_15.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssPTIST3(PowerSystemStabilizerDynamics):
	'''
	PTI Microprocessor-Based Stabilizer type 3.

	:m: (M).  M=2*H.  Typical Value = 5. Default: 
	:tf: Time constant (Tf).  Typical Value = 0.2. Default: 
	:tp: Time constant (Tp).  Typical Value = 0.2. Default: 
	:t1: Time constant (T1).  Typical Value = 0.3. Default: 
	:t2: Time constant (T2).  Typical Value = 1. Default: 
	:t3: Time constant (T3).  Typical Value = 0.2. Default: 
	:t4: Time constant (T4).  Typical Value = 0.05. Default: 
	:k: Gain (K).  Typical Value = 9. Default: 
	:dtf: Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025. Default: 
	:dtc: Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical Value = 0.025. Default: 
	:dtp: Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.0125. Default: 
	:t5: Time constant (T5). Default: 
	:t6: Time constant (T6). Default: 
	:a0: Filter coefficient (A0). Default: 
	:a1: Limiter (Al). Default: 
	:a2: Filter coefficient (A2). Default: 
	:b0: Filter coefficient (B0). Default: 
	:b1: Filter coefficient (B1). Default: 
	:b2: Filter coefficient (B2). Default: 
	:a3: Filter coefficient (A3). Default: 
	:a4: Filter coefficient (A4). Default: 
	:a5: Filter coefficient (A5). Default: 
	:b3: Filter coefficient (B3). Default: 
	:b4: Filter coefficient (B4). Default: 
	:b5: Filter coefficient (B5). Default: 
	:athres: Threshold value above which output averaging will be bypassed (Athres).  Typical Value = 0.005. Default: 
	:dl: Limiter (Dl). Default: 
	:al: Limiter (Al). Default: 
	:lthres: Threshold value (Lthres). Default: 
	:pmin: (Pmin). Default: 
	:isw: Digital/analog output switch (Isw). true = produce analog output false = convert to digital output, using tap selection table. Default: 
	:nav: Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4. Default: 
	:ncl: Number of counts at limit to active limit function (Ncl) (>0). Default: 
	:ncr: Number of counts until reset after limit function is triggered (Ncr). Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'm': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'tp': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						'dtf': [cgmesProfile.DY.value, ],
						'dtc': [cgmesProfile.DY.value, ],
						'dtp': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						'a0': [cgmesProfile.DY.value, ],
						'a1': [cgmesProfile.DY.value, ],
						'a2': [cgmesProfile.DY.value, ],
						'b0': [cgmesProfile.DY.value, ],
						'b1': [cgmesProfile.DY.value, ],
						'b2': [cgmesProfile.DY.value, ],
						'a3': [cgmesProfile.DY.value, ],
						'a4': [cgmesProfile.DY.value, ],
						'a5': [cgmesProfile.DY.value, ],
						'b3': [cgmesProfile.DY.value, ],
						'b4': [cgmesProfile.DY.value, ],
						'b5': [cgmesProfile.DY.value, ],
						'athres': [cgmesProfile.DY.value, ],
						'dl': [cgmesProfile.DY.value, ],
						'al': [cgmesProfile.DY.value, ],
						'lthres': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						'isw': [cgmesProfile.DY.value, ],
						'nav': [cgmesProfile.DY.value, ],
						'ncl': [cgmesProfile.DY.value, ],
						'ncr': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, m = , tf = , tp = , t1 = , t2 = , t3 = , t4 = , k = , dtf = , dtc = , dtp = , t5 = , t6 = , a0 = , a1 = , a2 = , b0 = , b1 = , b2 = , a3 = , a4 = , a5 = , b3 = , b4 = , b5 = , athres = , dl = , al = , lthres = , pmin = , isw = , nav = , ncl = , ncr = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.m = m
		self.tf = tf
		self.tp = tp
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.k = k
		self.dtf = dtf
		self.dtc = dtc
		self.dtp = dtp
		self.t5 = t5
		self.t6 = t6
		self.a0 = a0
		self.a1 = a1
		self.a2 = a2
		self.b0 = b0
		self.b1 = b1
		self.b2 = b2
		self.a3 = a3
		self.a4 = a4
		self.a5 = a5
		self.b3 = b3
		self.b4 = b4
		self.b5 = b5
		self.athres = athres
		self.dl = dl
		self.al = al
		self.lthres = lthres
		self.pmin = pmin
		self.isw = isw
		self.nav = nav
		self.ncl = ncl
		self.ncr = ncr
		
	def __str__(self):
		str = 'class=PssPTIST3\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
