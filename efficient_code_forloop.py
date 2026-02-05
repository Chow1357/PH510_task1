#!/opt/software/anaconda/python-3.10.9/bin/python
"""
Parallel approximation of pi using MPI and the mid-point rule

Tested with: 
    Python 3.10.9
    mpi4py 
    OpenMPI
"""
#import mpi4py 
from mpi4py import MPI 
#defining the global communicator containing MPI processes
#rank defines the process's ID 
#nproc is the total number of processes launched which in this case is 16 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nproc = comm.Get_size()
