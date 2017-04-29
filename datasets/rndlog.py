import csv
import random

data = [[], []]
alphabetdata = []
n = int(input())

#form alphabet
first = 0
last = 0
final = list()
for i in range(96, 123):
    if chr(i) == 'a':
        first = i
    elif chr(i) == 'z':
        last = i
        break

j = 0
for i in range(first, last + 1):
    alphabetdata.append(chr(i))
    j += 1
    if j>=n: break #check condition

#randomize alphabet
for k in range(n):
    pw = random.choice(alphabetdata)
    k += 1
    data[0].append(pw)
print(data)

#randomize case id
m = random.randrange(1, n+1)
print(m)
new1 = list(range(1,m+1))+[random.randint(1, m) for i in range(n-m)]
    # p = random.randrange(1, n) #easy random
    # j += 1
data[1].append(new1)

#write log in csv file
with open('random_log.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file,  delimiter=',')
    header = ['act_name','case id']
    csv_writer.writerow(header)
    for p1,p2 in zip(data[0],data[1][0]):
        csv_writer.writerow([p1,p2])
