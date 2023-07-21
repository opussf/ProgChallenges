#!/usr/bin/env python3
### Line
import Point
import math

class Line( object ):
    def __init__( self, point1, point2 ):
        self.point1 = point1
        self.point2 = point2
    @property
    def length( self ):
        return math.sqrt( math.pow( self.point2.x - self.point1.x, 2) + math.pow( self.point2.y - self.point1.y, 2))

if __name__ == "__main__":
    import unittest
    class TestLine( unittest.TestCase ):
        def setUp( self ):
            self.L = Line( Point.Point( 0, 0 ), Point.Point( 1, 1 ) )
        def tearDown( self ):
            self.L = None
        def test_Line_getLength( self ):
            self.assertAlmostEqual( 1.4142135623730951, self.L.length )

    unittest.main()
