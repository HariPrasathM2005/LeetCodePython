def Numberofones(str):
    c=0
    for i in range(0,len(str)):
        if(str[i]=='1'):
            c=c+1
    return c
if __name__=="__main__":
    n=int(input())
    res=[]
    for i in range(0,n+1):
        #print(str(bin(i))[2::])
        c=Numberofones(str(bin(i))[2::])
        res.append(c)
    print(res)
