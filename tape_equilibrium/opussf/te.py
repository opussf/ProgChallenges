#!/usr/bin/env python

def s1( arrayIn, split ):
	return abs( sum(arrayIn[:split]) - sum(arrayIn[split:]) )

def solution( arrayIn, split ):
	firstHalf = arrayIn[ : split ]
	secondHalf = arrayIn[ split : ]

	firstHalfSum = sum( firstHalf )
	secondHalfSum = sum( secondHalf )

	diff = firstHalfSum - secondHalfSum

	absDiff = abs( diff )
	return absDiff

if __name__=="__main__":
	import unittest

	class testTapeEquilibrium( unittest.TestCase ):
		def setUp( self ):
			self.testArray = [ 3, 1, 2, 4, 3 ]
		def test01( self ):
			self.assertEquals( solution( self.testArray, 1 ), 7 )
		def test02( self ):
			self.assertEquals( solution( self.testArray, 2 ), 5 )
		def test03( self ):
			self.assertEquals( solution( self.testArray, 3 ), 1 )
		def test04( self ):
			self.assertEquals( solution( self.testArray, 4 ), 7 )

	unittest.main()