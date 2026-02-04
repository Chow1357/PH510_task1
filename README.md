# PH510_task1
# the code, job scripts and output files in this repository were all used in assignment 1 which was based on approximating pi from a definite integral. it uses mpi4py.
 the code in this repository was run tested using python 3.10.9 with mpi4py and OpenMPI.

 the LICENSE file contains a suitable MIT License for this code. 

 the original code is in the .py file 'original_bad_code.py' this was run in the job script 'run_code_mpi_only_original_code.sh' and the output is 'original_bad_code_test.out'

 the improved efficient code where all the main improvements were made is in the .py file 'efficient_code.py' this was run in job script 'run_code_mpi_only_efficient.sh' and the output is in the output file 'efficient_code_test.out' 

 both codes were then run for different numbers of cores in the job scripts 'run_code_mpi_only_best_efficient_diffcores.sh' and 'run_code_mpi_only_best_efficient_allcores.sh' for cores (1,2,4,8,16) and (1,2,....,16) respectivley. 

 the output of the ''run_code_mpi_only_best_efficient_diffcores.sh' job script is the output file 'both_code_diff_cores.out'. 

 the output for 'run_code_mpi_only_best_efficient_allcores.sh' is the output file '' this is where you can find comparable numerical results for the code being run in parallel
 and in serial. 

there are two extra job scripts that can be useful. 

'run_code_mpi_only_best_efficient_allcores.sh' runs the efficient code and the original code on rank numbers (1,2,3,4...,16) run after run after run. 

'run_code_only_efficient_allcores.sh' runs only the efficient code on all the different number of cores run after run after run, with a warm up at the start incase mpi module needs a warm up run to not affect the recorded runs. 

