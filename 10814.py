n=int(input())
dic=list()
for i in range(n):
    ag,na=input().split()
    dic.append([int(ag),na])
print(dic)
dic=sorted(dic,key = lambda x: x[0])

for ag,na in dic:
    print(ag,na)
