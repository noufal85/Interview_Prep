def summary_range(nums):
    out = []
    x, y = 0,0
    x = nums[0]
    l = len(nums)
    i = 0

    while i<l-1:
        if nums[i+1] > nums[i]+1:
            out.append('{} => {}'.format(x,nums[i]))
            x = nums[i+1]
        i += 1
    out.append('{} => {}'.format(x,nums[-1]))
        

        
    return out

        
if __name__ == "__main__":
    nums1 = [1,2,3,4,8,9,10]
    print(summary_range(nums1))

    