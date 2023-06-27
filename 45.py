# Triangle n(n+1)/2
# Pentagonal n(3n-1)/2
# Hexagonal n(2n-1)

# T285 = P165 = H143, find the next triangle that is also penta and hex
from math import sqrt

def triangular(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

def is_triangular(n):
    t = sqrt(8 * (n) + 1)
    return t % 1 == 0
        
def is_pentagonal(n):
    p = (1 + sqrt(24*n + 1))/6
    return p % 1 == 0
    
def main():
    i = 144
    while True:
        h = hexagonal(i)
        if is_pentagonal(h) and is_triangular(h):
            print(h, "is the answer")
            return h
        i+=1
    
if __name__ == '__main__':
    main()
