A = [1,2,2,3]

increase = True
decrease = True
for i in range(len(A)-1):
    if A[i] > A[i+1]:
        increase = False
    if A[i] < A[i+1]:
        decrease = False

print(decrease or increase)
print(False or False)
print(False or True)
