#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

def find_next_prime(n):
    primes = []
    while len(primes) <= 10001:
        is_prime = True
        for i in range(2,n-1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
       #     print(n, "is prime")
        n+=1
    return primes[10000]

def main():
    ten_thousand_and_first = find_next_prime(2)
    print("10,001th prime: ",ten_thousand_and_first)

if __name__ == '__main__':
    main()
