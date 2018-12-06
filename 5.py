# https://adventofcode.com/2018/day/5

import string

def main():
    with open('5.data', 'r') as f:
        list_of = f.read()
        f.close()

    a = "dabAcCaCBAcCcaDA"
    a = list_of.strip()
    l = len(a)
    print('Length of data: %i' % l)
    print('Length of crunched data: %i' % len(take_away_dups(a)))

    for l in string.ascii_lowercase:
        in_data = a
        in_data = in_data.replace(l, '')
        in_data = in_data.replace(l.upper(), '')
        out_data = take_away_dups(in_data)
        length = len(out_data)
        print('%s %i' % (l, length))


def take_away_dups(in_data):
    repeat = True
    while repeat:
        length = len(in_data)
        for l in string.ascii_lowercase:
            u = l.upper()
            in_data = in_data.replace(l+u, '')
            in_data = in_data.replace(u+l, '')
        if length == len(in_data):
            repeat = False

    return in_data


if __name__ == '__main__':
    main()

