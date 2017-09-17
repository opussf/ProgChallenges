#!/usr/bin/env lua

function solution( tableIn, offset, swapLength )
	newTable = {}

	-- copy non-reversed
	for lcv = 1, offset do  -- offset = 0 == no initial data
		table.insert( newTable, tableIn[lcv] )
	end
	-- copy reversed section
	for lcv = offset+swapLength, offset+1, -1 do -- offset+1 to go to 1, not 0.
		table.insert( newTable, tableIn[lcv] )
	end
	-- copy non-reversed
	for lcv = offset+swapLength+1, #tableIn do
		table.insert( newTable, tableIn[lcv] )
	end
--[[
	for lcv=1, #newTable do
		print( string.format("%02i: %i", lcv, newTable[lcv] ) )
	end
]]
	return newTable
end
