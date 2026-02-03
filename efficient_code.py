#!/opt/software/anaconda/python-3.10.9/bin/python
"""
code that approximates pi using the mid point rule
for a definite integral, optimised for a parallel environment

Tested using:
    Python 3.10.9
    mpi4py
    OpenMPI
"""
#import the necessary functions
from mpi4py import MPI # pylint: disable=no-name-in-module
import numpy as np
#stating defining variables for the main features of MPI
#including the main communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nproc = comm.Get_size()

#number of sample points in the integration and defining the width
#of each sample point between 0 and 1
N = 100000000
DELTA = 1.0 / N

#sharing the workload, number of integration points,
#equally between the cores (nproc = 16)
min_jobs = N // nproc
#if N cannot be divided by nproc evenly we must deal witht he remaining
#intgerations (Ns) and distribute them to between the cores
#good incase N value changes
int_remain = N % nproc
local_n = min_jobs + (1 if rank < int_remain else 0)
#ensures each MPI process indexes at the correct sampling point
#so each is only sampled once and then stops at the correct place
start = rank * min_jobs + min(rank, int_remain)
end = start + local_n

#vectorised local integral
i = np.arange(start, end, dtype=np.float64)
x = (i + 0.5) * DELTA
local_sum = np.sum(4.0 / (1.0 + x*x), dtype=np.float64) * DELTA
#combines all the partial results in each rank using the SUM operation
#and then returns this result only to rank 0
I = comm.reduce(local_sum, op=MPI.SUM, root=0)
#prints the final result in rank 0 to 10 decimal places
if rank == 0:
    print(f"integral {I:.10f}")
