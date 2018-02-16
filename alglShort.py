# short way
def gcd(m,n):

     cf = []
     for i in range(1,min(m,n)+1):
          if (m%i) == 0 and (n%i) == 0:
               cf.append(i)
     return(cf[-1])


#When There is No lists!

def gcd(m,n):
     for i in range(1,min(m,n)+1):
          if (m%i) == 0 and(n%i) == 0:
               mrcf = i
     return (mrcf)


#No lists using while

def gcd(m,n):

     i = min(m,n)

     while i > 0:
          if (m%i) == 0 and (n%i) == 0:
               return(i) #----> exit
          else:
               i = i-1 #update i to i-1
