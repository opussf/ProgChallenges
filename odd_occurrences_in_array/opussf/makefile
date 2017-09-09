CC = gcc
FRAMEWORKS:= -framework Foundation
LIBRARIES:= -lobjc
CFLAGS = -Wall -Werror -g -v -pedantic -ObjC
LDFLAGS=$(LIBRARIES) $(FRAMEWORKS)

all: odd

odd: odd.o
	$(CC) odd.o $(CFLAGS) $(LDFLAGS) -o odd

odd.o: odd.m
	$(CC) $(CFLAGS) -c odd.m

clean:
	rm odd.o odd
