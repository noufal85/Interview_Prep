def mostCommon(lst):
    return max(set(lst), key=lst.count)

def mostCommon2(lst):
    freq = {}

    for item in lst:
        if item in freq:
            freq[item] +=1
        else:
            freq[item] =1 
    return max(freq, key = freq.get)


def replaceNone(lst):
    out = []
    for i in range(len(lst)):
        if lst[i]:
            out.append(lst[i])
        else:
            out.append(lst[i-1])
    return out

def getNthvalueKey(dic,n):
    val = list(dic.values())
    val.sort(reverse=True)
    #print(val)
    nthVal= val[n-1]
    keys = []

    for key in dic:
        if dic[key] == nthVal:
            keys.append(key)
    return max(keys)

def commonWords(list1, list2):
    return list(set(list1).intersection(list2))

def flaten_list(lst,out = None):
    if not out:
        out = []
    for n in lst:
        if not type(n) == list:
            out.append(n)
        else:
            flaten_list(n,out)
    return out

        
    


if __name__ == "__main__":
    lst1 = [1,2,3,4,5,5,5,5,6]
    print(mostCommon(lst1))
    print(mostCommon2(lst1))
    lst2 = [1,2,3,None,4,5,6]
    print(replaceNone(lst2))
    dic = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:8}
    print(getNthvalueKey(dic,3))
    list1 = [1,2,3,4]
    list2 = [4,5,6,7]
    print(commonWords(list1, list2))

    nested_ = [1,2,3,[4,5,6,[7,8,9]]]
    print(flaten_list(flaten_list(nested_)))