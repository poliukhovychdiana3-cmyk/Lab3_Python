sum = 0
count = 0

x = int(input())

while x != 0:
    sum = sum + x
    count = count + 1
    x = int(input())

average = sum / count

print(average)