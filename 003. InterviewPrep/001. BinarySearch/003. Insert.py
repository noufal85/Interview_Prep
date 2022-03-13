def searchInsert( nums,target):
    left , right = 0 , len(nums)-1
    print('{},{}'.format(left , right))
    if target <= nums[0]:
        return left
    if target == nums[-1 ]:
        return right
    if target > nums[-1]:
        return right +1
    while left <= right :
        middle = left + (right+left)//2
        if middle == 0 : return 1
        print('middle is {}'.format(nums[middle]))
        #1,2,3,4,5
        if target > nums[middle-1] and target < nums[middle]:                
            return middle
        if target > nums[middle] and target < nums[middle+1]:
            return middle+1
        if target == nums[left]:
            return left
        if target == nums[middle] :
            return middle
        if target > nums[middle]:
            left = left +1 
        if target < nums[middle]:
            right  = middle -1