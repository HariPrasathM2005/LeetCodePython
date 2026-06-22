from collections import Counter
if __name__=="__main__":
    text="nlaebolko"
    c=Counter(text)
    tot=0
    while(c['b']>0):
        if(c['b']>=1 and c['a']>=1 and c['l']>=2 and c['o']>=2 and c['n']>=1):
            tot=tot+1
            c['b']=c['b']-1
            c['a']=c['a']-1
            c['l']=c['l']-2
            c['o']=c['o']-2
            c['n']=c['n']-1
        else:
            c['b']=0
    print(tot)
