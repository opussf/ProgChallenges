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

def BracketTest( stringIn ):
	""" Determine how many of what brackets are needed to balance the string
		Return a dictionary of needed brackets
	"""
	print( "BracketTest( \"%s\" )" % ( stringIn, ) )
	leftBrackets = [ "{", "(", "[" ]
	rightBrackets = [ "}", ")", "]" ]

	bracketCount = {}
	for i in range( len( leftBrackets ) ):
		bracketCount[leftBrackets[i]] = 0
		bracketCount[rightBrackets[i]] = 0
	bracketNeeds = bracketCount.copy()

	for c in stringIn:
		if c in leftBrackets:
			bracketCount[c] = bracketCount[c] + 1
		elif c in rightBrackets:
			bracketCount[c] = bracketCount[c] + 1
	#print bracketCount

	for i in range( len( leftBrackets ) ):
		leftBracket = leftBrackets[i]
		rightBracket = rightBrackets[i]

		leftCount = bracketCount[leftBracket]
		rightCount = bracketCount[rightBracket]
		if bracketCount[leftBracket] <= bracketCount[rightBracket]:
			bracketCount[rightBracket] -= bracketCount[leftBracket]
			bracketCount[leftBracket] -= bracketCount[leftBracket]
		elif bracketCount[rightBracket] < bracketCount[leftBracket]:
			bracketCount[leftBracket] -= bracketCount[rightBracket]
			bracketCount[rightBracket] -= bracketCount[rightBracket]
		bracketNeeds[leftBracket] = bracketCount[rightBracket]
		bracketNeeds[rightBracket] = bracketCount[leftBracket]

	print( bracketCount )

	print( bracketNeeds )

	return bracketNeeds

	#return bracketBalanceOut

if __name__=="__main__":
	import unittest

	class testBracketsBalance( unittest.TestCase ):
		def setUp( self ):
			pass
		def test01( self ):
			self.assertEquals( 0, BracketTest( "()" )["("] )
		def test02( self ):
			self.assertEquals( 1, BracketTest( "(" )[")"] )
		def test03( self ):
			self.assertEquals( 1, BracketTest( ")" )["("] )
		def test04( self ):
			self.assertEquals( 2, BracketTest( "( ( ( )" )[")"] )
		def test05( self ):
			self.assertEquals( 0, BracketTest( ")(" )["("] )

	unittest.main()