#!/usr/bin/env lua

function factor( inVal, p )
	outVals = {}
	for f = 2, inVal / 2 do
		while (inVal / f) % 1 == 0 do
			outVals[f] = outVals[f] and outVals[f] + 1 or 1
			inVal = inVal / f
		end
		if inVal <= 1 then
			break
		end
	end
	if p then
		for i,v in pairs(outVals) do
			print(i.."^"..v)
		end
	end
	return outVals
end

nums = {455, 11,  1, 3, 11, 1}
dens = { 33, 13, 11, 7,  2, 3}

input = (2^5)*(3^3)

factor(input, true)

maxInstructon = #(nums)

n = input

inst = 1

while inst <= maxInstructon do
	numerator, denominator = nums[inst], dens[inst]
	result = n * numerator / denominator
	if result % 1 == 0 then
		print( n.." * "..numerator.."/"..denominator.." = "..result )
		n = result
		inst = 1
	else
		inst = inst + 1
	end
end

print(n)

factor( n,true )

