import sys

V = 7
m = [9,6,5,3]
m.sort()
arr = [sys.maxsize]*(V+1)
arr[0] = 0
for i,x in enumerate(m):
    for j in range(x,V+1):
        arr[j] = min(arr[j],1+arr[j-x])

if arr[V]==sys.maxsize:
    arr[V]=-1
print(arr[V])
