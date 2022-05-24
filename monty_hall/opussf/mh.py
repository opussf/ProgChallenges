#!/usr/bin/env python

import random

class MontyHall( object ):
	prize = 1
	choosen = 2
	opened = 4
	removed = 8

	def __init__( self, switch=False ):
		random.seed()
		self.actions = []
		self.switch = switch

	def __setup( self ):
		self.doors = [0,0,0]  # bit fields, 1 = prize, 2 = choosen, 4 = opened, 8 = removed
		door = random.randint(0,2)
		self.doors[door] = 1
		self.actions.append(door+1)
		print( self.doors )

	def __chooseDoor( self ):
		canChoose = map( lambda x: False if x & self.opened \
										 or x & self.removed \
										 or (self.switch and not ( x & self.choosen )) \
										 else True, self.doors )
		guessing = True
		while guessing:
			door = random.randint(0,2)
			if canChoose[door]:
				self.doors[door] = self.doors[door] | self.choosen
				guessing = False
		self.actions.append(door+1)
		print( canChoose )
		print( self.doors )



	def __revealDoor( self ):
		pass

	def run( self, iterations ):
		for i in xrange( iterations ):
			self.__setup()
			self.__chooseDoor()
			self.__revealDoor()
			self.__chooseDoor()
			self.__revealDoor()

	def __str__( self ):
		out = []
		return "Actions: %s" % (self.actions)
		#return "\n".join(map(str,self.actions))


if __name__ == "__main__":
	mh = MontyHall( True )
	#mh.run(10000000)
	mh.run(1)
	print( mh )
