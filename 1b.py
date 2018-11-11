# https://adventofcode.com/2018/day/1#part2
with open('1.data', 'r') as f:
    list_of_numbers = f.read().splitlines()

nr_of_loops = 1
freq = 0
found = []
while(1):
    print('Loop number: %i (%i)' % (nr_of_loops, freq))
    nr_of_loops += 1
    
    for i in list_of_numbers:
        freq = freq + int(i.strip())
        if freq in found:
            print(freq)
            exit()

        found.append(freq)
        
    

