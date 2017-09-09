CC = gcc
FRAMEWORKS:= -framework Foundation 
LIBRARIES:= -lobjc
CFLAGS = -pedantic -Wall -ObjC

all: odd

odd: odd.o
	$(CC) -ObjC -o odd odd.o

odd.o: odd.m
	$(CC) $(CFLAGS) -c odd.m

clean:
	rm odd.o odd
