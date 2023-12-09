all: parMDS seqMDS

parMDS: parMDS.cpp
	nvc++ -O3 -std=c++14 -acc=multicore  parMDS.cpp -o parMDS.out && ./parMDS.out inp1.vrp -nthreads 20 -round 1 > outinputs1.txt
	
seqMDS: seqMDS.cpp
	g++ -O3 -std=c++14 seqMDS.cpp -o seqMDS.out && ./seqMDS.out inp1.vrp > outinputs2.txt

clean:
	rm -f *.out

cleanFolders:
	rm -rf outinputs*
