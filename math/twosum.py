A = [2, 7, 11, 15]
target = 26

def twosum(A,target):

    sum_index = {}
    for i in range(len(A)):
        if (target - A[i]) in sum_index:
            return sum_index[(target - A[i])],i
        else:
            sum_index[A[i]] = i

print(twosum(A,target))
