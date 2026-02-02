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
#if N cannot be divided by nproc evenly we must deal witht he remaining intgerations (Ns)and distribute them to between the cores
int_remain = N % nproc
local_n = rank * base(1 if rank < rem else 0) 
#ensures each MPI process indexes at the correct sampling point so each is only sampled once and then stops at the correct place
start = rank * base + min(rank, rem) 
end = start + local_n 

#vectorised local integral
i = np.arange(start, end, dtype=np.float64)
x = (x + 0.5) * Delta 
local_sum = np.sum(4.0 / (1.0 + x*x), dtype=np.float64) 


