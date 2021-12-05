def getMinimumSeconds(height, h, u, v):
    # Write your code here
    min_seconds = 0
    if 2*u <= v:
        return len(height)*u

    height = sorted(height)
    i=0
    j=len(height)-1
    while(i<=j):
        if i!=j and height[j]+height[i]<h:
            i += 1
            min_seconds += v
        else:
            min_seconds += u
        j -= 1

    return min_seconds
            