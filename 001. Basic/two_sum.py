# https://leetcode.com/problem-list/top-100-liked-questions/
def two_sum(nums, target):
    seen = {}
    out = []

    seen = set()
    for i in range(len(nums)):
        print(nums[i],seen)
        diff = target - nums[i]
        print(f'diff: {diff}')
        if diff in seen:
            return [nums[i],diff]
        else:
            seen.add(nums[i])

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    target = 10

    print(two_sum(nums,target))

