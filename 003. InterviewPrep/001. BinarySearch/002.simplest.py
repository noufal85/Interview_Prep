
from numpy import left_shift


def n_solution(nums,target):
    for i in range(len(nums)):
        #print(nums[i])
        if nums[i] == target:
            return i
    return 0

def Ologn(nums,target):
    left , right = 0 , len(nums) - 1
    while left <= right :
        #print('left is {} and rght is {}'.format(left, right))
        middle = left + (right -left) //2
        #print('middle is {}'.format(middle))
        #print('num in middle - {}'.format(nums[middle]))
        if nums[middle] == target:
            return middle
        if target < nums[middle]:
            right = middle - 1
            #print('new right is {}'.format(right))
        else:
            left = middle +1
            #print('new left is {}'.format(left))
    return -1
        



if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    target =4
    print('solution from first one - {}'.format(n_solution(nums,target)))
    print('Solution from second one - {}'.format(Ologn(nums,target)))

