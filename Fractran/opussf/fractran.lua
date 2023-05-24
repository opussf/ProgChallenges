#!/usr/bin/env lua

prog = { 455, 33, 11, 13, 1, 11, 3, 7, 11, 2, 1 ,3 }

input = 72

maxInstructon = #(prog)/2

n = input

inst = 1

while inst <= maxInstructon do
	result = n * prog[(inst*2)-1] / prog[(inst*2)]
	print( n.."*"..prog[inst*2-1].."/"..prog[inst*2].."="..result )
	if result % 1 == 0 then
		n = result
		inst = 1
	else
		inst = inst + 1
	end
end

print(n)
