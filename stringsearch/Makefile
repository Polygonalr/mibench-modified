FILE1 = bmhasrch.c  bmhisrch.c  bmhsrch.c  pbmsrch_small.c 
FILE2 = bmhasrch.c  bmhisrch.c  bmhsrch.c  pbmsrch_large.c 

all: search_large

search_large: ${FILE2} Makefile
	gcc -static ${FILE2} -O3 -o search_large

clean:
	rm -rf search_large output*
