list1=[]
list2=[]
list3=[]
num=int(input("Enter the number of items in the first list :"))
for i in range(num):
    l=int(input("enter the elements of first list :"))
    list1.append(l)
print("List 1",list1)

num=int(input("Enter the number of items in the second list :"))
for i in range(num):
    l=int(input("enter the elementsof second list :"))
    list2.append(l)
print("List 2",list2)


for num in list1:
    if num not in list3:
        list3.append(num)

for num in list2:
    if num not in list3:
        list3.append(num)


print("list of unique elements of both list 1 and list2 :",list3)