def maximumProduct(inputArray):
    # Write your code here
    mod = 1000000007
    inputArray = sorted(inputArray)
    n = len(inputArray)

    occur = [0]*(n+1)
    occur[0] = 1
    for i in range(1,n+1):
        occur[i] = 2*occur[i-1]
        occur[i] %= mod

    result = 1
    for i in range(n-1,-1,-1):
        val = (occur[i]-1)
        for j in range(val):
            result *= inputArray[i]
            result %= mod

    for i in range(n):
        result *= inputArray[i]
        result %= mod

    return result