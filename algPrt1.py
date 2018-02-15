#use fm, fn, for list of factors of m, n, respectively
#for each i from 1 to m, add i to fm if i divides m
#for each j from 1 to n, add j to fn if j divides n
#use cf for list of common factors
#for each f in fm, add f to cf if also appears in fn
#Return largest(rightmost(values in cf

def gcd(m,n):
     fm = []
     for i in range(1,m+1):
          if (m%i) == 0:
               fm.append(i)
     fn = []
     for j in range(1,n+1):
          if (n%j) == 0:
               fn.append(j)
     cf = []
     for f in fm:
          if f in fn:
               cf.append(f)
     return(cf[-1])
