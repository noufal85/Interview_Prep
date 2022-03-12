
def sorted_squares(nums):
    ans = [0] * len(nums)
    left = 0 
    right = len(nums) -1 
    print(' right and left to start with are {} & {}'.format(right, left ))
    if len(nums) == 1:
        ans = [nums[0]*nums[0]]
        return ans
    for i in range(1,len(nums)):
        print('values of i = {} , right = {}, left = {}'.format(i, right , left))
        l = nums[left] * nums[left]
        r = nums[right]  * nums[right]
        if  l <= r:
            ans[-i] = nums[right]*nums[right]
            right -= 1
        else:
            ans[-i] = nums[left]*nums[left]
            left += 1
        print(ans)

    return ans



    return ans

if __name__ == "__main__":
    nums = [-2,-1,0,1,2,3,4]
    print(sorted_squares(nums))
    print(nums[-2])