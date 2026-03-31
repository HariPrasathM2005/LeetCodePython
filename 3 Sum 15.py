def Triplet(arr, target):
    n = len(arr)
    res=set()
    Res=[]
    for i in range(n - 2):
        st = set()

        for j in range(i + 1, n):
            second = target - arr[i] - arr[j]

            if second in st:
                sub=tuple(sorted([arr[i], second, arr[j]]))
                res.add(sub)
            
            st.add(arr[j])

    Res=[i for i in res]
    return Res

def unique(res,n):
    if n in res:
        return res
    else:
        res.append(n)
        return res
     
if __name__=="__main__":
    arr=[1,2,-1,0,0,1]
    target=1
    res=Triplet(arr,target)
    print(res)
