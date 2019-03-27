#!/usr/bin/env python

def per( n, steps=0, nums=[] ):
	if steps == 0:
		nums = []
	nums.append( n )
	if len( str( n ) ) == 1:
		return steps, nums


	digits = [int(i) for i in str(n)]

	result = 1
	for j in digits:
		result *= j

	steps, nums = per( result, steps+1, nums )
	return steps, nums


if __name__=="__main__":
	assert( per( 277777788888899 )[0] == 11 )
