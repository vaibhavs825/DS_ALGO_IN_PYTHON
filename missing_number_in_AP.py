arr = [[1, 6, 11, 16, 21, 31], [5,7,11,13], [12,14,15],[2, 4, 8, 10, 12, 14], [1, 6, 11, 16, 21, 31], [15,13,12]]

# d1 = a[1]-a[0]
# d2 = a[2]-a[1]
# d3 = a[3]-a[2]
#
# d = 0
# if(d1==d2 and d2==d3):
#     d = d1
# elif(d1==d2):
#     d = d1
# elif(d1==d3):
#     d = d1
# elif(d2==d3):
#     d = d2
for a in arr:
    n = len(a)
    d = (a[n-1]-a[0])//n

    missing_element = -1
    for i,x in enumerate(a[1:]):
        i += 1
        if(a[i] == (a[i-1]+(2*d))):
            missing_element = a[i-1]+d
    print(missing_element)

    # Binary Search
    l=0
    r=n-1
    while l <= r:
        mid = (l + r)//2
        if (a[mid] - a[0])//d == mid:
            l = mid + 1
        else:
            r = mid - 1
    print(a[r] + d)
