list1=[]
list2=[]
num=int(input("Enter the number of items in the list :"))
for i in range(num):
    l=int(input("enter the elements :"))
    list1.append(l)
print("List 1",list1)
for num in list1:
    if num not in list2:
        list2.append(num)

print("List after removing duplicates ",list2)