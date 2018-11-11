# https://adventofcode.com/2018/day/2

def main():
    with open('2.data', 'r') as f:
        list_of_boxes = f.read().splitlines()

    # Part 1
    nr_of_two = 0
    nr_of_three = 0
        
    for i in list_of_boxes:
        two, three = contains(i)
        if two:
            nr_of_two += 1
        if three:
            nr_of_three += 1

    print('Part1. Number of two %i, number of three %i and the summ: %i' % (nr_of_two, nr_of_three, nr_of_two * nr_of_three))
    print
    
    ###############################
    # Part 2
    
    for i in list_of_boxes:
        for n in list_of_boxes:
            the_one = compair_to_strings(i, n)
            if the_one:
                print('Part2. The one code: %s' % the_one)
                exit()
    

    
def compair_to_strings(string1, string2):
    if len(string1) != len(string2):
        print('The strings has to have the same length %s | %s' % (string1, string2))

    differs = 0
    common_letters = ''
    for i in range(0, len(string1)):
        if string1[i] != string2[i]:
            differs += 1
        else:
            common_letters += string1[i]

    if differs == 1:
        return common_letters


        
    
def contains(string):
    two = False
    three = False

    for i in string:
        if string.count(i) == 3:
            three = True
        elif string.count(i) == 2:
            two = True

    return(two, three)
            

if __name__ == '__main__':
    main()
