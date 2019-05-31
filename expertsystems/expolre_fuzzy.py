import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership functions
quality = ctrl.Antecedent(np.arange(start=0, stop=11, step=1), 'quality')
service = ctrl.Antecedent(np.arange(start=0, stop=11, step=1), 'service')
tip = ctrl.Consequent(np.arange(0, 2, 0.1), 'tip')
rage = ctrl.Consequent(np.arange(0, 2, 0.1), 'rage')

# Auto-membership function population is possible with .automf(3, 5, or 7)
quality.automf(3)
service.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 0.3])
tip['medium'] = fuzz.trimf(tip.universe, [0, 0.3, 1])
tip['high'] = fuzz.trimf(tip.universe, [0.5, 1, 1])

rage['low'] = fuzz.trimf(tip.universe, [0, 0, 0.3])
rage['medium'] = fuzz.trimf(tip.universe, [0, 0.3, 1])
rage['high'] = fuzz.trimf(tip.universe, [0.5, 1, 1])

rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'] & rage['high'])
rule2 = ctrl.Rule(service['average'], tip['medium'] & rage['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'] & rage['low'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# Crunch the numbers
tipping.compute()

print(tipping.output['tip'])
print(tipping.output['rage'])
