CC = gcc
FRAMEWORKS:= -framework Foundation
LIBRARIES:= -lobjc
CFLAGS = -Wall -Werror -g -v -pedantic -ObjC
LDFLAGS=$(LIBRARIES) $(FRAMEWORKS)

all: cyc

cyc: cyc.o
	$(CC) cyc.o $(CFLAGS) $(LDFLAGS) -o cyc

cyc.o: cyc.m
	$(CC) $(CFLAGS) -c cyc.m

clean:
	rm cyc.o cyc
