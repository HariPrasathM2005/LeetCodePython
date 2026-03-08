s=input()
res=False
next=False
zerosoccurs=False
if(len(s)==1 and s[0]=='1'):
    res=True
for i in range(0,len(s)):
    if(s[i]=='1' and zerosoccurs==False):
        res=True
    elif(s[i]=='1' and zerosoccurs==True):
        res=False

    if(s[i]=='0'):
        zerosoccurs=True
print(res)
