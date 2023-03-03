# Using names.txt, a 46K text file containing over five-thousand first names,
# Begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.

# Ex. COLIN 3 + 15 +_12 + 9 + 14 = 53 x 938th position = 49714

# What is the total for all the name scores in the file?

def sum_name(name, position):
    name_total = 0
    name = name
    first_char = name[0]
    while True:      
        name_total += ord(first_char) - 64
        name = name[1:]
        if len(name) == 0:
            break
        first_char = name[0]
    return name_total * position   
    
         


def main():
    readfile = open("names.txt", encoding = 'utf-8', errors = 'ignore')

    names_array = readfile.readline().split(',')
#  print(names_array[0])
    names_array.sort()
#    for x in range (10):
#        print(names_array[x])
#    print(sum_name('COLIN',938))
    readfile.close()
    position = 1
    names_sum = 0
    for name in names_array:
        name = name.strip('"')
        print(name, "at position: ", position)
        names_sum += sum_name(name,position)
        print("summed: ", sum_name(name,position))
        position += 1
    print("sum of all names and positions: ", names_sum)    

if __name__ == '__main__':
    main()
