#!/usr/bin/env python3
import sys

def BETEncode( strIn ):
	"""Takes a string, returns a string"""
	if not "\003" in strIn:
		s = strIn + "\003"
		table = sorted(s[i:]+s[:i] for i in range(len(s)))
		last_column = [row[-1:] for row in table]
		return "".join(last_column)
	else:
		return none

def BETDecode( strIn ):
	table = [""] * len(strIn)
	for i in range(len(strIn)):
		table = sorted(strIn[i] + table[i] for i in range(len(strIn)))
		#print( table )
	strOut = [row for row in table if row.endswith("\003")][0]
	return strOut.rstrip("\003")

print( BETEncode( "BANANA" ) )
print( BETEncode( "Altanzaya" ) )
print( BETEncode( "Charles" ) )
print( BETEncode( "SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES" ) )
print( BETEncode( open(sys.argv[0],"r").read() ) )

print( BETDecode( BETEncode( open(sys.argv[0],"r").read() ) ) )
#print( BETDecode( "EXEREDSEEND.HREENRRREVHS.TETTT.SEO.FUEHHHI......OEI" ) )