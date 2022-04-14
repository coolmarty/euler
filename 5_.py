#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divisible(n, div):
    if(div == 1):
        return True
    if(n % div != 0):
        return False
    else:
        return is_divisible(n,div-1)

def main():
    n = 100
    while(is_divisible(n,20) != True):
#       print("NOT DIVISIBLE:", n)
        n+=1   
    print("DIVISIBLE BY 1-20:", n)

if __name__ == '__main__':
    main()
