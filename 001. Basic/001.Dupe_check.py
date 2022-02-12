# simplest 
def dupe_check(string):
    return len(set(string)) == len(string)

# using hash

def dup_check_hash(string):
    hash_map = []*128
    for s in string:
        hash_map[ord(s)] += 1
        if hash_map[ord(s)] > 1:
            return False
    return True




if __name__ == '__main__':
    print(dupe_check('abcd'))
    print(ord('a'))