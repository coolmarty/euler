# What is the index of the first term in the Fibonacci sequence
# to contain 1000 digits?

def fibonacci(a, b, n):
    if n == 1:
        return a
    return fib(a+b, a, n-1)

def how_many_digits(n):
    strnum = str(n)
    return len(strnum)

def main():
#    print(how_many_digits(fibonacci(12)))
    a = 1
    b = 0
    n = 1
    while how_many_digits(a) != 1000:
        a, b = a+b, a
        n+=1
    print(n)
        
if __name__ == '__main__':
    main()
