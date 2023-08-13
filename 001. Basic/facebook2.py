def monotonic(arr):
    inc = 0
    dec = 0

    for i in range(1,len(arr)):
        if arr[i-1] < arr[i]:
            inc += 1
        else:
            dec += 1

    if inc == len(arr) -1 or dec == len(arr) - 1:
        return True

    return False

def monotonic_arr(A):
    x= []
    y = []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse= True)
    if x == A or y ==A:
        return True
    else:
        return False

if __name__ == "__main__":
    mon1 = [1,2,3,4,5,6,4]
    print(monotonic_arr(mon1))

def replace_None(lst):
    for i in range(1,len(lst)):
        if lst[i]:
            pass
        else:
            lst[i] = lst[i-1]
    return lst

def nth_highest(inp,n):
    b = list(sorted(set(inp.values()), reverse = True))
    o = {k for k,v in inp.item() if v == b[n-1]}
    return min(o)

def flatten(dic , out = None):

    pass

if __name__ == "__main__":
    mon1 = [1,2,3,4,5,6,4]
    print(monotonic(mon1))
    none1 = [1,2,3,4,None,6]
    print(replace_None(none1))
    dic = {1:1, 2:2, 3:3, 4:4, 5:5}
    print(nth_highest(dic,2))
