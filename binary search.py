def binarySearch(list,key):
    low=0
    high=len(list)-1
    while low<=high:
        mid=int((low+high)/2)
        if list[mid]==key:
            return mid
        if key>list[mid]:
            low=mid+1
        if key<list[mid]:
            high=mid-1
    return -1

list=input()
list_1=list.split()
for n in range(len(list_1)):
    list_1[n]=int(list_1[n])
print(list_1)
key=int(input())
res=binarySearc