da=input()
ls=['c=','c-','dz=','d-','lj','nj','s=','z=']
aqc=0
for k in ls:
    if da.count(k)>0:
         aqc+=da.count(k)
         print(aqc,k)
print(len(da)-aqc)
