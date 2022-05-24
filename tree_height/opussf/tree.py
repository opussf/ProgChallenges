#!/usr/bin/env python

def solution( C, H ):
	out = [ " "*(H-i-1)+(" ".join([ C for j in range(i+1) ]) ) for i in range(H) ]
	return "\n".join( out )

if __name__=="__main__":
	import unittest

	print( solution( "***", 10 ))

	class testTree( unittest.TestCase ):
		def test01( self ):
			out = solution( "*", 2 )
			self.assertEquals( " *\n* *", out )
		def test02( self ):
			out = solution( "t", 5 )
			self.assertEquals( "    t\n   t t\n  t t t\n t t t t\nt t t t t", out )

	unittest.main()

