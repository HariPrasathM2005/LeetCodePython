from collections import Counter
if __name__=="__main__":
    sentence=input()
    s=Counter(sentence)
    res=False
    c=0
    for i in s:
        if(i!=0 and i.isalpha()):
            c=c+1
    if(c==26):
        res=True
    else:
        res=False
    print(res)
