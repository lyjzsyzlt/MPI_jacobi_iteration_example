# MPI_jacobi_iteration_example
Implementation of Jacobi with Python and MPI

* Normal implementation of jacobi
* MPI implementation with mpi4py

# Defendancy
* numpy
* math
* mpi4py

Need MPI installation for mpi4py

For ubuntu,
```
sudo apt-get install mpich
```

# Test run

```
mpirun -n 4 python jacobi_mpi.py
```
