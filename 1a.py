
f = open('1.data', 'r')

freq = 0
for i in f:
    freq = freq + int(i.strip())
    

print(freq)

    

