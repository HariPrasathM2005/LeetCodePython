def BinarytoInt(binary):
    pow=0
    num=0
    for i in range(len(binary)-1,-1,-1):
        #print(binary[i])
        if(binary[i]=='1'):
            num=num+(2**pow)
        pow=pow+1
    print(num)
    return num
def BinaryAddition(bin1,bin2):
    #print("res:",bin1)
    num1=BinarytoInt(str(bin1))
    num2=BinarytoInt(str(bin2))
    res=num1+num2
    #print("res:",res)
    res_bin=bin(res)
    res_str=str(res_bin[2:])
    print("res:",res_str)
    return res_str

def Complement(num):
    Binary=bin(num)
    Binary=int(Binary[2:])
    #print(Binary)
    Binary_str=str(Binary)
    padd_val=32-len(str(Binary))
    #print(padd_val)
    for i in range(0,padd_val):
        Binary_str='0'+Binary_str
    #print(Binary_str)
    Inverted=0
    for i in str(Binary_str):
        if(i=='0'):
            Inverted=Inverted*10+1
        else:
            Inverted=Inverted*10
    
    print("Inverted:",Inverted,"\n")
    complement_str=BinaryAddition(Inverted,1)
    print(complement_str)
    Inverted_bin=BinarytoInt(complement_str)
    return hex(Inverted_bin)

if __name__=="__main__":
    num=int(input())
    if(num<0): 
        res=Complement(-num)
        print(str(res[2:]))
    else:
        res=hex(num)
        print(res[2:])
