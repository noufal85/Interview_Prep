def validP(string):
    stack = []
    opening = set('{([')
    matching = ['()','{}','[]']
    print(opening)
    for p in string:
        print(p)
        if p in opening:
            stack.append(p)
        else:
            last_ = stack.pop()
            comp = '{}{}'.format(last_,p)
            print(comp)
            if comp not in matching:
                return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    s1 = '({}[)'
    print(validP(s1))