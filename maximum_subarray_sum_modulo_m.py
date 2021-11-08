import sys

a = [1,5,9]
m=5

curr_sum = a[0]
max_sum = 0
i=0
j=0
while(j<len(a) and i<len(a)):
    if(curr_sum>=m):
        temp = curr_sum - a[j]
        if(temp>max_sum):
            max_sum=temp
        curr_sum -= a[i]
        i += 1
        if(i>j):
            j+1
            curr_sum += a[j]
    else:
        j+=1
        curr_sum += a[j]

if curr_sum<m:
    if curr_sum>max_sum:
        max_sum = curr_sum

print(max_sum)

        