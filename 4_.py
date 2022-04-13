#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    strnum = str(n)
    if (len(strnum) < 2):
        return True
    return (strnum[0] == strnum[-1] and is_palindrome(strnum[1:-1]))

def main():
#    print(is_palindrome(67))
#    print(is_palindrome(909))
    greatest = 0
    for i in range(99, 999):
        for j in range(99,999):
            if(is_palindrome(i*j) and i*j > greatest):
                greatest = i*j
    print("greatest palindrome: ", greatest)
if __name__ == '__main__':
  main()
