#!/usr/bin/env python3
### Line
import Point

class Line( object ):
    def __init__( self, point1, point2 ):
        pass

if __name__ == "__main__":
    import unittest
    class TestLine( unittest.TestCase ):
        def setUp( self ):
            self.L = Line( Point.Point( 0, 0 ), Point.Point( 1, 1, ) )
        def tearDown( self ):
            self.L = None
        def testLine01( self ):
            pass

    unittest.main()
