def flatten(nums,out =None):
    if not out:
        out = []

    for n in nums:
        if type(n) == list:
            flatten(n,out)
        else:
            out.append(n)

    return out

if __name__ == "__main__":
    one = [3,[1,2,3,4,5]]
    print(flatten(one))