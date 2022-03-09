import test_package.module_a as a
import test_package.module_b as b
from test_package import *

print(a.variable_a)
print(b.variable_b)
print(module_a.variable_a)
print(module_b.variable_b)