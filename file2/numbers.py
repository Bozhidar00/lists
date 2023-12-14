number = []

for i in range(1, 8):
    number.append(i)
    print(number)

    if i%2 == 0:
        number.remove(i)
        print(number)
