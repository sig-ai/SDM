CC=clang++
LSDL=$(shell sdl2-config --cflags --libs)
FLAGS=$(LSDL) -std=c++11 -Wall
LDFLAGS=$(LSDL) -std=c++11 -Wall

SRCS=$(wildcard *.hpp)
_OBJS=$(SRCS:%.hpp=%.o)
OBJS=$(patsubst %,$(DIR)/%,$(_OBJS))
DIR=bin

all: main


main: pre $(OBJS)
	$(CC) main.cpp $(OBJS) $(FLAGS) -o main


pre:
	mkdir -p $(DIR)


$(DIR)/%.o: %.cpp %.hpp
	$(CC) -c $< $(LDFLAGS) -o $@


.PHONY: clean


clean:
	rm -rf bin
