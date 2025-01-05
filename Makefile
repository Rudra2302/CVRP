all: parMDS seqMDS

parMDS: parMDS.cpp
	nvcc -O3 -std=c++14 parMDS.cpp -o parMDS.out && ./parMDS.out myInputs/inp100000.vrp -nthreads 20 -round 1 > Solutions/inp100000_parMDS.sol
	
seqMDS: seqMDS.cpp
	g++ -O3 -std=c++14 seqMDS.cpp -o seqMDS.out && ./seqMDS.out myInputs/inp100000.vrp > Solutions/inp100000_seqMDS.sol

clean:
	rm -f *.out

cleanFolders:
	rm -rf outinputs*
