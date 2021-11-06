import bisect

mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

max_ones = 0
row = -1

m,n = len(mat),len(mat[0])

for i,r in enumerate(mat):
       occ = bisect.bisect_left(r,1)
       temp = len(r)-occ
       if(max_ones<temp):
              max_ones=temp
              row = i

print(row)