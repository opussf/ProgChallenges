#!/usr/bin/env python

def solution( listIn, offset, swapLength ):
	""" reverse only a portion of listIn, starting at offset, and reversing swapLength items
	"""
	# find the slice to reverse
	outList = listIn[offset:offset+swapLength]
	# reverse it
	outList.reverse()
	# reconstruct the list
	outList = listIn[:offset]+outList+listIn[offset+swapLength:]
	# return the list
	return outList

if __name__=="__main__":
	import unittest

	class testCyclicRotation2( unittest.TestCase ):
		def setUp( self ):
			pass
		def test01( self ):
			self.assertEquals( solution( [ 3, 8, 9, 7, 6 ], 1, 3 ), [ 3, 7, 9, 8, 6 ] )
		def test02( self ):
			self.assertEquals( solution( [ 3, 8, 9, 7, 6 ], 0, 3 ), [ 9, 8, 3, 7, 6 ] )
		def test03( self ):
			self.assertEquals( solution( [ 3, 8, 9, 7, 6 ], 0, 5 ), [ 6, 7, 9, 8, 3 ] )
		def test04( self ):  # Bonus!  it goes 'backwards' too
			self.assertEquals( solution( [ 3, 8, 9, 7, 6 ], 1, 4 ), [ 3, 6, 7, 9, 8 ] )
		def test05( self ):
			self.assertEquals( solution( solution( [ 3, 8, 9, 7, 6 ], 1, 2 ), 1, 4 ), [ 3, 6, 7, 8, 9 ] )

	unittest.main()


