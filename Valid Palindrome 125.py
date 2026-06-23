if __name__=="__main__":
    s = "A man, a plan, a canal: Panama"
    S=""
    s=s.lower()
    for i in s:
        if(i.isalnum()):
            S=S+i
    if(S[::]==S[::-1]):
        print(True)
    else:
        print(False)
