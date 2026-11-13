# COMPARISON OPERATORS
print(10 > 3)
print(10 >= 3)
print(10 < 3)
print(10 <= 3)
print(10 == 3)
print(10 != "10")
print("hey" == "HEY")

print(ord('h'))
print(ord('H'))


# CONDITIONAL STATEMENTS
temperature = 15

if temperature > 30:
    print("Its warm")
    print("Drink more water")
elif temperature > 20:
    print("Its nice")
else:
    print("Its cold")


print("We good!")




# Check student eligibility
age = 16

if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"


print(message)


# TERNARY OPERATOR
message = "Eligible" if age >= 18 else "Not eligible"
print(message)



# LOGICAL OPERATORS
# and
# or
# not

# LOAN ELIGIBILITY DETECTOR
highIncome = True
goodCredit = True
student = False

if (highIncome and goodCredit) and not student:
    print("Eligible for loan")
else:
    print("Not eligiblre for loan")



# implementing the same logic with the ternary operator
eligibility = "Eligible for loan" if ((highIncome and goodCredit) and not student) else "Not eligible for loan"
print(eligibility)

