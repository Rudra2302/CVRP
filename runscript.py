import os

nvalues = [5000,6000,10000,15000,20000]

for n in nvalues:
    inputfile = "myInputs/inp" + str(n) + ".vrp"
    outputfile = "myOutputs/out" + str(n) + ".txt"
    os.system("nvc++ -O3 -std=c++14 -acc=multicore  parMDS_baseline.cpp -o parMDS.out && ./parMDS.out" + inputfile + "-nthreads 20 -round 1 > " + outputfile)
    os.system("nvc++ -O3 -std=c++14 -acc=multicore  parMDS_oldPrims.cpp -o parMDS.out && ./parMDS.out" + inputfile + "-nthreads 20 -round 2 >> " + outputfile)
    os.system("nvc++ -O3 -std=c++14 -acc=multicore  parMDS_oldTSP2.cpp -o parMDS.out && ./parMDS.out" + inputfile + "-nthreads 20 -round 3 >> " + outputfile)
    os.system("nvc++ -O3 -std=c++14 -acc=multicore  parMDS.cpp -o parMDS.out && ./parMDS.out" + inputfile + "-nthreads 20 -round 4 >> " + outputfile)
