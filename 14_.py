# Which starting number, under one million, produces the longest chain?

def find_collatz(n, list_):
    if n == 1:
        return list_
    if n % 2 == 0:
        n /= 2
    else:
        n = 3*n + 1
    list_.append(n)
    return find_collatz(n,list_)

def main():
    max_list = []
    for x in range(1,1000000):
#       print("finding...", x)
        l = find_collatz(x,[x])
        if len(l) > len(max_list):
            max_list = l
    print("LONGEST COLLATZ CHAIN: ", max_list[0])
if __name__ == '__main__':
    main()
    
