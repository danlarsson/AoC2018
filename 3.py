# https://adventofcode.com/2018/day/3
import re

def main():
    with open('3.data', 'r') as f:
        list_of_clames = f.read().splitlines()
    f.close()
        
    fabric = [[0] * 1000 for i in range(1000)] # Create a 1000x1000 array.
    overlap = 0

    for i in list_of_clames:
        clame = decode(i) # ID, Start X, Start Y, Len X, Len Y

        for x in range(int(clame[1]), int(clame[1]) + int(clame[3])):
            for y in range(int(clame[2]), int(clame[2]) + int(clame[4])):
                if fabric[x][y] == 0:
                    fabric[x][y] = clame[0]
                elif fabric[x][y] == -1:
                    pass
                else:
                    fabric[x][y] = -1
                    overlap += 1

    print('Inches2 that overlap: %i' % overlap) 

    
    ############################
    # Part 2
    
    for i in list_of_clames:
        clame = decode(i) # ID, Start X, Start Y, Len X, Len Y
        no_overlap = True
        
        for x in range(int(clame[1]), int(clame[1]) + int(clame[3])):
            for y in range(int(clame[2]), int(clame[2]) + int(clame[4])):
                if fabric[x][y] != clame[0]:
                    no_overlap = False

        if no_overlap:
            print('Area %i is not overlaping anyting else' % int(clame[0]))



def decode(claims):
    '''TG for a good manual :)'''
    p = re.compile(r'\d+')
    return p.findall(claims)


if __name__ == '__main__':
    main()
    
