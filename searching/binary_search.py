# #=======
# # O(n)
# #======
#
# def linear_search(data, target):
#     for i in range(len(data)):
#         if data[i] == target:
#             return True
#         return False
#
# #========
# # O(logn)
# #========
#
# data =
# # only takes sorted array
#
# def binary_search(data, low, high):
#
#
# def binary_search(data, target):
#     low = 0
#     high = len(data) - 1
#     mid = (low + high)/2
#
# print((5+8)//2)

data_set = [2,5,6,8,9,10,14,16,20,24,26,29]
data = 20

def binary_search(data_set, data, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data == data_set[mid]:
            return True
        elif data > data_set[mid]:
            return binary_search(data_set, data, mid+1, high)
        else:
            return binary_search(data_set, data, low, mid-1)

print(binary_search(data_set,data,0,len(data_set)))

