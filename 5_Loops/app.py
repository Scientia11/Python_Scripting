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


# NESTED LOOPS
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")



# ITERABLES
# range()
for number in range(3):
    print(number)


# strings
for letter in "Python":
    print(letter)


# list
marks = [58, 89, 75, 75]

for mark in marks:
    print(mark)


# WHILE LOOPS
command = ""

while command.lower() != "quit":
    command = input(">")
    print("ECHOE", command)


# Infinite Loops
# These are loops in which the test condition ia always true hence the loop run forever and should be avoided


# Practice Exercise: Write a program to print even numbers between 1 and 10
evenNumbersCount = 0

for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        evenNumbersCount += 1
else:
    print(f"We have {evenNumbersCount} even numbers")


# Exercise 1: Basic for loop
# A SOC analyst has a list of suspicious IP addresses:
suspiciousIPs = ["192.168.1.10",    "10.0.0.25",    "172.16.0.8",    "192.168.1.50",    "10.0.0.100"]

# Tasks:
# 1. Use a for loop to print each IP address.
# 2. Modify your loop to print each IP address alongside the message "Suspicious IP detected:".
# 3. Explain what happens when the loop processes each item.

# ANSWER
# 1. Use a for loop to print each IP address.
# 2. Modify your loop to print each IP address alongside the message "Suspicious IP detected:".
for IPAddress in suspiciousIPs:
    print(f"Suspicious IP detected: {IPAddress}")


# 3. Explain what happens when the loop processes each item.
# In each iteration, a suspicious IP in the suspiciousIP addreses array is set to IPAddress





# Exercise 2: Analysing failed login attempts
# A security log contains the following failed login attempts:
failedLogins = [3, 7, 2, 10, 5, 1, 8]

# Tasks:
# 1. Use a for loop to print each failed login count.
# 2. Print "High number of failed attempts" whenever the count is greater than or equal to 5.
# 3. Print "Normal activity" whenever the count is below 5.

# ANSWER
for loginCount in failedLogins:
    if loginCount >= 5:
        print(f"High number of failed attempts: {loginCount}")
    else: 
        print(f"Normal activity: {loginCount}")




# Exercise 3: Calculating total security alerts
# A SOC team recorded the following alerts during a shift:
alertCounts = [12, 8, 15, 6, 9]

# Tasks:
# 1. Create a variable called totalAlerts and initialise it to 0.
# 2. Use a for loop to add each alert count to totalAlerts.
# 3. Print the total number of alerts after the loop finishes.
# 4. Explain why totalAlerts must be initialised before the loop.

# ANSWER
totalAlerts = 0

for alert in alertCounts:
    totalAlerts += alert

print(f"Total Alerts: {totalAlerts}")

# 4. Explain why totalAlerts must be initialised before the loop.
# Because we are going to modify it to hold the result of the addition in the loop after each iteration




# Exercise 4: Understanding for...else
# A SOC analyst is searching for a particular suspicious IP address:
suspiciousIPs = ["192.168.1.10", "10.0.0.25", "172.16.0.8", "192.168.1.50"]
targetIP = "8.8.8.8"

# Tasks:
# 1. Use a for loop to search for targetIP.
# 2. If the IP is found, print "Target IP found!".
# 3. Use a for...else structure to print "Target IP not found!" if the loop completes without finding it.
# 4. Change targetIP to "8.8.8.8" and observe the output.
# Important: In Python, the else block of a for loop executes when the loop finishes normally without encountering a break.

# ANSWER
for IP in suspiciousIPs:
    if (IP == targetIP):
        print("Target IP found!")
        break
else:
    print("Target IP not found!")





# Exercise 5: Mini SOC investigation challenge
# You are investigating a list of login attempts:
loginAttempts = ["SUCCESS", "FAILED", "FAILED", "SUCCESS", "FAILED", "SUSPICIOUS"]

# Tasks:
# 1. Create two variables:
#    - successfulLogins = 0
#    - failedLogins = 0
# 2. Use a for loop to examine each login attempt.
# 3. If an attempt is "SUCCESS", increase successfulLogins by 1.
# 4. If an attempt is "FAILED", increase failedLogins by 1.
# 5. Use for...else to print "Investigation completed." after all attempts have been processed.
# 6. Print the total successful and failed login attempts.

# Bonus: Modify the investigation so that it searches for "SUSPICIOUS" in the list. If found, print "Suspicious activity detected!"; otherwise, use the loop's else block to print "No suspicious activity detected."


# ANSWER
successfulLogins = 0
failedLogins = 0
suspiciousActivity = "No suspicious activity detected."


for attempt in loginAttempts:
    if attempt == "SUCCESS":
        successfulLogins += 1
    elif attempt == "SUSPICIOUS":
        suspiciousActivity = "Suspicious activity detected!"
    else:
        failedLogins += 1
else:
    print(f"""
Investigation Completed.
Successful Logins: {successfulLogins}
Failed Logins: {failedLogins}
Suspicous Activity: {suspiciousActivity}
""")



# Exercise 6 — Network Port Enumeration
# A SOC analyst is investigating a host for potentially exposed network ports.
targetPorts = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3389]

# Tasks:
# 1. Use a for loop to examine every port.
# 2. Print ports that are commonly associated with remote access or file-sharing risks: 21, 22, 23, 445, and 3389.
# 3. Use range() to generate numbers from 1 to 10 and print their squares.
# 4. Modify the first task so that each port is printed with its position in the list, starting from 1.
# Challenge: Explain the difference between range(1, 10) and range(1, 11).

# ANSWER
print("Exposed Remote Acess or File Sharing Ports")
for port in range(0, 10):
    if targetPorts[port] == 21 or targetPorts[port] == 22 or targetPorts[port] == 23 or targetPorts[port] == 445 or targetPorts[port] == 3389:
        print(f"port: {targetPorts[port]}, positon: {port + 1}")


print("")

print("Square of numbers from 1-10")
for number in range(1, 11):
    print(number * number)

# Challenge: Explain the difference between range(1, 10) and range(1, 11).
# range(1, 10) starts from 1 and end at 9
# range(1, 11) starts from 1 and end at 




# Exercise 7 — Password Character Analysis
# You are analysing a suspicious password recovered during a security investigation.
password = "Admin@2026Secure"

# Tasks:
# 1. Use a for loop to examine every character in the password.
# 2. Count how many characters are digits (0–9).
# 3. Count how many characters are uppercase letters.
# 4. Count how many characters are lowercase letters.
# 5. Count how many characters are special characters (characters that are neither uppercase, lowercase nor digits).
# 6. Print a summary of your findings.
# Hint: You can use string methods such as .isdigit(), .isupper(), and .islower().

# Challenge: Use string slicing to extract the first five and last six characters of the password.

# ANSWER
digitsCount = 0
upperCaseCount = 0
lowerCaseCount = 0
specialCharCount = 0

for char in password:
    if char.isdigit():
          digitsCount += 1
    elif char.isupper():
          upperCaseCount += 1
    elif char.islower():
          lowerCaseCount += 1
    else:
          specialCharCount += 1



report = f"""
==== PASSWORD CHARACTER ANALYSIS ====
Digits: {digitsCount}
Uppercase: {upperCaseCount}
Lowercase: {lowerCaseCount}
Special Characters: {specialCharCount}
======================================
"""
print(report)


print("")

# Challenge: Use string slicing to extract the first five and last six characters of the password.
print("First five characters: ", password[0:5])
print("Last six characters: ",password[-6:len(password)])




# Exercise 8 — Nested Loops: Security Event Matrix
# A SOC analyst is monitoring three servers. Each server has recorded several failed login attempts.
serverLogs = [ [2, 5, 1, 7], [8, 3, 6, 2], [1, 4, 9, 5]]

# Tasks:
# 1. Use nested for loops to print every failed login count.
# 2. Print the values in a structured format, identifying each server and its individual attempt count.
# 3. Calculate the total failed login attempts across all servers.
# 4. Count how many individual login counts are greater than or equal to 5.
# 5. Identify which server recorded the highest individual failed login count.

# ANSWER
totalFailedAttempts = 0
loginLimitCount = 0
highestFaildCount = 0
highestFaildCountServer = ""

for serverLog in range(0, len(serverLogs)):
    print(f"SERVER {serverLog + 1} LOGS")

    for log in serverLogs[serverLog]:
            if (log >= 5):
                  loginLimitCount += 1

            print(log)

            totalFailedAttempts += log

            if (highestFaildCount < log):
                  highestFaildCountServer = f"Server {serverLog + 1}"
else: 
      print("Total failed attempts: ", totalFailedAttempts)
      print("Login Limit Count: ", loginLimitCount)
      print("Highest attempts count server: ", highestFaildCountServer)
    




# Exercise 9 — Nested Loops: IP Address Investigation
# Advanced
# You have two lists containing IP addresses from different security logs.
# internalIPs = [    "192.168.1.10",    "10.0.0.5",    "172.16.0.8",    "192.168.1.50"]suspiciousIPs = [    "10.0.0.5",    "8.8.8.8",    "192.168.1.50",    "45.33.32.156"]



# Your task is to identify IP addresses that appear in both lists.

# Tasks:
# 1. Use nested for loops to compare every IP in internalIPs with every IP in suspiciousIPs.
# 2. Print an IP address whenever a match is found.
# 3. Count the total number of matching IP addresses.
# 4. Print a message if no matching IP address is found.
# Challenge: Explain why nested loops are useful for comparing two lists, and how many comparisons your code performs with these lists.


# Exercise 10 — Mini SOC Log Analysis Engine
# Advanced
# This is your main challenge. You are building a basic log analysis engine that examines multiple security events.
# securityLogs = [    "2026-11-21 ALERT FAILED_LOGIN FROM 192.168.1.10",    "2026-11-21 INFO USER_LOGIN FROM 10.0.0.5",    "2026-11-21 ALERT MALWARE_DETECTED FROM 172.16.0.8",    "2026-11-21 ALERT FAILED_LOGIN FROM 192.168.1.50",    "2026-11-21 INFO SYSTEM_UPDATE FROM 10.0.0.10",    "2026-11-21 ALERT UNAUTHORIZED_ACCESS FROM 45.33.32.156"]



# Tasks:
# 1. Use a for loop to examine each log entry.
# 2. Count the total number of logs containing "ALERT".
# 3. Count the number of logs containing "FAILED_LOGIN".
# 4. Count the number of logs containing "MALWARE_DETECTED".
# 5. Use string methods to convert each log entry to uppercase before analysing it.
# 6. Use string slicing to extract the date from each log entry.
# 7. Extract the IP address from each log entry using string slicing.
# 8. Use a nested loop to compare the extracted IP addresses against this list:
# blockedIPs = [    "192.168.1.50",    "45.33.32.156"]



# 9. Print any log entry whose IP address appears in blockedIPs.
# 10. Print a final investigation summary containing all your counts.
# Bonus challenge: Use for...else to display "Log analysis completed successfully." after all log entries have been processed.