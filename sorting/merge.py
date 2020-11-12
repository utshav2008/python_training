A = [5,6,8,10]
B = [9,11,15,17]
C = []

ll = 0
rl = 0
# ll = len(A)
# rl = len(B)
while ll < len(A) and rl < len(B):
    if A[ll] < B[rl]:
        C.append(A[ll])
        ll += 1
    else:
        C.append(B[rl])
        rl += 1
while ll < len(A):
    C.append(A[ll])
    ll += 1
while rl < len(B):
    C.append(B[rl])
    rl += 1

print(C)