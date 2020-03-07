#!/usr/bin/env python

def solution( C, H ):
	z = len(C) / 2
	print z
	out = [ " "*(H-i+z)+((" "*(z+1)).join([ C for j in range(i+1) ]) ) for i in range(H) ]
	return "\n".join( out )

if __name__=="__main__":
	import unittest

	print( solution( "***", 10 ))
	print( solution( "****", 4 ))
	print( solution( "*", 2 ))

	class testTree( unittest.TestCase ):
		def test01( self ):
			out = solution( "*", 2 )
			self.assertEquals( "  *\n * *", out )
		def test02( self ):
			out = solution( "t", 5 )
			self.assertEquals( "    t\n   t t\n  t t t\n t t t t\nt t t t t", out )
		def test03( self ):
			out = solution( "123", 3 )
			self.assertEquals( )

	unittest.main()

"""
   12           -- 2
 12  12         -- 1
12 12 12        -- 0

    123         -- 4 spaces
  123 123       -- 2
123 123 123


         1234            -- 9 spaces    i = 0
      1234  1234         -- 6           i = 1
   1234  1234  1234      -- 3           i = 2
1234  1234  1234  1234   -- 0           i = 3

(len(C) - 1) * i     = ( 4 - 1 ) * 3      3 = H - 1

9 = 3 * 3  -   ( 3 * i )



H

3

"""


