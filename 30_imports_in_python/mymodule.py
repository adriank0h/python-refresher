def divide(dividend, divisor):
    return dividend / divisor

#__name__ will see whihc file u are in. Global variable 
print("mymodule.py:", __name__)

# -- importing from a folder --

import libs.mylib

print("mymodule.py:", __name__)
