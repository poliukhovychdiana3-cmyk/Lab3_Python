n = int(input())

positive = 0
negative = 0
zero = 0

for i in range(n):
    number = int(input())

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print(positive, negative, zero)