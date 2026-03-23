if __name__=="__main__":
    arr=["H","E","L","L","O"]
    print(arr)
    for i in range(0,int(len(arr)/2)):
        arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
    print(arr)
