months_list = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_sunday(day):
    return(day % 7 == 0)

def main():
    sunday_firsts = 0
    current_day = 1
    for year in range(1901,2000):
        for m in range(len(months_list)):           
            current_day += months_list[m]
            if year % 4 == 0 and m == 1:
                current_day += 1
            if(is_sunday(current_day)):
               sunday_firsts += 1
    print("SUNDAY FIRSTS: ", sunday_firsts)

if __name__ == '__main__':
    main()
