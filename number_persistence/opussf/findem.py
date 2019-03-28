#!/usr/bin/env python

import sys, os

sys.path.insert( 1, os.path.join( sys.path[0], '..' ) )

from persistence import *
per = per_iterative

lowestMax = {}
allNumsBySteps = {}
for vln in xrange( sys.maxint ):
#for vln in xrange( 10000 ):
	steps, nums = per( vln )
	hasSteps = allNumsBySteps.get( steps, None )
	if not hasSteps:
		allNumsBySteps[steps] = 0
	allNumsBySteps[steps] += 1
	if steps not in lowestMax.keys():
		lowestMax[steps] = vln
		print lowestMax
	if vln % 500000 == 0:
		print "Counts: ", allNumsBySteps

allKeys = allNumsBySteps.keys()
allKeys.sort()
for k in allKeys:
	print "%3i : %3i" % ( k, len( allNumsBySteps[k] ) )
