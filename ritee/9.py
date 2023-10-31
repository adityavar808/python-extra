list1=[]
num=int(input("Enter the number of items in the list :"))
for i in range(num):
    l=int(input("enter the elements :"))
    list1.append(l)
print("List 1",list1)
even=0
odd=0
for i in list1:
    if i%2==0:
        even+=1
    else:
        odd+=1
    
print(f"there are {even} even numbers and {odd} odd numbers")

   