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


# TYPE CONVERSION
# int()
# float()
# str()
# bool()

# Input from the user always comes as a string in python
textScore = input("Text score: ")

print(type(textScore)) #string
print(type(int(textScore)))  #int

examScore = 55

totalScore = int(textScore) + examScore
print(totalScore)


# Bool(Falsy Values)
# ""
# 0
# None

print(bool(""))
print(bool(0))
print(bool(None))



# Exercise 1 — Identify and work with number types
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


# ANSWER
# 1. Print each variable.
print("Failed Logins = ", failedLogins)
print("Response Time = ", responseTime)
print("Signal Value = ", signalValue)

# 2. Identify which variable contains an integer, a floating-point number, and a complex number.
# failedLogins = 12 #integer
# responseTime = 2.75 #floating point number
# signalValue = 4 + 3j #complex number

# 3. Use Python's `type()` function to display the type of each variable.
print("")
print("Failed Logins: ", type(failedLogins))
print("Response Time: ", type(responseTime))
print("Signal Value: ", type(signalValue))

# 4. Create three additional variables of your own: one integer, one float, and one complex number. Print their values and types.
score = 80
height = 8.7
formula = 6 + 3j

print("score = ", score)
print("height = ", height)
print("formula = ", formula)

print("")
print("score: ", type(score))
print("height: ", type(height))
print("height: ", type(height))





# Exercise 2 — Calculate incident statistics
# A monitoring system records the following information:
failedAttempts = 18
successfulAttempts = 6
minutesMonitored = 4

# Your tasks:
# 1. Calculate the total number of attempts.
# 2. Calculate the difference between failed and successful attempts.
# 3. Calculate the total number of attempts per minute.
# 4. Calculate the whole-number quotient when total attempts are divided by `minutesMonitored`.
# 5. Calculate the remainder.
# 6. Print each result with a meaningful message using f-strings.


# ANSWER
# 1. Calculate the total number of attempts.
totalAttempts = failedAttempts + successfulAttempts

# 2. Calculate the difference between failed and successful attempts.
differenceBetweenAttempts = failedAttempts - successfulAttempts

# 3. Calculate the total number of attempts per minute.
attemptsPerMinute = totalAttempts / minutesMonitored

# 4. Calculate the whole-number quotient when total attempts are divided by `minutesMonitored`
wholeNumberQuotient = totalAttempts // minutesMonitored

# 5. Calculate the remainder.
remainder = totalAttempts % minutesMonitored

# 6. Print each result with a meaningful message using f-strings.
incidentStatisticsReport = f"""
==== INCIDENT STATISTICS REPOORT ====
Total Attempts: {totalAttempts}
Difference Between Attempts: {differenceBetweenAttempts}
Total Attempts Per Minute: {attemptsPerMinute}
Whole Number Qoutient Of Attempts: {wholeNumberQuotient}
Remainder: {remainder}
"""

print(incidentStatisticsReport)



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

# ANSWER
# 1. Calculate `baseScore ** multiplier`.
firstResult = baseScore ** multiplier

# 2. Calculate `baseScore * multiplier + bonusScore`.
secondResult = baseScore * multiplier + bonusScore

# 3. Calculate `baseScore * (multiplier + bonusScore)`.
thirdResult = baseScore * (multiplier + bonusScore)

# 4. Calculate `2 ** 3 ** 2`.
fourthResult = 2 ** 3 ** 2

# 5. Print all four results using f-strings.
calculationResults = f"""
=== CALCULATION RESULTS ===
1. {firstResult}
2. {secondResult}
3. {thirdResult}
4. {fourthResult}
"""
print(calculationResults)

# 6. Explain why the second and third calculations produce different results.
# In the second calculation * took precedence over + and vise versa in the third calculation


# Exercise 4 — Update incident counters
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

# ANSWER
# 1. Add 5 using `+=`.
failedLogins += 5
print(failedLogins)

# 2. Subtract 3 using `-=`.
failedLogins -= 3
print(failedLogins)

# 3. Multiply the current value by 2 using `*=`.
failedLogins *= 2
print(failedLogins)

# 4. Divide the current value by 4 using `/=`.
failedLogins /= 4
print(failedLogins)

# 6. Explain how augmented assignment changes the variable's value.
# it takes this form variable = variable (operation) number

# Challenge: What type of value does `failedLogins` hold after the `/=` operation? Explain why.
print(type(failedLogins))
# Float



# Exercise 5 — Mini SOC calculation challenge
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

# Bonus questions:

# - Why might `/` produce a float even when both operands are integers?
# - What is the difference between `x = x + 3` and `x += 3`?
# - If `failedLogins` is increased by 3, does `totalAttempts` automatically update if you calculated it before the increase? Explain.


# ANSWER
# 1. Calculates the total login attempts using `+`.
totalLoginAttemts = failedLogins + successfulLogins

# 2. Calculates the difference between failed and successful logins using `-`.
differenceBetweenLoginAttempts = failedLogins - successfulLogins

# 3. Calculates the average number of total login attempts per hour using `/`.
averageLoginAttempt = totalLoginAttemts / monitoringHours

# 4. Calculates the whole-number quotient and remainder when total attempts are divided by `monitoringHours`, using `//` and `%`.
qoutient = totalLoginAttemts // monitoringHours

remainder = totalLoginAttemts % monitoringHours

# 5. Calculates `riskBase ** riskExponent`.
risk = riskBase ** riskExponent

# 6. Increases `failedLogins` by 3 using `+=`, then prints the updated value.
failedLogins += 3
print("Updated Failed Logins: ", failedLogins)


# 7. Prints a neatly formatted report using f-strings.
incidentReport = f"""
===== LOGIN INVESTIGATION =====
Failed Logins: {failedLogins}
Successful Logins: {successfulLogins}
Total Attempts: {totalLoginAttemts}
Difference: {differenceBetweenLoginAttempts}
Average Attempts Per Hour: {averageLoginAttempt}
Whole-Number Quotient: {qoutient}
Remainder: {remainder}
Risk Calculation: {risk}
===============================
"""
print(incidentReport)


# Bonus questions:

# - Why might `/` produce a float even when both operands are integers?
# ANSWER: Because / is designed to perforn true division or mathematical division , hence always return a float

# - What is the difference between `x = x + 3` and `x += 3`?
# ANSWER: they are the same, the only difference is the operator been used, = and +=

# - If `failedLogins` is increased by 3, does `totalAttempts` automatically update if you calculated it before the increase? Explain.
# ANSWER: NO. because the program runs from top to down



# Exercise 6 — Rounding numerical values
# A security monitoring system records the following response times:
responseTime1 = 3.4567
responseTime2 = 7.8912
responseTime3 = 12.5555

# Your tasks:
# 1. Print each response time rounded to 2 decimal places using round().
# 2. Round each response time to the nearest whole number.
# 3. Store each rounded result in a separate variable.
# 4. Print the original and rounded values using f-strings.

# Reasoning questions:
# - What does round(responseTime1, 2) mean?
# - What happens if you use round(responseTime1) without specifying the number of decimal places?

# ANSWER
# 1. Print each response time rounded to 2 decimal places.
print( round(responseTime1, 2))

print(round(responseTime2, 2))

print(round(responseTime3, 2))

# 2. Round each response time to the nearest whole number.
# 3. Store each rounded result in a separate variable.
result1 = round(responseTime1)

result2 = round(responseTime2)

result3 = round(responseTime3)

# 4. Print the original and rounded values using f-strings.
roundingReport = f"""
Original Response Time 1: {responseTime1}
Rounded Value:{result1}

Original Response Time 2 {responseTime2}
Rounded Value:{result2}

Original Response Time 3: {responseTime3}
Rounded Value:{result3}
"""

print(roundingReport)


# Reasoning questions:
# - What does round(responseTime1, 2) mean?
# ANSWER: It round responseTime1 to 2 decimal places

# - What happens if you use round(responseTime1) without specifying the number of decimal places
# ANSWER: Python will by default set it to 0 and run it to the nearest whole number




# # Exercise 7 — Working with absolute values
# # An analyst compares expected and actual server response times.
# expectedTime = 5.5
# actualTime = 8.2

# # Your tasks:
# # 1. Calculate the difference between the two values.
# # 2. Use abs() to obtain the absolute difference.
# # 3. Print both the original difference and the absolute difference.
# # 4. Repeat the exercise with expectedTime = 10 and actualTime = 6.

# # Reasoning questions:
# # - What does abs() do?
# # - Why might absolute differences be useful when comparing security metrics?



# # Exercise 8 — Using the math module
# # Python's math module provides additional mathematical functions.

# # First, import the module:
# # import math

# # Given:
# number1 = 4.3
# number2 = 9.8
# number3 = 25
# number4 = 3

# # Your tasks:
# # 1. Use math.ceil() on number1.
# # 2. Use math.floor() on number2.
# # 3. Use math.isqrt() on number3.
# # 4. Use math.exp() on number4.
# # 5. Print all results using descriptive messages.
# # 6. Use type() to check the data type of each result.

# # Reasoning questions:
# # - What is the difference between math.ceil() and math.floor()?
# # - What does math.isqrt(25) return?
# # - What mathematical operation does math.exp(3) perform?


# # Exercise 9 — Type conversion
# # Consider these values:
# loginAttempts = "15"
# responseTime = "4.75"
# accountBalance = 250
# isCompromised = 1

# # Your tasks:
# # 1. Convert loginAttempts into an integer using int().
# # 2. Convert responseTime into a float using float().
# # 3. Convert accountBalance into a string using str().
# # 4. Convert isCompromised into a Boolean using bool().
# # 5. Print each converted value.
# # 6. Use type() to verify the data type of each converted variable.

# # Reasoning questions:
# # - Why can't you directly perform arithmetic addition between "15" and 5?
# # - What happens if you try int("hello")?



# # Exercise 10 — Accepting user input
# # Create a simple program that asks a SOC analyst for information.

# # Your program should:
# # 1. Ask for the analyst's name using input().
# # 2. Ask for the number of failed login attempts.
# # 3. Ask for the average response time.
# # 4. Convert the number of failed login attempts into an integer.
# # 5. Convert the average response time into a float.
# # 6. Print all collected information using an f-string.
# # 7. Use type() to display the data types of the converted values.
# # Example interaction:
# # Enter analyst name: Godsway
# # Enter failed login attempts: 12
# # Enter average response time: 4.75

# # ===== ANALYST REPORT =====
# # Analyst: Godsway
# # Failed Logins: 12
# # Average Response Time: 4.75

# # Important: Remember that input() returns a string, even when the user enters a number.


# # Exercise 11 — Understanding Boolean values
# # Python treats certain values as falsy and most other values as truthy.

# # Create these variables:
# value1 = ""
# value2 = "SOC Analyst"
# value3 = 0
# value4 = 25
# value5 = None
# value6 = 3.14
# value7 = False
# value8 = True

# # Your tasks:
# # 1. Convert each value into a Boolean using bool().
# # 2. Print each original value and its Boolean result.
# # 3. Use type() to identify the original data type.
# # 4. Identify all the falsy values.
# # 5. Identify all the truthy values.

# # Reasoning questions:
# # - Why is bool("0") different from bool(0)?
# # - Is an empty string falsy?
# # - Is a negative number truthy?



# # Exercise 12 — User input and Boolean conversion
# # Imagine you're building a basic security monitoring configuration tool.

# # Your program should:
# # 1. Ask the analyst to enter a username.
# # 2. Ask whether monitoring should be enabled, requesting 1 for yes and 0 for no.
# # 3. Store both inputs in variables.
# # 4. Convert the monitoring input into an integer.
# # 5. Convert that integer into a Boolean using bool().
# # 6. Print the username, monitoring status, and their data types.
# # Example:
# # Enter username: adminRoot
# # Enable monitoring? Enter 1 for yes or 0 for no: 1

# # ===== MONITORING CONFIGURATION =====
# # Username: adminRoot
# # Monitoring Enabled: True
# # Username Type: <class 'str'>
# # Monitoring Type: <class 'bool'>

# # Reasoning question: Why is converting "1" directly to a Boolean different from converting 1 to a Boolean?



# # Exercise 13 — Mathematical security calculations
# # A security analyst is calculating a simple risk score.

# # Given:
# failedLogins = 17
# successfulLogins = 5
# riskMultiplier = 2.75

# # Your tasks:
# # 1. Calculate the difference between failed and successful logins.
# # 2. Use abs() to obtain the absolute difference.
# # 3. Multiply the absolute difference by riskMultiplier.
# # 4. Round the resulting risk score to 2 decimal places.
# # 5. Use math.ceil() to round the risk score upward.
# # 6. Use math.floor() to round the risk score downward.
# # 7. Print all results using f-strings.
# # 8. Use type() to inspect the calculated values.

# # Bonus: What happens to the final score if riskMultiplier is changed to 3.5?



# # Exercise 14 — Predict before execution
# # Study the following code carefully.

# # Before running it, predict the output and data type of every expression.
# # import math
# value1 = 12.75
# value2 = -8
# value3 = "25"
# value4 = ""
# value5 = 0
# value6 = None
# print(round(value1))
# print(round(value1, 1))
# print(abs(value2))
# print(int(value3))
# print(float(value3))
# print(bool(value4))
# print(bool(value5))
# print(bool(value6))
# print(math.ceil(4.2))
# print(math.floor(4.9))
# print(math.isqrt(36))
# print(math.exp(1))

# # Your tasks:
# # 1. Predict every output.
# # 2. Identify the data type returned by each function.
# # 3. Execute the code and compare your predictions.
# # 4. Explain any differences between your predictions and the actual results.
# # Important: math.exp(1) produces a floating-point approximation of Euler's number, approximately 2.71828.



# # Exercise 14 — Mini SOC analyst command-line tool
# # This exercise combines everything you've studied.

# # Imagine you're developing a basic command-line tool that collects incident information and calculates a simple risk score.

# # Your program should:

# # Part A: Collect information

# # Use input() to request:
# # - Analyst name
# # - Username under investigation
# # - Number of failed login attempts
# # - Number of successful login attempts
# # - Risk multiplier
# # Part B: Convert the data

# # Convert:
# # - Failed login attempts into an integer.
# # - Successful login attempts into an integer.
# # - Risk multiplier into a float.
# # Use type() to verify the converted values.

# # Part C: Perform calculations
# # 1. Calculate the total login attempts.
# # 2. Calculate the difference between failed and successful logins.
# # 3. Calculate the absolute difference using abs().
# # 4. Multiply the absolute difference by the risk multiplier.
# # 5. Round the risk score to 2 decimal places.
# # 6. Use math.ceil() to obtain the rounded-up risk score.
# # 7. Use math.floor() to obtain the rounded-down risk score.
# # Part D: Boolean checks

# # Create a Boolean variable indicating whether the username is empty.

# # Create another Boolean variable indicating whether failed login attempts are greater than zero, using the values you've collected.

# # Part E: Generate the report

# # Print a neatly formatted report using an f-string.

# # Your report should follow this structure:
# # ========== SOC INCIDENT REPORT ==========
# # Analyst: [analyst name]
# # Username: [username]

# # Failed Logins: [value]
# # Successful Logins: [value]
# # Total Attempts: [value]

# # Absolute Difference: [value]
# # Risk Score: [value]
# # Rounded Up Score: [value]
# # Rounded Down Score: [value]

# # Username Is Empty: [True/False]
# # Failed Login Activity: [True/False]
# # =========================================


# # Bonus questions:
# # 1. What happens if an analyst enters "ten" instead of 10 for failed login attempts?
# # 2. Why must you convert the input before performing arithmetic?
# # 3. What would happen if the analyst entered an empty username?
# # 4. Why might math.ceil() be useful when rounding a risk score to a whole number?