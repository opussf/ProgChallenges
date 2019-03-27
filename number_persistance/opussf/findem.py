#!/usr/bin/env python

import sys, os

sys.path.insert( 1, os.path.join( sys.path[0], '..' ) )

from persistance import *


lowestMax = {}
allNumsBySteps = {}
for vln in xrange( sys.maxint ):
#for vln in xrange( 10000 ):
	steps, nums = per( vln )
	hasSteps = allNumsBySteps.get( steps, None )
	if not hasSteps:
		allNumsBySteps[steps] = []
	allNumsBySteps[steps].append( vln )
	if steps not in lowestMax.keys():
		lowestMax[steps] = vln
		print lowestMax

allKeys = allNumsBySteps.keys()
allKeys.sort()
for k in allKeys:
	print "%3i : %3i" % ( k, len( allNumsBySteps[k] ) )
