CFLAGS= -O2 -Wall 

fibonacci:
	gcc -o fibonacci fibonacci.c $(CFLAGS)

clean:
	rm -f fibonacci
