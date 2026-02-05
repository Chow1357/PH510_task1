# PH510_task1
# the code, job scripts and output files in this repository were all used in assignment 1 which was based on approximating pi from a definite integral. it uses mpi4py.

this repository contains the original bad code 'original_bad_code.py' and then I have provided two alternatives. The main alternative which shows very good parallel scaling from 1 to 16 cores is 'efficient_code_forloop.py' the second code uses a vectorised intergal method 'efficient_code.py' and is much faster than the forloop method however could break if N is too large and does not represent scaling as well as the for loop code. 

# for loop code 
the for loop code was run as well as the original code in the job script 'run_code_mpi_only_best_efficient_loop_diffcores.sh' and gave the output 'forloop_and_original_run.out'
the run times from this is the data we used for our plots in the 1 page hand in. 

# vectorised integral code
this was an additional method that was trialled to try and imprve the speeds in the parallel environement
the optimised code using this method is in 'efficient_code.py'. this did significantly imprve the speeds, however there is potential for it to break for different number of sample integrals. 

