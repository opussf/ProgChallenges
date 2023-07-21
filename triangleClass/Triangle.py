### Triangle Class from class
class Triangle( object ):
    pass

if __name__ == "__main__":
    import unittest
    class TestTriangle( unittest.TestCase ):
        def setUp( self ):
            self.t = Triangle()
        def tearDown( self ):
            self.t = None
        def test1():
            pass


    unittest.main()