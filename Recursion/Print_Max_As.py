
def findoptimal(N):

    if N < 6:
        return N

    maxi = 0

    for b in range(N-3, 0, -1):

        curr_i = (N-b-1) * findoptimal(b)
        if curr_i > maxi:
            maxi = curr_i

    return maxi


if __name__ == '__main__':

    # for the rest of the array we will
    # rely on the previous
    # entries to compute new ones
    for n in range(1, 21):
        print('Maximum Number of As with ', n,
              'keystrokes is ', findoptimal(n))
