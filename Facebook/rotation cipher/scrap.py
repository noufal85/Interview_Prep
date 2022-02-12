

def hashexample(string, rotation):
    rotated = []
    hashL = {}
    for i,j in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(1,27)):
        print(i,j)
        hashL[i] = j
    #print(hashL)
    for s in string:
        if s.isnumeric():
            pass
        else:
            NOUF
        rotated.append(s)
    return rotated

if __name__ == "__main__":
    string = 'abcd'
    print(hashexample(string,1))
