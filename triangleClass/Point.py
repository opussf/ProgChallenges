#!/usr/bin/env python3

class Point( object ):
    def __init__( self, x, y ):
        self.__x = x
        self.__y = y
    @property
    def x( self ):
        return self.__x
    @property
    def y( self ):
        return self.__y
    def complex( self ):
        return complex( self.__x, self.__y )

if __name__ == "__main__":
    import unittest
    class TestPoint( unittest.TestCase ):
        def setUp( self ):
            self.P = Point( 5, 6 )
        def tearDown( self ):
            self.P = None
        def test_Point_getX( self ):
            self.assertEqual( 5, self.P.x )
        def test_Point_getY( self ):
            self.assertEqual( 6, self.P.y )
        def test_Point_cannot_assign_x( self ):
            with self.assertRaises( AttributeError ):
                self.P.x = 10
            self.assertEqual( 5, self.P.x )
        def test_Point_cannot_assign_y( self ):
            with self.assertRaises( AttributeError ):
                self.P.y = 10
            self.assertEqual( 6, self.P.y )
        def test_Point_complex( self ):
            self.assertEqual( 5+6j, self.P.complex() )

    unittest.main()