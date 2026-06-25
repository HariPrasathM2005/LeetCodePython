def generate_subsets(index, arr, current, result):
    result.append(current[:])  # store copy
    print("Current:",current)

    for i in range(index, len(arr)):
        current.append(arr[i])                 # include element
        generate_subsets(i + 1, arr, current, result)
        current.pop()                          # backtrack
    


arr = [1,2,3]
result = []

generate_subsets(0, arr, [], result)

# Print subsets
'''print(len(result))
n=1
c=0
res=0
for i in result:
    c=0
    for num in i:
        if(n==num):
            c=c+1
    if(c>len(i)//2):
        print(i)
        print("len:",len(i)//2," count:",c)
        res=res+1
print("result:",res)'''
ans=0
n=0
for i in arr:
    n=n+1
target=4
for i in range(0,n):
    count=0
    for j in range(i,n):
        if(arr[j]==target):
            count=count+1
        len=j-i+1
        if(count>len//2):
            ans=ans+1
print(ans)
