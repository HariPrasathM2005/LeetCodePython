def BinarytoInt(binary):
    pow=0
    num=0
    for i in range(len(binary)-1,-1,-1):
        #print(binary[i])
        if(binary[i]=='1'):
            num=num+(2**pow)
        pow=pow+1
    return num
def Complement(num):
    Binary=bin(num)
    Binary=int(Binary[2:])
    Binary_str=str(Binary)
    Inverted=0
    for i in str(Binary_str):
        if(i=='0'):
            Inverted=Inverted*10+1
        else:
            Inverted=Inverted*10
    Inverted_bin=BinarytoInt(str(Inverted))
    return Inverted_bin
if __name__=="__main__":
    num=1
    val=Complement(num)
    print(val)
