import numpy as np
import math
import matplotlib.pyplot as plt

# NxN matrix
MAX_N = 20

# Matrix for jacobi calculation input and output
A = np.zeros((MAX_N-2, MAX_N-2))
A = np.pad(A, pad_width=1, mode='constant', constant_values=1)

# Matrix for jacobi calculation output temp
(row_num, col_num) = A.shape
B = np.zeros((row_num, col_num))

# Do jacobi
converge = False
iteration_num = 0
while (converge == False):
    iteration_num = iteration_num+1
    diffnorm = 0.0

    # for convinience, use padding border
    A_padding = np.pad(A, pad_width=1, mode='constant', constant_values=0)

    for i in range(row_num):
        for j in range(col_num):
            # because we do padding, index changed
            idx_i_A = i + 1
            idx_j_A = j + 1
            # Do jacobi
            B[i][j] = 0.25*(A_padding[idx_i_A+1, idx_j_A]
                            + A_padding[idx_i_A-1, idx_j_A]
                            + A_padding[idx_i_A, idx_j_A+1]
                            + A_padding[idx_i_A, idx_j_A-1])
            # simple converge test
            diffnorm += math.sqrt((B[i, j] - A[i, j])*(B[i, j] - A[i, j]))
    A = np.copy(B)
    
    # check converge
    print('Error : %f' % diffnorm)
    if diffnorm <= 0.0001:
        print('Converge, iteration : %d' % iteration_num)
        print('Error : %f' % diffnorm)
        converge = True

# Show
plt.imshow(A, cmap='gray', interpolation='nearest')
plt.show()