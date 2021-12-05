a = [pow(2,i) for i in range(20)]

def parallelize(arr,j):
    b = arr.pop(j)
    a = arr.pop(j-1)
    c = []
    for x,y in zip(a,b):
        c.append(x)
        c.append(y)
    arr.insert(j-1,c)
    return arr

def split_(arr,j):
    b = arr.pop(j)
    a = arr.pop(j-1)
    arr.insert(j-1,a+b)
    return arr

def inputStream(distributionNodes, streamAtLeaves):
    # Write your code here
    n = len(distributionNodes)
    j = len(streamAtLeaves)-1
    for i in range(n,0,-1):
        if i+1 in a:
            j = len(streamAtLeaves)-1
        if distributionNodes[i-1]==1:
            streamAtLeaves = parallelize(streamAtLeaves,j)
        elif distributionNodes[i-1]==0:
            streamAtLeaves = split_(streamAtLeaves,j)
        j -= 2

    return streamAtLeaves

print(inputStream([1,0,0],[[10],[20],[30],[40]]))