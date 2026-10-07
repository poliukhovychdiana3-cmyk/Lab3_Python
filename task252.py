count = 0

x = int(input())

while x != 0:
    if x % 2 == 0:
        count = count + 1

    x = int(input())

print(count)