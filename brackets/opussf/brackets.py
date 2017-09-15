#!/usr/bin/env python

def DoBracketsMatch( stringIn ):
	leftBrackets = [ "{", "(", "[" ]
	rightBrackets = [ "}", ")", "]" ]

	bracketList = []

	for c in stringIn:
		if c in leftBrackets:	# add left brackets
			bracketList.append(c)
			continue
		if c in rightBrackets:  # match right brackets
			rindex = rightBrackets.index(c)
			if bracketList[-1] == leftBrackets[rindex]:  # remove if the last left bracket matches the right bracket
				bracketList.pop()

	return True if len(bracketList) == 0 else False

if __name__=="__main__":
	import unittest

	class testBracketsMatch( unittest.TestCase ):
		def setUp( self ):
			pass
		def test01( self ):
			self.assertTrue( DoBracketsMatch( "{}" ) )
		def test02( self ):
			self.assertTrue( DoBracketsMatch( "()" ) )
		def test03( self ):
			self.assertTrue( DoBracketsMatch( "[]" ) )
		def test04( self ):
			self.assertTrue( DoBracketsMatch( "{([])}" ) )
		def test05( self ):
			self.assertFalse( DoBracketsMatch( "{([})]" ) )
		def test06( self ):
			self.assertTrue( DoBracketsMatch( "function fname( param, param ) {\ncode\nmoar code\n}" ) )
		def test07( self ):
			self.assertFalse( DoBracketsMatch( "function fname( param, () {\ncode\n) }" ) )

	unittest.main()