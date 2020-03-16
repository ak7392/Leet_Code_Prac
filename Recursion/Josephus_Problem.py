
# recusrion problem


def Josephus_recursion(n, k):
    if n == 1:
        return 1
    else:
        # The position returned by
        # josephus(n - 1, k) is adjusted
        # because the recursive call
        # josephus(n - 1, k) considers
        # the original position
        # k%n + 1 as position 1
        return (Josephus_recursion(n-1, k) + k-1) % n+1


print(Josephus_recursion(14, 2))
