from scipy import *
import numpy as np

def row_reduce(A, b, n): 
    (rows, cols) = shape(A)
    for i in range(rows):
        if i > n:
            scale = (A[i,n] / A[n,n])
            b[i] = b[i] - scale * b[n]
            for k in range(cols):
                A[i,k] =  A[i,k] - scale * A[n,k]
        else:
            continue
    ## No return values needed bc python automatically passes pointers to the call stack

def gauss_eliminate(A, b):
    (rows, cols) = shape(A)
    x = zeros(len(b))
    for i in range(rows):
        row_reduce(A, b, i)
    
    # Back substitution.
    for i in reversed(range(rows)):
        x[i] = (b[i] - sum(A[i, :] * x)) / A[i, i]
    
    return x
        

        
A = np.array([[1., 2., 3.], [3., 2., 2.], [2., 6., 2.]])
b = np.array([3., 4., 4.])

print(gauss_eliminate(A, b))


