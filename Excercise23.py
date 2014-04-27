################################
######### Excercise 23##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

#I am using the following source code to guess and see what each line does to better by understanding about Python
#Code is taken off GITHUB from simplegeo/python-oauth2


#!/usr/bin/env python

#The next two lines import modules from certain libraries required for the program to run
from setuptools import setup, find_packages
import os, re

#Assigning a string to a variable called PKG
PKG='oauth2'

#Different/More advanced version of concatenation
VERSIONFILE = os.path.join('oauth2', '_version.py')

#Assigning a string to a variable called verstr
verstr = "unknown"

#Try to execute the following code if possible
try:
    #Code will try to open the following file defined above
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    #If fails, then do some regular expression assignment
    MVSRE = r"^manual_verstr *= *['\"]([^'\"]*)['\"]"
    mo = re.search(MVSRE, verstrline, re.M)
    #If statement conditionals
    if mo:
        mverstr = mo.group(1)
    else:
        #If file is not found, output an error message
        print "unable to find version in %s" % (VERSIONFILE,)
        raise RuntimeError("if %s.py exists, it must be well-formed" % (VERSIONFILE,))
    AVSRE = r"^auto_build_num *= *['\"]([^'\"]*)['\"]"
    mo = re.search(AVSRE, verstrline, re.M)
    if mo:
        averstr = mo.group(1)
    else:
        averstr = ''
    verstr = '.'.join([mverstr, averstr])

#Looks like information is being added into a list of data ("REF Tuple")
setup(name=PKG,
      version=verstr,
      description="library for OAuth version 1.0",
      author="Joe Stump",
      author_email="joe@simplegeo.com",
      url="http://github.com/simplegeo/python-oauth2",
      packages = find_packages(),
      install_requires = ['httplib2'],
      license = "MIT License",
      keywords="oauth",
      zip_safe = True,
      test_suite="tests",
      tests_require=['coverage', 'mock'])

