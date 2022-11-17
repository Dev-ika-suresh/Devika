a=int(input("Enter the number of strings:"))
print("Enter the strings:")
list=[]
count=0
for i in range(0,a):
    b=input()
    list.append(b)
print(list)
for i in list:
    for j in i:
        if j=='a':
            count=count+1
            print(count)