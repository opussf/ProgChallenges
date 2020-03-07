#!/usr/bin/env python -OO

import TilingField

class Tiling( object ):
	""" Tiling takes a field size, and finds all of the ways to fit shapes into it """
	def __init__( self, x, y ):
		if x and y and x==int(x) and y==int(y):
			self.field = TilingField.TilingField( x, y )
	def


if __name__ == "__main__":
	import unittest

	class testTiling( unittest.TestCase ):
		def setUp( self ):
			self.tiling = Tiling( 5, 5 )
		def teatDown( self ):
			self.tiling = None
		def test_Instanced( self ):
			self.assertIsNotNone( self.tiling.field )


	unittest.main()