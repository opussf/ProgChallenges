#!/usr/bin/env python

class SIPrefixes( object ):
	def __init__( self ):
		pass

	def display( self, valIn ):
		pass

if __name__=="__main__":
	import unittest

	class testTree( unittest.TestCase ):
		def setUp( self ):
			self.out = SIPrefixes()
		def test_1( self ):
			self.assertEquals( "1", self.out.display(1) )
		def test_10( self ):
			self.assertEquals( "10", self.out.display(10) )
		def test_100( self ):
			self.assertEquals( "100", self.out.display(100) )
		def test_1000( self ):
			self.assertEquals( "1k", self.out.display(1000) )

	unittest.main()