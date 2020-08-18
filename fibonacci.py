
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib2( n):
    """
    :type n: int
    :rtype: int
    """
    a,b=0,1
    for i in range (n):
        a,b=b,a+b
    return a


if __name__ == "__main__":
    #print(fib(10))
    print(fib2(45))
