
ls=[]
for i in range(100,1000):
    for j in range(100,1000):
        ls.append(i*j)

res=[]
for k in ls:
    s=str(k)
    if len(s)==5:
        if s[0]==s[3] and s[1]==s[2]:
            res.append(int(s))
    elif len(s)==6:
        if s[0]==s[5] and s[1]==s[4] and s[2]==s[3]:
            res.append(int(s))

high=1

for j in res:
    if high > j:continue
    else:
        high=j

print(high)
print(len(res),max(res))
