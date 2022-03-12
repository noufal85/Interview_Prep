def fib_rec(n):
    #base
    if n == 0 or n== 1:
        return n
    
    # recursive 
    else:
        return fib_rec(n-1) + fib_rec(n-2)


def fib_iter(n):
    '''
    same solution for 
    '''

    a = 0
    b = 0

    for i in range(n):

        a,b = b ,a+b

    return a