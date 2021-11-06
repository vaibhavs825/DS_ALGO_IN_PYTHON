
m=3
n=3

def count_path(i,j):
    if(i>m or j>n):
        return 0
    if(i==m and j==n):
        return 1
    return count_path(i+1,j)+count_path(i,j+1)


total_path = 0
total_path = count_path(1,1)
print(total_path)