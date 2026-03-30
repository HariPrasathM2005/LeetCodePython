
def addDigits(num):
    Sum=0
    Rep=True
    n=num
    while Rep:
        while(n>0):
            m=n%10
            Sum=Sum+m
            n=int(n/10)
        n=Sum
        #print("Sum:",Sum)
        if(len(str(n))>1):
            n=Sum
            Sum=0
        elif(len(str(n))==1):
            Rep=False
    return Sum
if __name__=="__main__":
    num=int(input())
    res=addDigits(num)
    print(res)
