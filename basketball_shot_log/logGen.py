#!/usr/bin/env python

import random
random.seed( 15364 )

players = [
		( "t1 p1", "t1 p2", "t1 p3", "t1 p4", "t1 p5", "t1 p6", "t1 p7" ),
		( "t2 p1", "t2 p2", "t2 p3", "t2 p4", "t2 p5", "t2 p6", "t2 p7" ),
]

quarterTime = 12 * 60

# 0 = no activity
# 1 = shot - miss
# 2 = shot - made - 2 pt
# 3 = shot - made - 3 pt
# 4 = foul - penality shot
activityList = [0] * 90
for t in range( 1, 5 ):
	while True:
		index = random.randrange( 0, len( activityList ) )
		if activityList[index] == 0:
			activityList[index] = t
			break

def sec2Time( secsIn ):
	# return string of seconds.  MM:SS
	return( "%02i:%02i" % ( secsIn/60, secsIn%60 ) )

def madeMissed( score ):
	if score == 0:
		return "missed"
	return "made"

shotDescritptions = [ [], [],
		[ "%(distanceStr)s jump shot", "layup shot", "dunk shot", "hook shot", "bank shot" ],   # 2 pt
		[ "%(distanceStr)s jump shot" ],  # 3 pt
		[],  # 4 foul shot
]


score = [0,0]
for t in xrange( quarterTime, 0, -1 ):
	activity = activityList[ random.randrange( 0, len( activityList ) ) ]
	if activity != 0:  # something happened
		team = random.randint( 0, 1 )
		player = players[team][ random.randrange( 0, len( players[team] ) ) ]
		shotInfo = []
		if activity == 4:
			shotsMade = random.randint( 0, 2 )
			shotInfo = [ madeMissed( shotsMade ), "penality shots %i of 2" % ( shotsMade, ) ]
			score[team] += shotsMade
		elif activity == 3:
			distanceInfo = { "distanceStr": "%i-foot" % ( random.randint( 22, 47 ) ) }
			shotInfo = [ madeMissed( 3 ),
					shotDescritptions[activity][random.randrange( 0, len( shotDescritptions[activity] ) )] % distanceInfo,
					"3-point shot" ]
			score[team] += 3
		elif activity == 2:  #
			distanceInfo = { "distanceStr": "%i-foot" % ( random.randint( 5, 22 ) ) }
			shotInfo = [ madeMissed( 2 ),
					shotDescritptions[activity][random.randrange( 0, len( shotDescritptions[activity] ) )] % distanceInfo ]
			score[team] += 2
		elif activity == 1:  # shot missed
			shotInfo = [ madeMissed( 0 ), "distance type" ]

		print "%s\t\t%s %s %s" % ( sec2Time( t ), player,
				" ".join( shotInfo ), "%i - %i" % ( score[0], score[1] ) )
