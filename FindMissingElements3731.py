def MissingElements(num):
    #print(max(num))
    diff=max(num)-min(num)
    #print(diff)
    new=[]
    for i in range(min(num),max(num)+1):
        new.append(i)
    #print(new)
    set1=set(new)
    set2=set(num)
    set3=set1-set2
    #print(set3)
    res=list(set3)
    print(res)
MissingElements([5,1])
