str=input("Enter the string:")
dict={}
a=str.split(' ')
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for k,v in dict.items():
    print(k,v)

