def containsDuplicates(nums,k):
    Res=False
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if(i!=j and nums[i]==nums[j]):
                if(i>=j):
                    if(i-j<=k):
                        return True
                elif(j>=i):
                    if(j-i<=k):
                        return True
    return Res
def Contains(nums,k):
    Res=False
    i=0
    num={}
    arr={}
    sub=[]
    #dist={}
    while(i<len(nums)):
        if nums[i] not in num:
            sub=[]
            num[nums[i]]=1
            sub.append(i)
            arr[nums[i]]=sub
            #dist[nums[i]]=0

        else:
            num[nums[i]]=num[nums[i]]+1
            sub=arr[nums[i]]
            sub.append(i)
            sub=sorted(sub)
            arr[nums[i]]=sub
            ind=0
            while(ind<len(sub)-1):
                if(abs(sub[ind]-sub[ind+1])<=k):
                    #print(abs(sub[ind]-sub[ind+1]))
                    #Res= True
                    return True
                ind=ind+1

            val=sub[1]-sub[0]
            #dist[nums[i]]=val
        i=i+1
    #print(num)
    #print(arr)

    #print(dist)
    return Res
if __name__=="__main__":
    #arr=[1,2,3,1,2,3,4]
    arr=[1,2,3,1]
    #arr=[1,0,1,1]
    k=3
    #res=containsDuplicates(arr,k)
    res=Contains(arr,k)
    print("Res:",res)
