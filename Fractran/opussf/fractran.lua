#!/usr/bin/env lua

function factor( inVal, p )
	if p then print(inVal..">") end
	outVals = {}
	for f = 2, inVal do
		while (inVal / f) % 1 == 0 do
			outVals[f] = outVals[f] and outVals[f] + 1 or 1
			inVal = inVal / f
		end
		if inVal <= 1 then
			break
		end
	end
	if p then
		printFactors( outVals )
	end
	return outVals
end

function printFactors( t )
	for f,p in pairs( t ) do
		io.write(f.."^"..p.." * ")
	end
	print()
end

nums = {455, 11,  1, 3, 11, 1}
dens = { 33, 13, 11, 7,  2, 3}

input = (2^5)*(3^5)

factor(input, true)

maxInstructon = #(nums)

for i,_ in ipairs( nums ) do
	nums[i] = factor(nums[i])
	dens[i] = factor(dens[i])
end

n = input
n = factor( n )

inst = 1
while inst <= maxInstructon do
	numerator, denominator = nums[inst], dens[inst]
	useThis = true
	for f, p in pairs( denominator ) do
		if not n[f] or n[f]<p then
			useThis = false
		end
	end
	if useThis then
		-- Subtract
		for f,p in pairs( denominator ) do
			n[f] = n[f] - p
			if n[f] == 0 then n[f] = nil end
		end
		-- Add
		for f,p in pairs( numerator ) do
			n[f] = n[f] and n[f] + p or p
		end
		inst = 1
	else
		inst = inst + 1
	end
end

r = 1
for i,p in pairs( n ) do
	print( i.."^"..p )
	r = r * ( i ^ p )
end

print( r )
