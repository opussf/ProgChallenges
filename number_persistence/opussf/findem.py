#!/usr/bin/env python

import sys, os, time
sys.path.insert( 1, os.path.join( sys.path[0], '..' ) )
from persistence import *
per = per_iterative

from optparse import OptionParser
import json

parser = OptionParser()
parser.add_option( "", "--runtime", action="store", dest="runtime", type="string", default="3600",
		help="how long to run for. 1h, 60m, 3600s, 3600 are all the same." )
parser.add_option( "-i", "--interval", action="store", dest="interval", type="int", default=500000,
		help="how often to report progress." )
parser.add_option( "-m", "--maxValue", action="store", dest="maxValue", type="int", default=sys.maxint-1,
		help="max value to go to." )

(options, args) = parser.parse_args()
jsonFile = "persistence.json"

try:
	storedData = json.load( open( jsonFile, "r" ), parse_int=int )
except:
	storedData = { "startVal": 0, "lowestMax": {}, "allNumsBySteps": {} }

print "Starting at:", storedData["startVal"]

endTime = time.time() + int( options.runtime )   # since this should have unit in it, it needs to be decoded

def storeValues( vln ):
	storedData["startVal"] = vln
	storedData["lowestMax"] = lowestMax
	storedData["allNumsBySteps"] = allNumsBySteps
	json.dump( storedData, open( jsonFile, "w" ) )

lowestMax = dict( [ (int(k), v) for k, v in storedData["lowestMax"].items() ] )
allNumsBySteps = dict( [ (int(k), v) for k, v in storedData["allNumsBySteps"].items() ] )
for vln in xrange( storedData["startVal"] + 1, options.maxValue+1 ):
	steps, nums = per( vln )
	hasSteps = allNumsBySteps.get( steps, None )
	if not hasSteps:
		allNumsBySteps[steps] = 0
	allNumsBySteps[steps] += 1
	if steps not in lowestMax.keys():
		lowestMax[steps] = vln
		print lowestMax
	if vln % options.interval == 0:
		print "%s (%0.2f): %s" % ( vln, vln / sys.maxint * 100, allNumsBySteps )
		storeValues( vln )
	if time.time() >= endTime:
		break
try: vln
except: pass
else:
	storeValues( vln )
print "Ending:", lowestMax
