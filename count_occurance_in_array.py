a = [2,3,3,1,5]

i=0
while(i<len(a)):
    if(a[i]<=0):
        i += 1
    else:
        if(a[a[i]-1]<=0):
            a[a[i]-1] -= 1
            a[i] = 0
        else:
            x = a[i]
            a[i] = a[a[i]-1]
            a[x-1] = -1

for i,x in enumerate(a):
    print(i+1, "->" , -x)
