# Monty Hall

This puzzle is to provide a simulation of the Monty Hall puzzle.

Your goal, is to design and implement a system that allows the Monty Hall puzzle to play out.

Probably the data needed is:
* an array of the doors [0, 0, 1] or [ 'G', 'G', 'C'] or anything of your choice
* the original choice
* either the second choice, or a flag to swap the choice (true to swap, false to stay).

This could be done with a single function, or with a system of objects:
* Door object, would hold the doors, and what is behind them
* Host (MontyHall) object, would know which door holds which, and will always reviel a 'goat' after the first pick
* The player object, makes a choice, then decides to swap or not.

How ever the solution is done, this should be able to be run many times, gathering the output to calculate statistics at the end.

As you might imagine, an optimal solution might be best.

Bonus for making it something that could be turned into a game, or turning it into a game.

# Data output

Post the stats output, maybe not the entire data run.

# What is expected

The data should probably support the published ideas that swapping the choice will result in a higher odds of winning.