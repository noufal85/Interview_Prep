def nsum(n):

    # base case 
    if n==0:
        return 0

    else:
        return n+nsum(n-1)

if __name__ == "__main__":
    print(nsum(10))