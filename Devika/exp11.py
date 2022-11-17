str1=input("Enter the string1: ")
str2=input("Enter the string2:")
a=str2[0]
b=str1[0]
newstr1=str2[0]+str1[1:]
newstr2=str1[0]+str2[1:]
print(newstr1+' '+newstr2)
