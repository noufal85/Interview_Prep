def mergeSorted(s1,s2):
    l1 = len(s1)
    l2 = len(s2)

    L = max(l1,l2)
    out = []
    i = 0
    j= 0
    while i< l1 and j<l2:
        if s1[i] >= s2[j]:
            out.append(s2[j])
            j += 1
        else:
            out.append(s1[i])
            i += 1
    #print(i,j)
    #print(range(i,l1))
    if i < l1:
        for i in range(i,l1):
            #print(s1[i])
            out.append(s1[i])

    if j < l2:
        for j in range(j,l2):
            out.append(s2[j])

    return out


if __name__ == "__main__":
    s1 = [1,3,5,7,9,10,11]
    s2 = [2,4,6,8]

    print(mergeSorted(s1,s2))


