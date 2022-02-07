import sys

def kadaneNeg(A,k):
    max_so_far = [-sys.maxsize]*k

    max_ending_here = [0]*k

    for i in range(len(A)):
        for j in range(k):
            max_ending_here[j] = max_ending_here[j] + A[i]

        for j,_ in enumerate(max_ending_here):
            max_ending_here[j] = max(max_ending_here[j], A[i])

        for j,_ in enumerate(max_so_far):
            max_so_far[j] = max(max_so_far[j], max_ending_here[j])

    return max_so_far.sort(reverse=True)
# def find_n(k):
#     value = 0
#     i=0
#     while True:


def max_sum(A,k):
    n = len(A)
    total = 1 << n
    top_k = [0]*k
    for i in range(total):
        Sum = 0

        for j in range(n):
            if ((i & (1 << j)) != 0):
                Sum += A[j]

        if top_k[-1]<Sum:
            top_k[-1]=Sum
            top_k = sorted(top_k,reverse=True)

    return top_k


if __name__ == '__main__':
    A = [3,5,-2]
    print("The sum of contiguous sublist with the largest sum is", max_sum(A,3))