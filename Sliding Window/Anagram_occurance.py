str1="foqxxforxaor"
str2="fox"
k=min(len(str1),len(str2))
temp=k
i=0
j=0
s=""
count=0
while(i<len(str1)-(temp-1)):
    res=str1[i:k]
    if sorted(res)==sorted(str2):
        count+=1
    i+=1
    k+=1
print(count)
