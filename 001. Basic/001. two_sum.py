# https://leetcode.com/problem-list/top-100-liked-questions/
def two_sum(nums, target):
    seen = {}
    out = []

    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [i,seen[diff]]
        else:
            seen[nums[i]] = i

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    target = 10

    print(two_sum(nums,target))

