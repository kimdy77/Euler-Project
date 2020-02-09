def fibo(n):
    ls=[1,2]
    while int(max(ls)) < n:
        ls.append(sum(ls[-2:]))
    return ls[:-1]

print(fibo(4000000))
j=0
for i in fibo(4000000):
    if i%2==0:
        j+=i

print(j)
