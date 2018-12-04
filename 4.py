# https://adventofcode.com/2018/day/4
import re

a=[]
a.append('[1518-11-01 23:58] Guard #99 begins shift')
a.append('[1518-11-02 00:40] falls asleep')
a.append('[1518-11-02 00:50] wakes up')
a.append('[1518-11-02 00:55] falls asleep')
a.append('[1518-11-02 00:58] wakes up')
a.append('[1518-11-03 00:05] Guard #10 begins shift')
a.append('[1518-11-02 00:25] falls asleep')
a.append('[1518-11-02 00:32] wakes up')
a.append('[1518-11-03 00:05] Guard #11 begins shift')

roster = [[0] * 60 for i in range(5000)] # Create a 2000x60 array.

def main():
    guard_list = set() # Just a uniqe list of guards
    
    with open('4sorted.data', 'r') as f:
        list_of = f.read().splitlines()
    f.close()

    for i in list_of:
        minute = int(i[15:17])
        data = i[19:]
        if 'Guard' in data:
            guard_id = int(get_nr(data))
            guard_list.add(guard_id)
        elif 'falls asleep' in data:
            sleep_time = minute
        elif 'wakes up' in data:
            wake_time = minute
            make_sleep(guard_id, sleep_time, wake_time)
        else:
            print('WTF! --> %s' % i)



    output_part1(guard_list)
    output_part2(guard_list)
    

def total_sleep_time(guard):
    sleep = 0
    for i in roster[guard]:
        sleep = sleep + i
    return sleep


def most_sleep_minute(guard):
    """ Returns the hour with most probability the guard sleeps """
    loop = 0
    hour = -1
    max_hour = -1
    for i in roster[guard]:
        if i > hour:
            hour = i
            max_hour = loop
        loop += 1
    return max_hour


def output_part1(guard_list):
    most_sleep = -1
    guard_id = -1
    for i in guard_list:
        tot_sleep = total_sleep_time(i)
        if tot_sleep > most_sleep:
            most_sleep = tot_sleep
            guard_id = i
        
    print 'The answer to part 1 is: %i' % (guard_id * most_sleep_minute(guard_id))


def output_part2(guard_list):
    max_h = -1
    guard = -1
    minute = -1
    for i in guard_list:
        loop = 0
        for n in roster[i]:
            if n > max_h:
                max_h = n
                guard = i
                minute = loop
            loop += 1
                
    print 'The answer to part 2 is: %i' % (guard * minute)


            
def make_sleep(guard, sleep, wake):
    """ Add 1 to the minutre a guard is sleeping """
    for i in range(sleep, wake):
        roster[guard][i] += 1

        
def get_nr(instr):
    p = re.compile(r'\d+')
    return p.findall(instr)[0]


if __name__ == '__main__':
    main()
    
                        
