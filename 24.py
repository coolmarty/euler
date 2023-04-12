# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
from math import factorial

def init_lexic(n):
    option_array = []
    while(n >= 0):
        option_array.append(n)
        n-=1
    option_array.sort()
    return option_array

def find_lexic(n,s):
    if len(s) == 1:
        return s
    quotient, remainder = divmod(n,factorial(len(s)-1))
    return s[quotient] + find_lexic(remainder, s[:quotient] + s[quotient+1:])

def main():
#    sas = find_lexic(9)
#   print(sas)
#    print(find_lexic(3, '012'))
    print(find_lexic(999999,'0123456789'))
    
if __name__ == '__main__':
    main()

# referenced https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-024-solution/ for ideation
