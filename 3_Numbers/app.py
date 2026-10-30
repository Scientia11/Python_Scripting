# TYPES OF NUMBERS IN PYTHON
# Integers
age = 16

# Floating point numbers
price = 20.16

# Complex numbers
eqn = 2 + 19j # a + bi where a and b are numbers and i is an imaginary number


# ARITHMETIC OPERATORS IN PYTHON
print(10 + 3) #addtion
print(10 - 3) #subtraction
print(10 * 3) #multiplication
print(10 / 3) #division
print(10 // 3) #return the integer part of a division
print(10 % 3) #remainder of division
print(10 ** 3) #exponent

score = 70
score += 10 #augmented assignment operator
print(score)



# WORKING WITH NUMBERS
import math

print(round(3.7))
print(abs(-5.6))

print(math.ceil(3.2))
print(math.floor(7.8))
print(math.factorial(10))
print(math.exp(2))
print(math.isqrt(20))
print(math.tan(10))





## Exercise 1 — Identify and work with number types
# A SOC analyst records these values:

failedLogins = 12
responseTime = 2.75
signalValue = 4 + 3j

# Your tasks:
# 1. Print each variable.
# 2. Identify which variable contains an integer, a floating-point number, and a complex number.
# 3. Use Python's `type()` function to display the type of each variable.
# 4. Create three additional variables of your own: one integer, one float, and one complex number. Print their values and types.

# Think about it: Why is `12` an integer while `12.0` is a float, even though they represent the same numerical quantity?



## Exercise 2 — Calculate incident statistics
# A monitoring system records the following information:
failedAttempts = 18
successfulAttempts = 6
minutesMonitored = 4

# Your tasks:
# 1. Calculate the total number of attempts using `+`.
# 2. Calculate the difference between failed and successful attempts using `-`.
# 3. Calculate the total number of attempts per minute using `/`.
# 4. Calculate the whole-number quotient when total attempts are divided by `minutesMonitored` using `//`.
# 5. Calculate the remainder using `%`.
# 6. Print each result with a meaningful message using f-strings.

# Think about it: If 24 attempts occur over 5 minutes, what results would `/`, `//`, and `%` produce when you divide 24 by 5?



## Exercise 3 — Understand exponentiation and operator precedence
# A security tool assigns a simple score based on repeated events.

baseScore = 3
multiplier = 2
bonusScore = 5

# Your tasks:
# 1. Calculate `baseScore ** multiplier`.
# 2. Calculate `baseScore * multiplier + bonusScore`.
# 3. Calculate `baseScore * (multiplier + bonusScore)`.
# 4. Calculate `2 ** 3 ** 2`.
# 5. Print all four results using f-strings.
# 6. Explain why the second and third calculations produce different results.

# Important: Predict the results before running your code. Python's operator precedence determines which operation happens first, and exponentiation has a special evaluation order.



## Exercise 4 — Update incident counters
# A SOC analyst is tracking failed logins during an investigation.

failedLogins = 10

# Your tasks:
# 1. Add 5 using `+=`.
# 2. Subtract 3 using `-=`.
# 3. Multiply the current value by 2 using `*=`.
# 4. Divide the current value by 4 using `/=`.
# 5. Print the value after each operation.
# 6. Explain how augmented assignment changes the variable's value.

# Challenge: What type of value does `failedLogins` hold after the `/=` operation? Explain why.




## Exercise 5 — Mini SOC calculation challenge
# A monitoring system records activity from a potentially compromised account.

failedLogins = 27
successfulLogins = 8
monitoringHours = 5
riskBase = 2
riskExponent = 3

# Write a Python script that:
# 1. Calculates the total login attempts using `+`.
# 2. Calculates the difference between failed and successful logins using `-`.
# 3. Calculates the average number of total login attempts per hour using `/`.
# 4. Calculates the whole-number quotient and remainder when total attempts are divided by `monitoringHours`, using `//` and `%`.
# 5. Calculates `riskBase ** riskExponent`.
# 6. Increases `failedLogins` by 3 using `+=`, then prints the updated value.
# 7. Prints a neatly formatted report using f-strings.

# Use this structure:

# ===== LOGIN INVESTIGATION =====
# Failed Logins: [updated value]
# Successful Logins: 8
# Total Attempts: [calculated value]
# Difference: [calculated value]
# Average Attempts Per Hour: [calculated value]
# Whole-Number Quotient: [calculated value]
# Remainder: [calculated value]
# Risk Calculation: [calculated value]
# ===============================

# Bonus questions:

# - Why might `/` produce a float even when both operands are integers?
# - What is the difference between `x = x + 3` and `x += 3`?
# - If `failedLogins` is increased by 3, does `totalAttempts` automatically update if you calculated it before the increase? Explain.
