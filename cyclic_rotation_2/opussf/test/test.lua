#!/usr/bin/env lua

require "wowTest"

test.outFileName = "testOut.xml"

package.path = "../?.lua;'" .. package.path
require "cr2"

function test.before()
	test.table = { 3, 8, 9, 7, 6 }
end
function test.after()
end

function test.test01()
	--test.testTable = { 3, 8, 9, 7, 6 }
	outTable = solution( test.table, 1, 3 )
	assertEquals( 3, outTable[1] )
	assertEquals( 7, outTable[2] )
	assertEquals( 9, outTable[3] )
	assertEquals( 8, outTable[4] )
	assertEquals( 6, outTable[5] )
end
function test.test02()
	outTable = solution( test.table, 0, 3 )
	assertEquals( 9, outTable[1] )
	assertEquals( 8, outTable[2] )
	assertEquals( 3, outTable[3] )
	assertEquals( 7, outTable[4] )
	assertEquals( 6, outTable[5] )
end
function test.test03()
	outTable = solution( test.table, 0, 5 )
	assertEquals( 6, outTable[1] )
	assertEquals( 7, outTable[2] )
	assertEquals( 9, outTable[3] )
	assertEquals( 8, outTable[4] )
	assertEquals( 3, outTable[5] )
end
function test.test04()
	outTable = solution( test.table, 1, 4 )
	assertEquals( 3, outTable[1] )
	assertEquals( 6, outTable[2] )
	assertEquals( 7, outTable[3] )
	assertEquals( 9, outTable[4] )
	assertEquals( 8, outTable[5] )
end
function test.test05()
	outTable = solution( test.table, 1, 2 )
	outTable = solution( outTable, 1, 4 )
	assertEquals( 3, outTable[1] )
	assertEquals( 6, outTable[2] )
	assertEquals( 7, outTable[3] )
	assertEquals( 8, outTable[4] )
	assertEquals( 9, outTable[5] )
end

test.run()
