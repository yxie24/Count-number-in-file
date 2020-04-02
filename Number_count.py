import re
file = open ('week_2_assignment.txt')
sum = 0
for line in file:
    line=line.rstrip()
    count = re.findall('[0-9]+',line)
    for number in count:
        sum = sum + int(number)
print(sum)
