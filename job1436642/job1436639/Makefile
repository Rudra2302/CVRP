all: parMDS #seqMDS

parMDS: parMDS.cpp
	nvc++ -O3 -std=c++14 -acc=multicore  parMDS.cpp -o parMDS.out && ./parMDS.out myInputs/inp1000000.vrp -nthreads 20 -round 1 > Solutions/inp1000000_parMDS.sol
	
# seqMDS: seqMDS.cpp
# 	g++ -O3 -std=c++14 seqMDS.cpp -o seqMDS.out && ./seqMDS.out myInputs/inp1000000.vrp > Solutions/inp1000000_parMDS.sol

clean:
	rm -f *.out

cleanFolders:
	rm -rf outinputs*
