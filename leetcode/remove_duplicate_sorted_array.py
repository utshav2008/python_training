l = [1,1,2,2,3,3,3,4,5,6,6,6]
#
# i = 0
# j = 1
# while i < len(l)-1:
#    if l[i] != l[i+1]:
#       l[j] = l[i+1]
#       j += 1
#    i+=1
# print(l)
# print(j)
#
#
#
#
#
print(len(l) + 3)
i = 0
j = 0
while i < len(l):
    print(l[i])
    if l[i]/2 == l[j]:
        print(f'printing {j} {l[j]}')
        j = i
    print(i,j)
    i+=1


