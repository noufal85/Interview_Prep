 
def maxSubArray(arr):
    maxSum = currentSum = arr[0]
    for n in arr[1:]:
        print('n is {}'.format(n))
        print('current = {} , max = {}'.format(currentSum, maxSum))
        currentSum = max(currentSum+n, n)
        maxSum = max(currentSum, maxSum)
    return maxSum

if __name__ == "__main__":
    arr = [1,2,3,-1,-2,-3]
    print(maxSubArray(arr))

