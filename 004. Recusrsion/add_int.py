def sum_func(n):
    #base case 
    if len(str(n)) == 1:
        return n

    else:

        return n%10 +sum_func(n//10)



if __name__ == "__main__":
    print(sum_func(12345))

