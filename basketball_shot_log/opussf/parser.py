#!/usr/bin/env python
# parser

import sys, os

sys.path.insert( 1, os.path.join( sys.path[0], '..' ) )

import logGen

import re

log, final = logGen.makeLog()
#################

shotRE = re.compile( "^.*\t\t(.*) made .* (\d+) - (\d+)$" )

playerScores = {}
for player in logGen.players[0]:
	playerScores[player] = 0

score = [0,0]
for line in log.split( "\n" ):
	matched = shotRE.match( line )
	if matched:
		name = matched.group(1)
		home = int( matched.group(2) )
		away = int( matched.group(3) )

		if home > score[0]:
			playerScores[name] += home - score[0]
			score[0] = home


print playerScores

