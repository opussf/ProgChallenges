#!/usr/bin/env lua

function solution( tableIn, shift )
	for lcv=1, shift do
		table.insert( tableIn, 1, table.remove( tableIn ) )
	end
	return tableIn
end

assert( solution( {3, 8, 9, 7, 6}, 1 )[1] == 6 )
assert( solution( {3, 8, 9, 7, 6}, 3 )[1] == 9 )
assert( solution( {3, 8, 9, 7, 6}, 0 )[1] == 3 )