### WRONG SOLUTION

a = [1,2,3]

k = 2
max_sum = 0
end = (k-1)*2 + 1
for i in range(0,min(end,len(a)),2):
    temp_sum = 0
    for j in range(k):
        temp_sum += a[i + j*2]
    if(temp_sum>max_sum):
        max_sum = temp_sum

end = (k-1)*2
for i in range(1,min(end,len(a)),2):
    temp_sum = 0
    for j in range(k):
        temp_sum += a[i + j*2]
    if(temp_sum>max_sum):
        max_sum = temp_sum

print(max_sum)