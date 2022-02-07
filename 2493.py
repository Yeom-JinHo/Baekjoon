import sys

n=int(sys.stdin.readline());

top=list(map(int,sys.stdin.readline().split()));

st=list();

for i in range(n): 
	while st and top[i]>top[st[-1]]: 
		st.pop();
	if st:
		st.append(i);
		print(0,end=" ");
	else:
		print(st[-1]+1,end=' ');
		st.append(i);

