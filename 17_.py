# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

def how_many_letters(n):
    if n == 1 or n == 2 or n == 6 or n == 10:
        return 3
    if n == 0 or n == 4 or n == 5 or n == 9:
        return 4
    if n == 3 or n == 7 or n == 8 or n == 40 or n == 50 or n == 60:
        return 5
    if n == 11 or n == 12 or n == 20 or n == 30 or n == 80 or n == 90:
        return 6
    if n == 70 or n == 15:
        return 7
    if n == 13 or n == 18:
        return 8
    if n < 20:
        return how_many_letters(n%10) + 4 #teen
    if n < 40:
        return 6 + how_many_letters(n % 10) #twenty or thirty
    if n < 70:
        return 5 + how_many_letters(n % 10) #forty, fifty, or sixty
    if n < 80:
        return 7 + how_many_letters(n % 10) #seventy
    if n < 100:
        return 6 + how_many_letters(n % 10) #eighty ninety
    if n % 100 == 0:
        return how_many_letters(n/100) + 7
    hundred_and = 10
    return how_many_letters(n//100) + hundred_and + how_many_letters(n % 100)

def main():
    sum_ = 0
#    print("EXPECTED: 25 ACTUAL: ", how_many_letters(867))
    for x in range(1, 1000):
#        print("summing, ", x)
        sum_ += how_many_letters(x)
    sum_ += 11                              #one thousand
    print("SUM OF ALL LETTERS: ", sum_)

if __name__ == '__main__':
    main()
