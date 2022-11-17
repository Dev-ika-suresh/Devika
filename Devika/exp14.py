n=int(input("Enter the number of elements in the list:"))
print("Enter the elements:")
list=[]
for i in range(0,n):
        e = int(input())
        if(e>100):
         list.append('over')
        else:
            list.append(e)
print(list)




