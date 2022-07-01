
# 費伯納西數列 (fibonacci sequence)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    # Given a number and show it's fibonacci value
    n = 5
    print(fib(n))