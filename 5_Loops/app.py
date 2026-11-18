# FOR LOOP
for number in range(2, 10, 2):
    print("Attempt", number, number * ".")


# Multiples of 3
for multiplesOfThree in range(3, 31, 3):
    print(multiplesOfThree)


# numbers divisible by 3 and 5 between 1-50
for number in range(1, 50):
    if (number % 3 == 0) and (number % 5 == 0):
        print(number)


# Even vumbers between 1-51
for evenNumber in range(2, 51, 2):
    print(evenNumber)



# FOR ELSE
successful = False

for number in range(3):
   print("Attempt", number + 1)
   if successful:
      print("Successful")
      break
else: 
   print("Unsuccessful login, 3 failed attempts!")
#    the else block run if the for loop complete without an early termination(break)