# How many such routes are there through a 20×20 grid?

def factorial(n):
    for x in range(1,n):
        n*=x
    return n

def main():
#    print("FACTORIAL TEN: ", factorial(10))
    left_right = 20
    up_down = 20
    binomial_top = factorial(left_right+up_down)
    binomial_bottom = factorial(left_right)*factorial(up_down)
    print(binomial_top/binomial_bottom, " PATHWAYS.")

if __name__ == '__main__':
    main()
