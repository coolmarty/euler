#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

from math import sqrt

def find_primes(n):
    primes = [2]
    for x in range(3,n,2):
        is_prime = True
        for y in primes:
            if y >= (sqrt(x)+1):
                break
            if x % y == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
#            print(x, "is prime")
    return sum(primes)

def main():
    summation_two_mil = find_primes(2000000)
    print("SOLUTION: ", summation_two_mil)

if __name__ == '__main__':
    main()
