#!/usr/bin/env python3
### Line
import Point

class Line( object ):
    def __init__( self, 

if __name__ == "__main__":
    import unittest
    class TestLine( unittest.TestCase ):
        def setUp( self ):
            self.L = Line()
        def tearDown( self ):
            self.L = None
        def testLine01( self ):
            pass

    unittest.main()
