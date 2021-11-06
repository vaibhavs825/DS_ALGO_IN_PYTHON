a = "abcba"
b = "aaaaa"
c = "babad"
d = "cbbd"
e = "a"
f = "ac"
g = ""

# iterate all elements
#

def expand(a,j,k):
    res = ''
    while(j>=0 and k<len(a) and a[j]==a[k]):
        res = a[j:k+1]
        j -= 1
        k += 1
        # res[0] +=1
    return res

for x in [a,b,c,d,e,f]:
    result = ''
    for i in range(len(x)):
        odd = expand(x,i,i)
        even = expand(x,i,i+1)
        if(len(odd)>len(even)):
            if(len(odd)>len(result)):
                result = odd
        else:
            if(len(even)>len(result)):
                result = even

    print(result)









