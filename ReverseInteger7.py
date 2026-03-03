def Reverse(x):
    if(x>=0):
        if(x>pow(2,31)-1):
            return 0
        x=str(x)
        rev_x=x[::-1]
        #print(rev_x)
        rev_x=int(rev_x)
        #print(rev_x)
        if(rev_x>pow(2,31)-1):
            return 0
        return rev_x
    else:
        if(x<pow(-2,31)):
            return 0
        y=str(x)
        y=y[1::]
        #print(y)
        rev_y=int(y[::-1])
        #print(rev_y)
        rev_y=0-rev_y
        if(rev_y<pow(-2,31)):
            return 0
        #print(rev_y)
        return rev_y
num=Reverse(-123)
print(num)
