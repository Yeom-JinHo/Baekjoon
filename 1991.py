import sys

def preorder(arr):
  print(arr[0],end='');
  if arr[1]!=".":
    for l in li:
      if l[0]==arr[1]:
          preorder(l);
  if arr[2]!=".":
    for l in li:
      if l[0]==arr[2]:
          preorder(l);

def inorder(arr):
  if arr[1]!=".":
    for l in li:
      if l[0]==arr[1]:
          inorder(l);
  print(arr[0],end='');
  if arr[2]!=".":
    for l in li:
      if l[0]==arr[2]:
          inorder(l);

def postorder(arr):
  if arr[1]!=".":
    for l in li:
      if l[0]==arr[1]:
          postorder(l);
  if arr[2]!=".":
    for l in li:
      if l[0]==arr[2]:
          postorder(l);
  print(arr[0],end='');
li=list();

n=int(sys.stdin.readline());

for _ in range(n):
  li.append(sys.stdin.readline().rstrip().split());
preorder(li[0])
print();
inorder(li[0])
print()
postorder(li[0])
print()