# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# Evaluate the sum of all the amicable numbers under 10000.

import math

def sum_proper_divisors(n):
    total = 1  #every number is divisible by 1
    for m in range (2,int(math.sqrt(n) + 1)):
        if n % m == 0:
            total += m
            y = n // m #remainder
            if y > m:
                total += y
    return total

def amicable(x, y):
    if(sum_proper_divisors(y) == x and x < 10000 and y < 10000):
#        print(x, "is amicable with ", y)
        return True
#    print("not amicable!", x, " and ", y)
    return False

def main():
    div_check = sum_proper_divisors(220)
    print(div_check)
    x = 1
    amicable_total = 0   
    for i in range(1,10000):
         sum_div_i = sum_proper_divisors(i)
         if amicable(i,sum_div_i) and i != sum_div_i:
             amicable_total += i
    print("sum of all amicables", amicable_total)

if __name__ == "__main__":
    main()
    
