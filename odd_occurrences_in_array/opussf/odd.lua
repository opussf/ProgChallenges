#!/usr/bin/env lua

function solution( arrayIn )
	singleValues = {}
	for _, val in pairs( arrayIn ) do
		if( singleValues[val] ) then
			singleValues[val] = nil
			--print( "Found a pair for "..val )
		else
			singleValues[val] = true
			--print( "No pair found yet for "..val )
		end
	end
	unPaired = {}
	for k in pairs( singleValues ) do
		table.insert( unPaired, k )
	end
	if( #unPaired == 1 ) then
		return( unPaired[ 1 ] )
	end
end

assert( solution( { 9, 3, 9, 3, 9, 7, 9 } ) == 7 )
assert( solution( { 1, 2, 3, 1, 2, 3, 4 } ) == 4 )
assert( solution( { 9, 8, 7, 6, 6, 7, 8 } ) == 9 )
