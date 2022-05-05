# What is the value of the first triangle number to have over five hundred divisors?

def next_triang(n):
    sum_ = 0
    for x in range(n+1):
        sum_ += x
    return sum_

def find_divisors(n):
    tri = next_triang(n)
    n_factors = 1
    i = 2
    div = 0
    while tri != 1:
        while (tri % i == 0):   
#            print(tri, " is divisible by: ", i)
            tri /= i
            div += 1
        i+=1
        n_factors = n_factors * (div+1)
        div = 0
#    print("triangular value: ", tri," has ", n_factors, "divisors.")
    return n_factors

def main():
    i = 1 
    while True:
        if(find_divisors(i) > 500):
            print("SOLUTION: ", next_triang(i))
            break
        else:
            i+=1

if __name__ == '__main__':
    main()
        
