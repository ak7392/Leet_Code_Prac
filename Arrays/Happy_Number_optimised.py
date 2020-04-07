def numSquareSum(n):
    squareSum = 0
    while(n):
        squareSum += (n % 10) * (n % 10)
        n = int(n / 10)
    return squareSum

# method return true if
# n is Happy number


def isHappynumber(n):

    # initialize slow
    # and fast by n
    slow = n
    fast = n
    while(True):

        # move slow number
        # by one iteration
        slow = numSquareSum(slow)

        # move fast number
        # by two iteration
        fast = numSquareSum(numSquareSum(fast))
        if(slow != fast):
            continue
        else:
            break

    # if both number meet at 1,
    # then return true
    return (slow == 1)


# Driver Code
n = 13
if (isHappynumber(n)):
    print(n, "is a Happy number")
else:
    print(n, "is not a Happy number")

# This code is contributed by mits
