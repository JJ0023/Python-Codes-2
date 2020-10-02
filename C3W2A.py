import re
handler = open("Real.txt")
sum=0
for line in handler:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    for i in y:
        sum = sum + int(i)
print(sum)
print("changes by neha")
