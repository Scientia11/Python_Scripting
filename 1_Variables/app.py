
# Variables are containers use to store items. 
# When we declare a variable, the compiler allocate a memory space, 
# store the item and set the varaible name to reference its address 




studentCount = 1000
# print("Total students :", studentCount)

rating = 8.99
# print("Rating: ", rating)

isPublished = False
# print("Published: ", isPublished)

courseName = "Python Programming"
# print("Course: ", courseName)





#Exercise 1(Your First Variables)
# Create four variables containing the following information:
# Variable	           Value
# analyst_name	        Your name
# analyst_role	        SOC Analyst
# daily_hours	        4
# is_learning_python	True

# Your task:
# 1. Create and initialize all four variables.
# 2. Print each variable to the terminal.
# 3. Print a descriptive message alongside each value.




# analystName = "Godsway Addo"
# print("Analyst Name: ", analystName)

# analystRole = "SOC Analyst"
# print("Role: ", analystRole)

# dailyHours = 4
# print("Daily Study Hours: ", dailyHours)

# isLearningPython = True
# print("Learning Python: ", isLearningPython)




#Exercise 2(Understanding Variable Reassignment)
# Examine this scenario.
# A security analyst initially records five failed login attempts. After investigating the logs, the analyst discovers that the actual number is eight.
# Your task:
# 1. Create a variable called failed_logins and initialize it to 5.
# 2. Print its value.
# 3. Update the same variable to 8.
# 4. Print its new value.



# failedLogins = 5
# print("Failed Login Attemps: ", failedLogins)

# failedLogins = 8
# print("Failed Login Attemps: ", failedLogins)

# Challeng Question: The new value 8 overrides the previous value for failed Logins





#Exercise 3(Security Alert Information)
# Imagine your SOC monitoring system generates an alert containing the following information:
# - Source IP address: 192.168.1.105
# - Destination IP address: 10.0.0.25
# - Alert severity: High
# - Alert status: Under Investigation

# Your task:
# Create one variable for each piece of information and print a report in the following format:
# ===== SECURITY ALERT =====
# Source IP: 192.168.1.105
# Destination IP: 10.0.0.25
# Severity: High
# Status: Under Investigation
# ==========================




# print("==== SECURITY ALERT ====")

# sourceIP = "192.168.1.105"
# print("Source IP: ", sourceIP)

# destinationIP = "10.0.0.25"
# print("Destination IP: ", destinationIP)

# alertSeverity = "High"
# print('Severity: ', alertSeverity)

# alertStatus = "Under Investigation"
# print("Status: ", alertStatus)

# print("========================")




#Exercise 4(PREDICT THE OUTPUT)
# Before running the following code, determine what you think it will print:
# username = "admin"
# username = "analyst"
# print(username)

# attempts = 3
# attempts = 7
# print(attempts)

# ip_address = "192.168.1.10"
# print(ip_address)


# Write down the exact output you expect, including the order of the lines. Then run the code to verify your prediction.
# Explain why the first two variables produce their respective outputs.




# Code Output Prediction
# analyst
# 7
# 192.168.1.10

# Explanation: because the values have been reasigned for the first two variables





#Exercise 5(Build A Mini SOC Alert Record)
#You're investigating a potentially compromised account. The following information has been collected:
# Information	            Value
# Username	           administrator
# Source IP	           203.0.113.45
# Failed login attempts	    12
# Account locked	      True
# Investigation status	  Open


# Your mission:
# Write a Python script that:
# 1. Stores all five pieces of information in appropriately named variables.
# 2. Prints a neatly formatted investigation report.
# 3. Prints the number of failed login attempts separately at the end.
# Your report should be easy for another SOC Analyst to read.

# Bonus question: Why might storing 12 as an integer be more useful than storing it as the string "12" when you eventually build security automation scripts?






# userName = "administrator"
# sourceIP = "203.0.113.45"
# failedLoginAttempts = 12
# accountIsLocked = True
# investigationStatus = "Open"

# print("==== SECURITY ALERT ====")
# print("User Name: ", userName)
# print("Source IP: ", sourceIP)
# print("Acount Locked: ", accountIsLocked)
# print("Status: ", investigationStatus)
# print("Failed Login Attempts: ", failedLoginAttempts)
# print("========================")


# Bonus Question: as an integer it help automationnscrpts easily determine the number of failed attempts. but a string is not a number.
