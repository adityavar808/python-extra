list1=[]
list2=[]
num=int(input("Enter the number of items in  list :"))
for i in range(num):
    l=int(input("enter the elements list :"))
    list1.append(l)
print("List 1",list1)

num1=int(input("Enter the element you want to remove: "))
for i in list1:
   if i!=num1:
       list2.append(i)
       
print(list2)