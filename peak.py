nums=[1,2,3,4]

l, r = 0, len(nums)-1
while(l < r):
    m = (l+r)//2
    if nums[m] > nums[m+1]:
        r = m
    else :
        l = m+1
print(m)
