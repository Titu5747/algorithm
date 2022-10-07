def selection(list):
    for i in range(len(list)-1):
        for j in range(len(list)):
            if list[i]<list[j]:
                temp,list[i]=list[i],list[j]
                list[j]=temp
    return list
list=input()
list1=list.split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
print(selection(list1))