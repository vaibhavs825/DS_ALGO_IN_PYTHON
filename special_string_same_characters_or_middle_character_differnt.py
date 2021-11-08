s = "abcbaba"

s = "adaa"
n = len(s)

def expand(s,i,j):
    count = 0
    if(i==j):
        count += 1
        if(i>0):
            char = s[i-1]
        else:
            char = s[i]
        i -= 1
        j += 1
    else:
        char = s[i]
    while(i>=0 and j<len(s) and s[i]==char and s[j]==char):
        count += 1
        i -= 1
        j += 1
    return count

# def expand_b(s,i,j):
#     count = 0
#     count =

count = 0
for i in range(n):
    count += expand(s,i,i)
    # count += expand(s,i-1,i+1)
    count += expand(s,i,i+1)

print(count)
