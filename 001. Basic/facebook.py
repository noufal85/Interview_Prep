def freqPrint(string):
    counter = {}

    for i in string:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    out = ''
    for ch in counter:
        out = out + str(counter[ch])+ ch
    return out

def not_common(sent1,sent2):
    l1 = sent1.split()
    l2 = sent2.split()

    def count(li):
        dic = {}
        for l in li:
            if dic.get(l):
                dic[l] += 1
            else:
                dic[l]= 1
        return dic

    count1 = count(l1)
    count2 = count(l2)

    for k in count1:
        if k in count2:
            count2[k] -=1
    
    for k in count2:
        if k in count1:
            count1[k] -=1
    print(count1)
    print(count2)

def balanced(s):
    stack = []

    openings = list('({[')
    closings = list(')}]')
    pairs = ['{}','()','[]']

    for c in s:
        if c in openings:
            stack.append(c)
        if c in closings:
            try:
                last_ = stack.pop()
            except:
                return False
            pair = '{}{}'.format(last_,c)
            if pair not in pairs:
                return False
    if stack:
        return False

    return True


    #print(openings)




if __name__ == "__main__":
    string1 = 'i am back'
    print(freqPrint(string1))
    sent1 = 'hi hello how are you cow'
    sent2 = 'hi hello how are you nice rice'
    print(not_common(sent1, sent2))
    good = '(hello how are you )'
    good2 = '(hello how are you)( what'
    print(balanced(good))
    print(balanced(good2))
