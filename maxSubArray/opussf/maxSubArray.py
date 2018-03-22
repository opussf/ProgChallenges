#!/usr/bin/env python

def solution( listIn ):
	"""
	search an array, find the subArray with the max sum of the elements in order.
	This was the solution I was working towards.
	O = log(n)  ?

	Notes:
	time to write (< 5 minutes)
	code simplicity :  simple
	code comfort    :  high
	code correctness:  high
	gotcha: needed to add the +1 to end....  (should it be range( start+1, len() ) ?)
	bonus : returns the offsets of all the subArrays that give the maxSum
	"""
	values = {}   # capure data in a dict
	for start in range( len( listIn ) ):
		for end in range( start, len( listIn ) ):
			subSum = sum( listIn[start:end+1] )
			try:
				values[subSum].append( [ start, end+1 ] )
			except KeyError:
				values[subSum] = [ [ start, end+1 ] ]
			#print( start, end+1, subSum, listIn[start:end+1] )
	sumKeys = values.keys()
	sumKeys.sort()
	maxValue = sumKeys[-1]
	return( maxValue, values[maxValue] )

def solution_2( listIn ):
	""" an idea was set forth to do this in a single loop
	Not sure if this can be done.

	Notes:
	time to write (Bah! too long, looked it up)
	https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
	code simplicity :  too complex to understand at a single read
	code comfort    :  low - med
	code correctness:  fails for a list with no 0 values
	gotcha: 0?  really?  0?
	bonus : speed, is it worth the not-correct convoluted logic?
	"""
	max_so_far = listIn[0]
	curr_max = listIn[0]
	for i in range( 1, len(listIn) ):
		curr_max = max( listIn[i], curr_max + listIn[i] )
		max_so_far = max( max_so_far, curr_max )

	print "return:", max_so_far
	return( max_so_far )


if __name__=="__main__":
	import unittest

	class testMaxSubarray( unittest.TestCase ):
		def setUp( self ):
			pass
		def test_mixed_maxValue_mine( self ):
			self.assertEquals( solution( [ -1, 0, 2, 3, 5, -20, 10, 11, -20 ] )[0], 21 )
		def test_mixed_offsets_mine( self ):
			self.assertEquals( solution( [ -1, 0, 2, 3, 5, -20, 10, 11, -20 ] )[1], [[6,8]] )
		def test_allNegValues_maxValue_mine( self ):
			self.assertEquals( solution( [ -1, -1, -2, -3, -5, -20, -10, -11, -20 ] )[0], -1 )
		def test_allNegValues_offsets_mine( self ):
			self.assertEquals( solution( [ -1, -1, -2, -3, -5, -20, -10, -11, -20 ] )[1], [ [0,1], [1,2] ] )
		def test_mixed_maxValue_set2( self ):
			self.assertEquals( solution( [ -2, -3, 4, -1, -2, 1, 5, -3 ] )[0], 7 )
		def test_singleItemArray( self ):
			self.assertEquals( solution( [ 42 ] )[0], 42 )

		def test_2_mixed_maxValue( self ):
			self.assertEquals( solution_2( [ -1, 0, 2, 3, 5, -20, 10, 11, -20 ] ), 21 )
		def test_2_allNegValues_maxValue( self ):
			self.assertEquals( solution_2( [ -1, -1, -2, -3, -5, -20, -10, -11, -20 ] ), -1 )
		def test_2_singleItemArray( self ):
			self.assertEquals( solution_2( [ 42 ] ), 42 )




	unittest.main()
