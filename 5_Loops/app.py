# FOR LOOP
for number in range(2, 10, 2):
    print("Attempt", number, number * ".")


# Multiples of 3
for multiplesOfThree in range(3, 31, 3):
    print(multiplesOfThree)


for number in range(1, 50):
    if (number % 3 == 0) and (number % 5 == 0):
        print(number)