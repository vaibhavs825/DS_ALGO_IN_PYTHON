a = [1, 4, 3, 2]

# o/p = [3,7,4,8,2,6,1]
# flag = 0
# if(len(a)<=2):
#     print(a)
# else:
#     for i in range(len(a)-1):
#         if flag==0:
#             if(a[i]>a[i+1]):
#                 a[i],a[i+1] = a[i+1],a[i]
#         else:
#             if(a[i]<a[i+1]):
#                 a[i],a[i+1] = a[i+1],a[i]
#
#         flag = 0 if flag==0 else 1
#
#
#     print(a)

def zigZag(arr, n):
    flag = True
    for i in range(n-1):
        if flag is True:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        flag = bool(1 - flag)
    print(arr)

zigZag(a,len(a))

