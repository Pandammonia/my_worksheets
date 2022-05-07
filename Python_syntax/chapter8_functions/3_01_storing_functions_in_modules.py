## importing entire modules, any function in this module is available using (module_name).(function_name)
# e.g as below pizza.make_pizza.py

import pizza # OR
import pizza as p # gives pizza the alias p, so instead of pizza.make_pizza() we can use p.make_pizza()

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'ham', 'cheese')

#import ALL functions
from pizza import *

#specific functions
from module_name import function_name
from module_name import function_name, function_name1, function_name2

## use "as" to change an imported functions name if it clashes for some reason

from pizza import make_pizza as mp
mp(16, 'pepperoni')

