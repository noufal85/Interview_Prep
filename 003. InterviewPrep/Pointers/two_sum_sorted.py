

def two_sum_sorted(nums,target):

    seen ={}

    for i in range(len(nums)):

        diff = target - nums[i]

        if diff in seen:
            return [seen[diff]+1,i+1]
        else:
            seen[nums[i]]=i

    

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    print(two_sum_sorted(nums, target))
