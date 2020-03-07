#!/usr/bin/env python

class TilingField( object ):
	""" this abstracts working with a field """
	def __init__( self, x=None, y=None ):
		if x and y and x==int(x) and y==int(y):
			self.setFieldSize( x, y )
	def setFieldSize( self, x, y ):
		self.fieldX = x
		self.fieldY = y
		self.field = ["."] * ( self.fieldX * self.fieldY )
	def getValue( self, x, y ):
		offset = self.__offset( x, y )
		return self.field[offset]
	def setValue( self, x, y, value="." ):
		offset = self.__offset( x, y )
		self.field[offset] = value

	def __offset( self, x, y ):
		""" private function.  return the offset, or raise a ValueError """
		#print( "__offset( %i, %i )" % ( x, y ) )
		if( x >= self.fieldX or x < 0 or y >= self.fieldY or y < 0 ):
			raise( ValueError )
		return( y*self.fieldX + x )

	def __str__( self ):
		return "\n".join( [" ".join( map( lambda x: str(x), self.field[self.fieldX*y:self.fieldX*(y+1)] ) ) for y in xrange(self.fieldY) ] )

if __name__ == "__main__":
	import unittest

	class testTilingField( unittest.TestCase ):
		def setUp( self ):
			self.field = TilingField()
		def tearDown( self ):
			self.field = None
		def test_setFieldFromInit( self ):
			self.field = TilingField( 3, 3 )
			self.assertEquals( self.field.fieldX, 3 )
			self.assertEquals( self.field.fieldY, 3 )
			self.assertIsNotNone( self.field.field )
		def test_setField_oddSize( self ):
			self.field.setFieldSize( 10, 4 )
			self.assertEquals( self.field.fieldX, 10 )
			self.assertEquals( self.field.fieldY, 4 )
		def test_setValue( self ):
			self.field.setFieldSize( 3, 3 )
			self.field.setValue( 2, 2, 1 )
			self.assertEquals( self.field.field[8], 1 )
		def test_getValue( self ):
			self.field.setFieldSize( 5, 5 )
			self.field.field[0] = 1
			self.assertEquals( self.field.getValue( 0, 0 ), 1 )
		def test_getValue_outsideRangeX( self ):
			self.field.setFieldSize( 3, 3 )
			with self.assertRaises( ValueError ):
				self.field.getValue( 2, 3 )

	unittest.main()
