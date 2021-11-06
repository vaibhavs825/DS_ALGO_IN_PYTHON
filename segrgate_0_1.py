a = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]

i=0
j=len(a)-1
while(i<j):
    if(a[i]==1):
        a[i],a[j] = a[j],a[i]
        j -=1
    else:
        i +=1

print(a)