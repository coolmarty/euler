# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# Evaluate the sum of all the amicable numbers under 10000.

def sum_proper_divisors(n):
    m = 1
    divisors = []
    while m <= n:
        if n % m == 0:
            divisors.append(m)
        m+=1
    return sum(divisors)

def amicable(x, y):
    amicable_arr = []
    if(sum_proper_divisors(x) == y):
        print(x, "is amicable with ", y)
        return True
#    print("not amicable!", x, " and ", y)
    return False

def main():
#    div_array = sum_proper_divisors(220)
    x = 10000
    y = 1
    amicables = []
    while(x > 0):
        while (y < x):
            if(amicable(x,y)):
                amicables.append(x)
            y+=1
        x-=1
    print("sum of all amicables", sum(amicables))

if __name__ == "__main__":
    main()
    
