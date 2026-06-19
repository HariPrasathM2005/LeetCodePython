def isDuplicate(List1,val):
    c=0
    for i in range(0,len(List1)):
        if(List1[i]==val):
            c=c+1
    if(c>1):
        return False
    else:
        return True
def Uncommon(s1,s2):
    res=[]
    print(s1)
    List1=s1.split(" ")
    List2=s2.split(" ")
    for i in List1:
        if (i not in List2) and (i not in res):
            val=isDuplicate(List1,i)
            if(val):
                res.append(i)
    for i in List2:
        if i not in List1 and i not in res:
            val=isDuplicate(List2,i)
            if(val):
                res.append(i)
    print(res)
if __name__=="__main__":
    s1="this apple is sweet"
    s2="this apple is sour"
    Uncommon(s1,s2)
