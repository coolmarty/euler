#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def find_primes(n, prime_list):
    divisor = 2
    while n != 1:
        if(n % divisor == 0):
            prime_list.append(divisor)
            return find_primes(n/divisor,prime_list)
        else:
           divisor += 1
    print(prime_list)

def main():
    l = []
    find_primes(600851475143,l)
        
if __name__ == '__main__':
  main()
