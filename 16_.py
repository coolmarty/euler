# What is the sum of the digits of the number 2^1000?

def find_sum_of_digits(n):
    num_string = str(n)
    sum_ = 0
    for x in range(0,len(num_string)):
        sum_ += int(num_string[x])
    return sum_

def main():
#    print("EXPECTED 18: ACTUAL: ", find_sum_of_digits(837))
    print("sum of 2^1000's digits: ", find_sum_of_digits(2**1000))
    
if __name__ == '__main__':
    main()

