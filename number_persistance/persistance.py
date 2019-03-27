#!/usr/bin/env python

def per_recursive( n, steps=0, nums=[] ):
	if steps == 0:
		nums = []
	nums.append( n )
	if len( str( n ) ) == 1:
		return steps, nums


	digits = [int(i) for i in str(n)]

	result = 1
	for j in digits:
		result *= j

	steps, nums = per_recursive( result, steps+1, nums )
	return steps, nums

def per_iterative( n ):
	steps = 0
	nums = []
	while len( str( n ) ) > 1:
		steps += 1
		nums.append( n )
		result = 1
		for j in [ int( i ) for i in str( n ) ]:
			result *= j
		n = result
	return steps, nums

if __name__=="__main__":
	assert( per_recursive( 277777788888899 )[0] == 11 )
	assert( per_iterative( 277777788888899 )[0] == 11 )
