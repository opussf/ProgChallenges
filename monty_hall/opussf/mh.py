#!/usr/bin/env python

import random

class MontyHall( object ):
	prize = 1
	choosen = 2
	opened = 4
	removed = 8

	def __init__( self, switch=False, randomRemoval=False ):
		random.seed()
		self.actions = []
		self.switch = switch
		self.randomRemoval = randomRemoval

	def __setup( self ):
		self.doors = [0,0,0]  # bit fields, 1 = prize, 2 = choosen, 4 = opened, 8 = removed
		door = random.randint(0,2)
		self.doors[door] = 1
		self.actions.append([])
		self.actions[-1].append("P%d" % (door+1,))
		self.outcome = None

	def __chooseDoor( self ):
		canChoose = map( lambda x: False if x & self.opened \
										 or x & self.removed \
										 or (self.switch and ( x & self.choosen )) \
										 else True, self.doors )
		#print(canChoose)
		guessing = True
		while guessing:
			door = random.randint(0,2)
			if canChoose[door]:
				self.doors[door] = self.doors[door] | self.choosen
				for d in range(len(self.doors)):
					if d!=door:
						self.doors[d] = self.doors[d] & (self.prize | self.opened | self.removed)
				guessing = False
		self.actions[-1].append("C%d" % (door+1,))

	def __reduceDoor( self ):
		door = 0
		if self.randomRemoval:
			door = random.randint(0,2)
		else:   # Monty Hall
			while True:
				door = random.randint(0,2)
				if (self.doors[door]==0):
					break

		self.doors[door] = self.doors[door] | self.removed
		self.actions[-1].append("R%d" % (door+1,))

	def __decideGame( self ):
		self.outcome = False
		if (self.prize | self.choosen) in self.doors:
			self.outcome = True
		self.actions[-1].append(self.outcome)


	def run( self, iterations ):
		for i in xrange( iterations ):
			self.__setup()
			self.__chooseDoor()
			self.__reduceDoor()
			self.__chooseDoor()
			self.__decideGame()


	def __str__( self ):
		out = []
		played = 0
		won = 0
		for game in self.actions:
			played += 1
			if game[-1]:
				won += 1

		out.append("In this game I %s." % (self.switch and "had to switch my choice" or "could switch my choice"))
		out.append("A door was removed %s." % (self.randomRemoval and "randomly" or "by Monty Hall"))
		out.append("I won %d of %d games for %0.2f%% win rate." % (won, played, (won*1.0 / played*1.0) * 100))
		return "\n".join(out)

		#return "Actions: %s" % (self.actions)
		#return "\n".join(map(str,self.actions))


if __name__ == "__main__":
	games = 10000000
	for z in [0,1,2,3]:
		mh = MontyHall( z & 1, z & 2 )
		mh.run(games)
		print(mh)
		print("="*42)
