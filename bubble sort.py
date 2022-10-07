def sorting(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp,list[j]=list[j],list[j+1]
                list[j+1]=temp
    return list
list=input()
list1=list.split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
print(sorting(list1))
