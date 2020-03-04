


list1 = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

print(zip(*list1[::-1]))



# ===> [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]

# list2 = []
# for n in range(len(list1)):
#     a= []
#     for i in list1[::-1]:
#         a.append(i[n])
#     list2.append(a)

# for item in list1[::-1]:
#     l = len(item)
#     for i in range(i):
#         print()

# //
# for (r = 0; r < m; r++)
# {
#    for (c = 0; c < n; c++)
#    {
#       // Hint: Map each source element indices into
#       // indices of destination matrix element.
#        dest_buffer [ c ] [ m - r - 1 ] = source_buffer [ r ] [ c ];
#    }
# }
# //


#### Solution One
print(list(zip(*list1[::-1])))

### Solution Two
# for i in range(0,len(list1)):
#     for j in range(0,len(list1)):
#         list1[j][len(list1) - i - 1] = list1[i][j]





