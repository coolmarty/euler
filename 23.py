# A perfect number is a number for which
# the sum of its proper divisors is exactly equal to the number.

# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.

# this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math



def get_divisors(num):
    if num == 1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while(divisor < n):
        if(num % divisor == 0):
            total += divisor
            total += num //divisor
        divisor += 1
    if n**2 == num:
        total += n
    return total


def abundance(num):
    if get_divisors(num) > num:
        return True
    return False

     
def main():
#    print(abundance(28))
    sum_all_a = []
    for x in range(1,28123):
        if abundance(x):

#            print("abundant found!")
            sum_all_a.append(x)
            
    sums = [0]*28124
    
    for x in range (0, len(sum_all_a)):
        for y in range (x, len(sum_all_a)):
                sumOf2AbundantNums = sum_all_a[x]+sum_all_a[y]
                if (sumOf2AbundantNums<= 28123):
                    if (sums[sumOf2AbundantNums] == 0):
                        sums[sumOf2AbundantNums] = sumOf2AbundantNums
    final_total = 0
    for x in range (1,len(sums)):
        if (sums[x] == 0):
            final_total += x
    print("final total: ", final_total)

if __name__ == '__main__':
    main()
        
