# Find the value of d < 1000 for which 1/d contains
# the longest recurring cycle in its decimal fraction part.
from decimal import *
getcontext().prec = 10000

def long_reciprocal(denom, num = 1):
    remainders = []
    rems = None
    while rems not in remainders:
        remainders.append(rems)
        num *= 10
        rems = num % denom
    remainders.pop(0)
    return len(remainders)
        


def main():
    max_length = 0
    for x in range(1,1000):
        length = long_reciprocal(x)
        if length > max_length:
            max_length = x
    print("ANSWER: ", max_length)
    return 0

if __name__ == '__main__':
    main()
