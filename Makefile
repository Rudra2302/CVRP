all: parMDS seqMDS

parMDS: parMDS.cpp
	nvc++ -O3 -std=c++14 -acc=multicore  parMDS.cpp -o parMDS.out && ./parMDS.out Instances/Ghent2.vrp -nthreads 20 -round 1 > Solutions/Ghent2.sol
	
seqMDS: seqMDS.cpp
	g++ -O3 -std=c++14 seqMDS.cpp -o seqMDS.out && ./seqMDS.out inp1.vrp > Solutions/Brussels1.sol

clean:
	rm -f *.out

cleanFolders:
	rm -rf outinputs*
