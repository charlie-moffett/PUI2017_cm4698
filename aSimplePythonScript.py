# Author: charlie moffett, NYU CUSP, 2017

# import package that changes python 2 print function
# so that it requires python 3 syntax

from __future__ import print_function

# import package to read line input arguments

import sys

# check how many arguments are passed to python

if not len(sys.argv) == 2:
    print("Invalid number of arguments. Run as: python  aSimplePythonScript.py YourNameHere")
    sys.exit()

# print 'Hello' + YourName + !, which you will
# have passed to python as an argument

print("Hello " + sys.argv[1] + "!")

