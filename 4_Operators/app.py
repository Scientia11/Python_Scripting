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



# Exercise 1 — Compare security metrics
# A monitoring system records the following information:
failedLogins = 8
loginThreshold = 5
responseTime = 3.5
maximumResponseTime = 5.0
userAge = 25
minimumAge = 18

# Your tasks:
# 1. Check whether failedLogins is greater than loginThreshold.
# 2. Check whether responseTime is less than maximumResponseTime.
# 3. Check whether userAge is equal to minimumAge.
# 4. Check whether userAge is not equal to minimumAge.
# 5. Check whether failedLogins is less than or equal to loginThreshold.
# 6. Print each comparison result with a meaningful message using f-strings.

# Reasoning questions:
# - What is the difference between = and ==?
# - What does != mean?
# - What data type do comparison operators return?

# ANSWER
# 1. Check whether failedLogins is greater than loginThreshold.
loginThresholdExceeded = failedLogins > loginThreshold

# 2. Check whether responseTime is less than maximumResponseTime.
responseTimeWihinRange = responseTime < maximumResponseTime

# 3. Check whether userAge is equal to minimumAge.
userAgeIsMinimumAge = userAge == minimumAge

# 4. Check whether userAge is not equal to minimumAge.
userAgeNotMinimumAge = userAge != minimumAge

# 5. Check whether failedLogins is less than or equal to loginThreshold.
loginThresholdReached = failedLogins <= loginThreshold

# 6. Print each comparison result with a meaningful message using f-strings.
result = f"""
=== SECURITY METRICS COMPARISON REPORT ===
Login Threshold Exceeded: {loginThresholdExceeded}
Response Time Within Range: {responseTimeWihinRange}
User Age Is Minimum: {userAgeIsMinimumAge}
User Age Is Not Minimum: {userAgeNotMinimumAge}
Login Threshold Reached: {loginThresholdReached}
"""

print(result)


# Reasoning questions:
# - What is the difference between = and ==?
# = is use to assign values and == is used to compare values


# - What does != mean?
# Not Equal To

# - What data type do comparison operators return?
# Boolean





# Exercise 2 — Build a basic login security checker
# You are developing a basic login security checker.

# Given:
userName = "adminRoot"
passwordCorrect = True

# Your tasks:
# 1. Check whether passwordCorrect is True.
# 2. If it is true, print "Login successful. Welcome!".
# 3. Otherwise, print "Login failed. Incorrect password.".
# 4. Change passwordCorrect to False and execute the program again.
# 5. Observe how the output changes.

# Reasoning question: What happens when the condition following if evaluates to False?

# ANSWER
print("Password is correct:", passwordCorrect)
print("")


if passwordCorrect: 
    print("Login successful. Welcome!")
else: 
    print("Login failed. Incorrect password.")


# Using the ternary operator
LoginMessage = "Login successful. Welcome!" if passwordCorrect else "Login failed. Incorrect password."

print(LoginMessage)

# Reasoning question: What happens when the condition following if evaluates to False?
# Python will skip the if block to execute the else block





# Exercise 3 — Classify security alerts
# A SOC monitoring system classifies alerts based on the number of failed login attempts.

# Use the following thresholds:
# Failed login attempts	Alert classification
# 0–2	Low
# 3–5	Medium
# 6–10	High
# Above 10	Critical

# Given:
failedLogins = 15

# Your tasks:
# 1. Use if, elif, and else to classify the alert.
# 2. Print the appropriate classification.
# 3. Test your program with these values: 1, 4, 8, and 15.
# 4. Make sure every possible value falls into the correct category.

# Reasoning questions:
# - Why do we use elif instead of writing several independent if statements?
# - What happens if none of the conditions in an if/elif chain is true and there is no else?

# ANSWER
failedLoginAttemptsStatus = "Low"

if failedLogins < 3:
    failedLoginAttemptsStatus
elif failedLogins < 6:
    failedLoginAttemptsStatus = "Medium"
elif failedLogins < 11:
    failedLoginAttemptsStatus = "High"
else:
    failedLoginAttemptsStatus = "Critical"


print("Failed Attempts:", failedLogins)
print("Attempts Status: ", failedLoginAttemptsStatus)

# Reasoning questions:
# - Why do we use elif instead of writing several independent if statements?
# elif only runs when the if and elif statements before it evaluates to false

# - What happens if none of the conditions in an if/elif chain is true and there is no else?
# Nothing will be returned





# Exercise 4 — Evaluate multiple security conditions
# Intermediate
#  and, or, not

# A security system determines whether an account should be flagged for investigation.

# Given:
# failedLogins = 7accountLocked = FalsesuspiciousIP = TrueknownDevice = False



# Your tasks:
# 1. Check whether the account has more than 5 failed login attempts and is locked.
# 2. Check whether the IP address is suspicious or the account is locked.
# 3. Use not to check whether the device is not recognized (knownDevice is false).
# 4. Check whether the account should be investigated when the IP is suspicious and the device is not recognized.
# 5. Print all results using f-strings.
# Bonus: Change accountLocked to True and suspiciousIP to False. Observe how the results change.

# Reasoning questions:
# - When does and return True?
# - When does or return True?
# - What does not do to a Boolean value?
# Exercise 5 — Mini SOC access-control system
# Challenge
#  All today's concepts

# You are building a basic access-control decision system for a security operations environment.

# Given:
# userName = "analyst01"accountActive = TruepasswordCorrect = TruefailedLogins = 2isAdmin = False



# Your program must perform the following checks.

# Part A — Access decision

# A user can log in only when:
# - The account is active.
# - The password is correct.
# - Failed login attempts are fewer than 5.
# Use logical operators to evaluate these conditions.

# If all conditions are satisfied, print:

# Access Granted

# Otherwise, print:

# Access Denied

# Part B — Role classification

# Use if, elif, and else:
# - If isAdmin is True, print "Administrator Access".
# - Otherwise, print "Standard Analyst Access".
# Part C — Security warning

# Use a conditional statement to check failed login attempts:
# - 0–2: "Normal Activity"
# - 3–4: "Warning: Login attempts approaching threshold"
# - 5 or more: "Account Lockout Recommended"
# Part D — Ternary operator

# Create a variable called accessStatus using the ternary operator.

# It should store:
# - "Granted" if access is allowed.
# - "Denied" otherwise.
# Part E — Generate a report

# Use an f-string to print:
# ===== ACCESS CONTROL REPORT =====
# Username: analyst01
# Account Active: True
# Password Correct: True
# Failed Logins: 2
# Access Status: Granted
# User Role: Standard Analyst Access
# Security Assessment: Normal Activity
# =================================


# Bonus challenges:
# 1. What happens if accountActive is False?
# 2. What happens if failedLogins is exactly 5?
# 3. Can the ternary operator replace a simple if/else statement? Explain.
# 4. Why is it important to check multiple conditions before granting access?
