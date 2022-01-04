import sys

input=sys.stdin.readline().rstrip().upper()
count=[0]*26
for inp in input:
  count[ord(inp)-ord('A')]+=1

result=[]

for i in range(0,26):
  if(max(count)==count[i]):
    result.append(chr(i+65))

print(result[0] if len(result)<2 else '?')