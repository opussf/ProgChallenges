#!/usr/bin/env lua



function factor( inVal, p )
	outVals = {}
	for f = 2, inVal / 2 do
		while (inVal / f) % 1 == 0 do
			outVals[f] = outVals[f] and outVals[f] + 1 or 1
			inVal = inVal / f
		end
	end
	if p then
		for i,v in pairs(outVals) do
			print(i.."^"..v)
		end
	end
	return outVals
end

prog = { 455, 33, 11, 13, 1, 11, 3, 7, 11, 2, 1 ,3 }

input = 72
factor(input, true)

maxInstructon = #(prog)/2

n = input

inst = 1

while inst <= maxInstructon do
	numerator, denominator = prog[inst*2-1], prog[inst*2]
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

