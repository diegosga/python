def LU(A):
  n = len(A)
  x = [0]*n

  for k in list(range(1,n,1)):
    for i in list(range(k+1,n+1,1)):
      m = A[i-1][k-1]/A[k-1][k-1]
      A[i-1][k-1] = m
      for j in list(range(k+1,n+1,1)):
        A[i-1][j-1] = A[i-1][j-1]-m*A[k-1][j-1] 

  return A


def solveLowerTriangular(L,b):
  n = len(b)
  y = [0]*n
  
  for i in list(range(1,n+1,1)):
    s = 0
    for j in list(range(1,i,1)):
      s = s + L[i-1][j-1]*y[j-1]

    y[i-1] = b[i-1] - s

  return y

def solveUpperTriangular(U,b):
  n = len(b)
  x = [0]*n
  x[n-1] = b[n-1]/U[n-1][n-1]

  for i in list(range(n-1,0,-1)):
    s = 0
    for j in list(range(i+1,n+1,1)):
      s = s + U[i-1][j-1]*x[j-1]

    x[i-1] = (b[i-1]-s)/(U[i-1][i-1])

  return x



Ai = [[3, 2, 4],
      [1, 1, 2],
      [4, 3,-2]]

bi = [1, 2, 3]

A = LU(Ai)
print("A =",A)
y = solveLowerTriangular(A,bi)
print("y =",y)
x = solveUpperTriangular(A,y)
print("x =",x)