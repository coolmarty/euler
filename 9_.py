# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc

def is_pythagorean(a,b,c):
    return(a**2 + b**2 == c**2)

def main():
#   print(is_pythagorean(3,4,5))
#   print(is_pythagorean(3,4,6))
    for i in range(3,1000):
        for j in range(4,1000):
            for k in range(5,1000):
                if(is_pythagorean(i,j,k)):
                   print("triplet: ",i, ", ", j, ", ", k, " sum: ", i+j+k)
                   if(i+j+k == 1000):
                       print("SOLUTION: ", i*j*k)
                       return
                   
if __name__ == '__main__':
    main()
