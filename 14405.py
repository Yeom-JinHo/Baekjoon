import sys

pikachu=["pi","ka","chu"]

inp=sys.stdin.readline().rstrip();

for word in pikachu:
  inp=inp.replace(word,"."*len(word));

if inp=="."*len(inp):
  print("YES")
else:
  print("NO")