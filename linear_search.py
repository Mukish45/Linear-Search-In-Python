import numpy as N
n=int(input("Enter the size of the array : "))
a= N.zeros ((n), dtype = 'i')
for i in range(n):
   b=int(input("Enter the element: "))
   a[i]=b
print("The elements in the array are:",a)
key=int(input("Enter the item to search: "))


def linear_search(a,key):
   for i in range(len(a)):
      if(a[i]==key):
         return(i)
   return(-1)


index=linear_search(a,key)
if(index!=-1):
   print("Entered element is found at index ",index)
else:
   print("Entered element not found")


print(type(a))
