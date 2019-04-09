#!/usr/bin/env python

import sys, os, time
sys.path.insert( 1, os.path.join( sys.path[0], '..' ) )
from persistence import *
per = per_iterative

import json

class FindEm( object ):
	jsonFile = "persistence.json"
	def __init__( self, options={} ):
		self.options = options
		self.__decodeRuntime()
		self.__loadData()
	def __decodeRuntime( self ):
		""" decode options["runtime"] from a string (with units) to an integer number of seconds """
		runtime = self.options["runtime"]
		multipliers = { " ": 1, "s": 1, "m": 60, "h": 3600, "d": 86400 }
		total, current = 0, 0
		for c in runtime:
			if c in multipliers.keys():
				current *= multipliers[c]
				total += current
				current = 0
			elif c.isdigit():
				current *= 10
				current += int( c )
		total += current
		self.options["runtime"] = total
	def __loadData( self ):
		""" load or init self.storedData """
		try:
			self.storedData = json.load( open( self.jsonFile, "r" ), parse_int=int )
		except:
			self.storedData = { "startVal": 0, "lowestMax": {}, "allNumsBySteps": {} }
		self.lowestMax = dict( [ (int(k),v) for k, v in self.storedData["lowestMax"].items() ] )
		self.allNumsBySteps = dict( [ (int(k), v) for k, v in self.storedData["allNumsBySteps"].items() ] )
	def __storeData( self, vln ):
		""" write the data out """
		self.storedData["startVal"] = vln
		self.storedData["lowestMax"] = self.lowestMax
		self.storedData["allNumsBySteps"] = self.allNumsBySteps
		json.dump( self.storedData, open( self.jsonFile, "w" ) )
	def main( self ):
		""" main method """
		print "Starting at:", self.storedData["startVal"]
		self.endTime = time.time() + int( self.options["runtime"] )
		for vln in xrange( self.storedData["startVal"]+1, self.options["maxValue"]+1 ):
			steps, nums = per( vln )
			hasSteps = self.allNumsBySteps.get( steps, None )
			if not hasSteps:
				self.allNumsBySteps[steps] = 0
			self.allNumsBySteps[steps] += 1
			if steps not in self.lowestMax.keys():
				self.lowestMax[steps] = vln
				print self.lowestMax
			if vln % self.options["interval"] == 0:
				print "%s (%0.2f): %s" % ( vln, vln / sys.maxint * 100, self.allNumsBySteps )
				self.__storeData( vln )
			if time.time() >= self.endTime:
				break
		try: vln    # if the loop does not execute for some reason, this is not set
		except: pass
		else:
			self.__storeData( vln )
		print "Ending:", self.lowestMax

if __name__ == "__main__":
	from optparse import OptionParser

	parser = OptionParser()
	parser.add_option( "-r", "--runtime", action="store", dest="runtime", type="string", default="3600",
			help="how long to run for. 1h, 60m, 3600s, 3600 are all the same." )
	parser.add_option( "-i", "--interval", action="store", dest="interval", type="int", default=500000,
			help="how often to report progress." )
	parser.add_option( "-m", "--maxValue", action="store", dest="maxValue", type="int", default=sys.maxint-1,
			help="max value to go to." )

	(options, args) = parser.parse_args()

	findem = FindEm( options.__dict__ )
	findem.main()
