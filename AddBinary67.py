def addBinary(b1,b2):
    b3=""
    c=0
    a=b1[::-1]
    b=b2[::-1]
    if(len(a)<len(b)):
        pad=len(b)-len(a)
        ch=''
        for i in range(0,pad):
            ch=ch+'0'
        a=a+ch
    elif(len(b)<len(a)):
        pad=len(a)-len(b)
        ch=''
        for i in range(0,pad):
            ch=ch+'0'
        b=b+ch
    #print(a)
    #print(b)
    for i in range(0,max(len(a),len(b))):
        sum=int(a[i])+int(b[i])+c
        #print(sum)
        c=0
        if(sum>=2):
            b3=str(sum%2)+b3
            c=1
        else:
            b3=str(sum)+b3
    if(c==1):
        b3='1'+b3
    return b3

b3=""
b3=addBinary("1","11")
print(b3)
