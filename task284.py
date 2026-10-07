maximum = 0
count = 0

x = int(input())

while x != 0:
    if x > maximum:
        maximum = x
        count = 1
    elif x == maximum:
        count = count + 1

    x = int(input())

print(count)