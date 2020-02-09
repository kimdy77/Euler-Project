import math
def prime(n):
    ls=[]
    for i in range(int(math.sqrt(n)),3,-1):
        if n%i==0:
            ls.append(i)
    return ls

print(prime(600851475143))
