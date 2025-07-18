# module = a file containiiiing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

print(help('modules')) # shows all the available modules

import math
print(math.pi) # prints the value of pi from the math module
import math as m # imported under an alias

# all the functions that come within the module can now be used

from math import pi # imports only the pi constant from the math module
from math import sqrt, pow # imports specific functions from the math module

import code # imports the custom module (renamed to avoid conflict)

print(code.nunvrt)
