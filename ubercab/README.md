# Uber Cab

Uber's original name was "UberCab".
Let's say we have a bunch of bumper stickers left over from those days which say "UBERCAB" and we decide to cut these up into their separate letters to make new words.

So, for example, one sticker would give us the letters "U", "B", "E", "R", "C", "A", "B", which we could rearrange into other words (like "car", "bear", etc).

# Challenge:

Write a function that takes as its input an arbitrary string and as output, returns the number of intact “UBERCAB” stickers we would need to cut up to recreate that string.

`solution( string )`

# For instance:

`solution(“car brace”)` would return "2", since we would need to cut up 2 stickers to provide enough letters to write “car brace”.

# Extra:

Expand to include an optional parameter to set the letters of the sticker.

`solution( string, stickerText )`

# Extra:

Write as an object.