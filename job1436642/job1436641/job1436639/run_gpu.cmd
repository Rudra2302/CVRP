#!/bin/bash
#PBS -e errorfile_1mil_rudra.err
#PBS -o logfile_1mil_rudra.log
#PBS -l walltime=48:00:00
#PBS -l select=1:ncpus=1:ngpus=1
#PBS -q gpuq
tpdir=`echo $PBS_JOBID | cut -f 1 -d .`
tempdir=$HOME/scratch/job$tpdir
mkdir -p $tempdir
cd $tempdir
cp -R $PBS_O_WORKDIR/* .
module load cuda11.4
make all
mv ../job$tpdir $PBS_O_WORKDIR/.