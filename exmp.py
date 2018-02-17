def gcd(m,n):
     #assume m >= n
     if m < n:
          (m,n) = (n,m)
     if (m%n) == 0:
          return n
     else:
          diff = m-n
     return (gcd(max(m, diff),min(n, diff)))

####
## Anather exmple of using while and if setement
###

def gcd(m,n):
     if m < n:
          (m,n) = (n,m)
     while (m%n) != 0:
          diff  = m-n
     #diff > n? possible
     (m,n) = (max(n,diff), min(n,diff))
     return (n)

#More exmples
def gcd(m,n):
     if m < n:
          (m,n) = (n,m)
     if (m%n) == 0:
          return n
     else:
          return (gcd(n,m%n)) #m%n < n always!

#more exmples using while

def gcd(m,n):
     if m < n:
          (m,n) = (n,m)
     while (m%n) != 0:
          (m,n) = (n,m%n) # m%n < n, always!
     return(n)
