list1=[]
num=int(input("Enter the number of items in the list :"))
for i in range(num):
    l=int(input("enter the elements :"))
    list1.append(l)
print("List 1",list1)
min_element=list1[0]
for i in list1:
   if i<min_element:
     min_element=i
print("the minimum element is :",min_element)