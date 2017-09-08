CC = gcc
CFLAGS = -pedantic -Wall



all: bg

bg: bg.o
	$(CC) -o bg bg.o

bg.o: bg.cpp
	$(CC) $(CFLAGS) -c bg.cpp

clean:
	rm bg.o bg