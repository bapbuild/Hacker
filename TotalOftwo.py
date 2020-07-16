str1= input().strip()
str2=[]
if len(str1)%2==0:
    for i in range(0,len(str1),2):
        str2.append(int(str1[i])+int(str1[i+1]))
else:
    for i in range(0,len(str1)-1,2):
        str2.append(int(str1[i])+int(str1[i+1]))

print(str2)
