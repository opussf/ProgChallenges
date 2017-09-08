#!/usr/bin/env lua

function solution( n )
	-- return longest binary gap or 0

	-- test for integer
	if( n ~= math.floor( n ) ) then
		return 0
	end
	zeroCount = 0
	zeroCountMax = 0
	oneSeen = false
	while n > 0 do
		bit = n % 2
		if( bit == 1 ) then
			zeroCountMax = math.max( zeroCountMax, zeroCount )
			zeroCount = 0
			oneSeen = true
		elseif( oneSeen ) then
			zeroCount = zeroCount + 1
		end
		--print( bit, zeroCount, zeroCountMax )

		n = math.floor( n / 2 ) -- integer div
	end
	return zeroCountMax
	--if( zeroCountMax > 0 ) then return zeroCountMax; end
end


assert( solution( 1041 ) == 5 )
assert( solution( 1089 ) == 5 )
assert( solution( 0 ) == 0 )
assert( solution( 20 ) == 1 )
assert( solution( 529 ) == 4 )
assert( solution( 9 ) == 2 )
assert( solution( 8 ) == 0 )
assert( solution( 15 ) == 0 )
assert( solution( 5.6 ) == 0 )
assert( solution( 2147483647 ) == 0 )
