if __name__=="__main__":
    nums1=[4,9,5]
    nums2=[9,4,9,8,4]
    s1=set(nums1)
    s2=set(nums2)
    res=s1.intersection(s2)
    print(list(res))
