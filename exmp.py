def gcd(m,n):
     #assume m >= n
     if m < n:
          (m,n) = (n,m)
     if (m%n) == 0:
          return n
     else:
          diff = m-n
     return (gcd(max(m, diff),min(n, diff)))
