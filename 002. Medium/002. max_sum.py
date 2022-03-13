
def max_sum(nums):
    if len(nums) == 0 : 
        return 0
    if len(nums)== 1:
        return nums[0]
    maxSum = currentSum = nums[0]

    for n in nums[1:]:
        #print('number is {}'.format(n))
        #print('now \n current sum is {} \n max sum is {}'.format(currentSum, maxSum))
        currentSum = max(currentSum+n , n)
        #print('current sum is-{}'.format(currentSum))
        maxSum = max(currentSum, maxSum)
        #print('Max Sum is {}'.format(maxSum))


    return maxSum


if __name__ == "__main__":
    nums=[1,2,3,46,-50,50]

    print(max_sum(nums))