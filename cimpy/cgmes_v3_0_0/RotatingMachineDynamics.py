from .DynamicsFunctionBlock import DynamicsFunctionBlock


class RotatingMachineDynamics(DynamicsFunctionBlock):
	'''
	Abstract parent class for all synchronous and asynchronous machine standard models.

	:damping: Damping torque coefficient (<i>D</i>) (&gt;= 0).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical value = 0. Default: 0.0
	:inertia: Inertia constant of generator or motor and mechanical load (<i>H</i>) (&gt; 0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical value = 3. Default: 0
	:saturationFactor: Saturation factor at rated terminal voltage (<i>S1</i>) (&gt;= 0).  Not used by simplified model.  Defined by defined by <i>S</i>(<i>E1</i>) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,02. Default: 0.0
	:saturationFactor120: Saturation factor at 120% of rated terminal voltage (<i>S12</i>) (&gt;= RotatingMachineDynamics.saturationFactor). Not used by the simplified model, defined by <i>S</i>(<i>E2</i>) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,12. Default: 0.0
	:statorLeakageReactance: Stator leakage reactance (<i>Xl</i>) (&gt;= 0). Typical value = 0,15. Default: 0.0
	:statorResistance: Stator (armature) resistance (<i>Rs</i>) (&gt;= 0). Typical value = 0,005. Default: 0.0
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'damping': [cgmesProfile.DY.value, ],
						'inertia': [cgmesProfile.DY.value, ],
						'saturationFactor': [cgmesProfile.DY.value, ],
						'saturationFactor120': [cgmesProfile.DY.value, ],
						'statorLeakageReactance': [cgmesProfile.DY.value, ],
						'statorResistance': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, damping = 0.0, inertia = 0, saturationFactor = 0.0, saturationFactor120 = 0.0, statorLeakageReactance = 0.0, statorResistance = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.damping = damping
		self.inertia = inertia
		self.saturationFactor = saturationFactor
		self.saturationFactor120 = saturationFactor120
		self.statorLeakageReactance = statorLeakageReactance
		self.statorResistance = statorResistance
		
	def __str__(self):
		str = 'class=RotatingMachineDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
