#!/usr/bin/env python

def solution( n ):
	zeroCount = 0
	oneSeen = False
	zeroCounts = [0]

	while( n > 0 ):
		if( n % 2 == 1 ):
			zeroCounts.append( zeroCount )
			zeroCount = 0
			oneSeen = True
		elif( oneSeen ):
			zeroCount += 1
		n = n >> 1
	return max( zeroCounts )

if __name__=="__main__":
	import unittest

	class testBinaryGap( unittest.TestCase ):
		def setUp( self ):
			pass
		def test01( self ):
			self.assertEquals( solution( 1041 ), 5 )
		def test02( self ):
			self.assertEquals( solution( 1089 ), 5 )
		def test03( self ):
			self.assertEquals( solution( 0 ), 0 )
		def test04( self ):
			self.assertEquals( solution( 20 ), 1 )
		def test05( self ):
			self.assertEquals( solution( 529 ), 4 )
		def test06( self ):
			self.assertEquals( solution( 9 ), 2 )
		def test07( self ):
			self.assertEquals( solution( 8 ), 0 )
		def test08( self ):
			self.assertEquals( solution( 15 ), 0 )
		def test09( self ):
			self.assertEquals( solution( 2147483647 ), 0 )
	unittest.main()
