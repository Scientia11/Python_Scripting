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
loginAttempts = ["SUCCESS", "FAILED", "FAILED", "SUCCESS", "FAILED"]

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