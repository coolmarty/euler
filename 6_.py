# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares(n, sum_):
    if(n == 1):
        print("summing squares complete: ", sum_ + 1)
        return sum_ + 1
#    print("adding:", n*n)
    return sum_squares(n-1,sum_+n*n)

def square_sums(n,sum_):
    if(n == 1):
        print("squaring sums complete: ", (sum_+1)*(sum_+1))
        return (sum_+1)*(sum_+1)
#    print("adding: ", n)
    return square_sums(n-1,sum_+n)

def main():
    
    sums_squared = sum_squares(100,0)
    squares_summed = square_sums(100,0)
    print("sums squared minus squared sums: ", squares_summed - sums_squared)
    return
    
if __name__ == '__main__':
    main()
