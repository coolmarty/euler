# Find the sum of the digits in the number 100!
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def find_sum_digits(num, sum_):
    str_num = str(num)
    if len(str_num) == 1:
        return sum_ + int(str_num[0])
    sum_+= int(str_num[0])
    return find_sum_digits(int(str_num[1:]), sum_)

def main():
#    print("factorial 10: " , factorial(10))
#    print("summed digits: " , find_sum_digits(factorial(10),0))
    print("factorial 100: " , factorial(100))
    print("summed digits: " , find_sum_digits(factorial(100),0))
    return 0

if __name__ == '__main__':
    main()
    
