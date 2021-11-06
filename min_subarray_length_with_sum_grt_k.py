a = [1, 2, 3, 4, 5, 6, 7, 8]
k=20

min_len = len(a)
i=0
j=0
sum = a[0]
while(j<len(a)):
    if(sum>k):
        temp = j-i+1
        min_len = temp if temp<min_len else min_len
        i += 1
        sum -= a[i-1]
        if i>j:
            j += 1
            if(j<len(a)):
                sum += a[j]
    else:
        j += 1
        if(j<len(a)):
            sum += a[j]

print(min_len)
