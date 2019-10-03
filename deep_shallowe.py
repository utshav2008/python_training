import copy

## Shallow Copy: Object reference points to the same reference, id of the items are pointing to the same location
## Deep Copy: Object reference points to different reference
## create new objects for individul items


list1 = [10,20,30,[40,50,60],{1:1,2:2,3:3}]
list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)

print(list3)

