def fibonnaci_recursion(n):
    result = []
    if n == 1 or n == 2:
        return 1
    elif n >= 3:
        return fibonnaci_recursion(n-1) + fibonnaci_recursion(n-2)


print(fibonnaci_recursion(3))
