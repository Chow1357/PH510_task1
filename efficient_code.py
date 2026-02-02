#!/opt/software/anaconda/python-3.10.9/bin/python
"""
approximation of pi using th emid point rule for a definite integral 

Tested using: 
    Python 3.10.9
    mpi4py
    OpenMPI
"""
#import the necessary functions 
import mpi4py as MPI 
import numpy as np 

# stating defining variables for the main features of MPI including the main communicator 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nproc = comm.Get_size() 

# number of sample points in the integration and defining the width of each sample point between 0 and 1
N = 100000000
DELTA = 1.0 / N 

#sharing the workload, number of integration points, equally between the cores (nproc = 16) 
min_jobs = N // nproc 

