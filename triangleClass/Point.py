#!/usr/bin/env python3
class Point( object ):
    pass

if __name__ == "__main__":
    import unittest
    class TestPoint( unittest.TestCase ):
        def setUp( self ):
            self P = Point()
        def tearDown( self ):
            self.P = None
        def testPoint01( self ):
            pass

    unittest.main()