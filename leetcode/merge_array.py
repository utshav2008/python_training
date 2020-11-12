# class Solution:
#     """
#     @param: A: sorted integer array A which has m elements, but size of A is m+n
#     @param: m: An integer
#     @param: B: sorted integer array B which has n elements
#     @param: n: An integer
#     @return: nothing
#     """
#
#     def mergeSortedArray(self, A, m, B, n):
#         # write your code here
#         ll = 0
#         rl = 0
#         nl = []
#         while ll < len(A) and rl < len(B):
#             if A[ll] < B[rl]:
#                 nl.append(A[ll])
#                 ll += 1
#             else:
#                 nl.append(B[rl])
#                 rl += 1
#
#         while ll < len(A):
#             nl.append(A[ll])
#             ll += 1
#         while rl < len(B):
#             nl.append(B[rl])
#             rl += 1


A = [1,2,3]
B = [4,5]

