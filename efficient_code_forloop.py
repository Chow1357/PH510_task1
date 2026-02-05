#!/opt/software/anaconda/python-3.10.9/bin/python
"""
Parallel approximation of pi using MPI and the mid-point rule

Tested with:
    Python 3.10.9
    mpi4py
    OpenMPI
"""
#import mpi4py
from mpi4py import MPI # pylint: disable=no-name-in-module
#defining the global communicator containing MPI processes
#rank defines the process's ID
#nproc is the total number of processes launched which in this case is 16
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nproc = comm.Get_size()
#N is the number of integral samples
#delta is the width of each integral sample point
N = 100000000
DELTA = 1.0 / N
#defining the integral for the approximation of pi
def integrand(x):
    """returns the integrand function  for the pi integral"""
    return 4.0 / (1 + x*x)

LOCAL_SUM = 0.0
# Each rank does i = rank, rank+nproc, rank+2*nproc,...
# Strided work distribution:
# This ensures all integration points are covered exactly once with
# minimal communication and good load balancing.
# xi this is our midpoint rule and samples at the centre of each interval
for i in range(rank, N, nproc):
    xi = (i + 0.5) * DELTA
    LOCAL_SUM += integrand(xi) * DELTA
# Combine once all the ranks and returns the result only to rank 0
I = comm.reduce(LOCAL_SUM, op=MPI.SUM, root=0)
#prints the result contained in rank 0 once
if rank == 0:
    print(f"Integral {I:.10f}")
