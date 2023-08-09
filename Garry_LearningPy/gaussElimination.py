import numpy as np

def gaussElim(A,b):
    A = np.concatenate((A,b), axis=1)
    nrow, ncol = A.shape
    
    for row in range(len(A)):
        # partial pivoting process
        max = abs(A[row][row])
        maxr = row
        
        for mrow in range(row,len(A)):
            if max < abs(A[mrow][row]):
                max = abs(A[mrow][row])
                maxr = mrow
        
        if max == 0:
            return "Matrix Singular"
        else:
            A[[row,maxr]]=A[[maxr,row]]
        
        # scaling proses
        scale = A[row][row]
        for col in range(row, ncol):
            A[row][col] = A[row][col] / scale
            
        # reduce rows process
        for rr in range(nrow):
            if rr != row:
                scale = A[rr][row]
                for col in range(row,ncol):
                    A[rr][col] = A[rr][col] - scale*A[row][col]
        
    return A[:,ncol-1]
    
Mrx = np.array(
    [[1.0,3,2,4,3,1], 
     [-4,0,3,2,3,4], 
     [3,-1,3,2,2,5], 
     [3,3,12,2,-6,-4], 
     [-1,-2,-3,7,6,4], 
     [7,5,0,0,4,2]]
    )
R = np.array([[ 4, 5, 6, 10, 6, -8 ]]) # This is a row vector
Rhs = R.T
print(gaussElim(Mrx,Rhs))

A1 = np.array([[2,1,-1],[2,1,-2],[1,-1,1]])
b1 = np.array([[1.0],[-2],[2]])
S1 = gaussElim(A1,b1)
print(S1)

x = np.linalg.solve(Mrx,np.transpose(R))
print(x)

# Rhs = R.T # R.T is transpose of R and a column vector
# S = gaussElim(Mrx,Rhs)
# print(S)
# A1 = np.array([[2,1,-1],[2,1,-2],[1,-1,1]])
# b1 = np.array([[1.0],[-2],[2]])
# S1 = gaussElim(A1,b1)
# print(S1)