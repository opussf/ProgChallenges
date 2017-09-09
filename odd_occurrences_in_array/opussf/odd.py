#!/usr/bin/env python

def solution( arrayIn ):
	singleValues = {}
	for val in arrayIn:
		try:
			seenBefore = singleValues[val]
			del singleValues[val]
			#print( "Found a pair for %i" % (val,) )
		except KeyError:
			singleValues[val] = True
			#print( "No pair found yet for %i" % (val,) )

	unPaired = singleValues.keys()
	if( len( unPaired ) == 1 ):
		return unPaired[0]
	return 0

if __name__=="__main__":
	import unittest

	class testOddOccurrences( unittest.TestCase ):
		def setUp( self ):
			pass
		def test01( self ):
			testArray = [ 9, 3, 9, 3, 9, 7, 9 ]
			self.assertEquals( solution( testArray ), 7 )
		def test02( self ):
			testArray = [ 1, 2, 3, 1, 2, 3, 4 ]
			self.assertEquals( solution( testArray ), 4 )
		def test03( self ):
			testArray = [ 9, 8, 7, 6, 6, 7, 8 ]
			self.assertEquals( solution( testArray ), 9 )

	unittest.main()