#!/usr/bin/env python

def solution( listIn, shiftVal ):
	outList = listIn[-shiftVal:] + listIn[:-shiftVal]
	return outList

if __name__=="__main__":
	import unittest

	class testCyclicShift( unittest.TestCase ):
		def setUp( self ):
			pass
		def test01( self ):
			self.assertEquals( solution( [ 3, 8, 9, 7, 6 ], 1 ), [ 6, 3, 8, 9, 7 ] )
		def test02( self ):
			self.assertEquals( solution( [ 3, 8, 9, 7, 6 ], 3 ), [ 9, 7, 6, 3, 8 ] )
		def test03( self ):
			self.assertEquals( solution( [ 3, 8, 9, 7, 6 ], 0 ), [ 3, 8, 9, 7, 6 ] )
		def test04( self ):  # Bonus!  it goes 'backwards' too
			self.assertEquals( solution( [ 3, 8, 9, 7, 6 ], -2 ), [ 9, 7, 6, 3, 8 ] )

	unittest.main()
