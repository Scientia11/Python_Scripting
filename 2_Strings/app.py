# To create strings i can use single quotes, double qoutes and thripple quotes.
# But it is advisable to be consistent with one

 #single qoutes
course = "Python"
print(course)


# #double qoutes
userName = 'Godsway'
print(userName)


#Triple quotes
#triple quotes can be used to format the output of a text
message = """
Hi Ben,
I am doing great, what about you?

Regards,
Godsway Addo.
"""

print(message)




# # Length Of A String
# # Use built in len() function to find the length of a string
# # A functon is a pieace of code that performs a task or calculates a value

courseName = "Python Programming"
stringLength = len(courseName)
print(stringLength)




#Accesing Individual Characters Of A String
#Use the square bracket and the character index

studyProgram = "Information Technology"

# # 0 upwards print from right to left
print(studyProgram[0])

# # -1 downwards print from right to left
print(studyProgram[-1])




# Slicing A String
firstName = "Godsway"

print("First name lemgth: ", len(firstName))

# slice the first 3 elements
print(firstName[0:3])

# slice from the first element all the way to the end of the string
print(firstName[0:])

# slice from the first element to the 3rd element
print(firstName[:3])

# slice from the beginning all the way to the end of the string
print(firstName[:])




# ESCAPE SEQUENCE
# \' = single qoute
# \" = double qoutes
# \\ = backslash
# \n = new line

townName = "\'Tapa \"Abotoase"
print(townName)

fullName = "\\Godsway \nAddo"
print(fullName)






# Exercise 1(Clean up the code)
# A junior SOC Analyst wrote the following code:
a = "administrator"
b = "192.168.1.25"
c = "Critical"
d = "Suspicious login detected"

# Your tasks:
# 1. Rename the variables using meaningful, clear, consistent Python naming conventions.
# 2. Print each variable with an appropriate descriptive label.
# 3. Explain why your new variable names are better than a, b, c, and d.



# ANSWER
# 1. Rename the variables using meaningful, clear, consistent Python naming conventions.
userName = "administrator"
sourceIP = "192.168.1.25"
severityLevel = "Critical"
alertMessage = "Suspicious login detected"

# 2. Print each variable with an appropriate descriptive label.
print("Username: ", userName)
print("Source IP: ", sourceIP)
print("Severity: ", severityLevel)
print("Alert: ", alertMessage)


# My variable names are better because they are meaniful,clear and follow a consistent style




# Exercise 2(String quotation challenge)
# Create variables containing the following text:
# 1. A string using single quotes: SOC Analyst
# 2. A string using double quotes: Security monitoring
# 3. A multiline string using triple quotes, formatted as follows:

# SECURITY INCIDENT REPORT
# Incident: Suspicious Login
# Severity: High
# Status: Under Investigation

# Print all three variables.
# Extra challenge: Create a string containing the text "The analyst's account was locked." Explain how you can represent it without Python confusing the apostrophe with the end of the string.




# ANSWER
# 1. A string using single quotes: SOC Analyst
profession = 'SOC Analyst'
print(profession)

# 2. A string using double quotes: Security monitoring
specialty = "Security monitoring"
print(specialty)

# 3. A multiline string using triple quotes
incidentReport = """
SECURITY INCIDENT REPORT
Incident: Suspicious Login
Severity: High
Status: Under Investigation
"""
print(incidentReport)


# Extra challenge: i can use double or triple quotes with the apostrophe in it
# this will prevent python from interpreting the single quote as the end of the string
status = "The Analyst's account was locked."
print(status)





# # Exercise 3(Investigate a suspicious username)
# A log entry contains this username:

username = "admin_root"

# Complete the following tasks:
# 1. Print the entire username.
# 2. Use len() to print the number of characters in the username.
# 3. Print the first character.
# 4. Print the last character.
# 5. Print the character at index 6.
# 6. Print the characters at indexes 0, 1, and 2 individually.
# Don't hardcode the length as your answer. Let Python calculate it.
# Reasoning question: Why does the first character have index 0 rather than index 1?




# ANSWER
# 1. Print the entire username.
print(username)

# 2. Use len() to print the number of characters in the username.
print(len(username))

# 3. Print the first character.
print(username[0])

# 4. Print the last character.
print(username[-1])

# 5. Print the character at index 6.
print(username[6])

# 6. Print the characters at indexes 0, 1, and 2 individually.
print(username[0])

print(username[1])

print(username[2])

# # Reasoning question: this is beacuse indexing in python starts from 0 



# # Exercise 4(Extract characters from a suspicious string)
# Consider this example:

source_ip = "10.20.30.45"

# Your tasks:
# 1. Print the length of the string.
# 2. Print the character at index 0.
# 3. Print the character at index 2.
# 4. Print the character at index 8.
# 5. Print the last character using negative indexing, if you've covered it in your course. Otherwise, leave this part until later.
# 6. Without running the code, predict what happens when you try to access source_ip[20]. Then test your prediction.
# Explain the result of the final task in your own words.


# ANSWER
# 1. Print the length of the string.
print(len(source_ip))

# 2. Print the character at index 0.
print(source_ip[0])

# 3. Print the character at index 2.
print(source_ip[2])

# 4. Print the character at index 8.
print(source_ip[8])

# 5. Print the last character using negative indexing, if you've covered it in your course. Otherwise, leave this part until later.
print(source_ip[-1])

# 6. Without running the code, predict what happens when you try to access source_ip[20]. Then test your prediction.
# the index is out of range hece an error will be displayed
# print(source_ip[20])





# Exercise 5(Build a security alert summary)
# You receive the following alert information:
# - Username: svc_backup
# - Source IP: 172.16.5.24
# - Alert type: Multiple Failed Login Attempts
# - Severity: Critical
# Write a Python script that:
# 1. Stores each item in a clearly named variable.
# 2. Prints a neatly formatted, multiline alert report using triple-quoted strings.
# 3. Prints the length of the username.
# 4. Prints the first and last characters of the username.
# 5. Prints the length of the alert type.
# 6. Prints the first character of the severity.





# ANSWER
# 1. Stores each item in a clearly named variable.
userName = "svc_backup"
sourceIP = "172.16.5.24"
alertType = "Multiple Failed Login Attempts"
severity = "Critical"

# 2. Prints a neatly formatted, multiline alert report using triple-quoted strings.
# Using f-string
alert = f"""
==== SECURITY ALERT ====
Username: {userName}
Source IP: {sourceIP}
Alert Type: {alertType}
Severity: {severity}
"""

print(alert)


# 3. Prints the length of the username.
userNameLength = len(userName)
print(userNameLength)

# 4. Prints the first and last characters of the username.
print(userName[0])
print(userName[1])

# 5. Prints the length of the alert type.
alertTypeLength = len(alertType)
print(alertTypeLength)

# 6. Prints the first character of the severity.
print(severity[0])





# EXERCISE 6 (Extract parts of a username)
# You receive this username from a system log:

userName = "socAnalyst2026"

# Write code to:
# 1. Print the first three characters.
# 2. Print the characters from index 3 up to, but not including, index 9.
# 3. Print the final four characters using slicing.
# 4. Print the entire username using slicing.
# 5. Print an empty slice by choosing the same start and stop index.

# Reasoning question: Why does userName[3:9] return six characters rather than seven?



# ANSWER
# 1. Print the first three characters.
print(userName[0:3])

# 2. Print the characters from index 3 up to, but not including, index 9.
print(userName[3:9])

# 3. Print the final four characters using slicing.
print(userName[(len(userName) - 4):])

# 4. Print the entire username using slicing.
print(userName[:])

# 5. Print an empty slice by choosing the same start and stop index.
print(userName[1:1])

# Reasoning Question: This is because pyhthon starts slicing from index 3 and ends at index 8(9-1)







# EXERCISE 7(Analyse a suspicious filename)
# A file has been flagged for investigation:

fileName = "invoice_malware.exe"

# Your tasks:
# 1. Extract invoice using slicing.
# 2. Extract malware using slicing.
# 3. Extract the file extension, including the period.
# 4. Extract everything before the extension.
# 5. Extract the first eight characters using a slice with an omitted start index.
# 6. Extract everything from index 8 to the end using a slice with an omitted stop index.

# Reasoning question: What does Python assume when you omit the start index or the stop index?



# ANSWER

# 1. Extract invoice using slicing.
extractedInvoice = fileName[0:7]
print(extractedInvoice)

# 2. Extract malware using slicing.
extractedMalware = fileName[8:15]
print(extractedMalware)

# 3. Extract the file extension, including the period.
fileExtentsion = fileName[15:]
print(fileExtentsion)

# 4. Extract everything before the extension.
fileNameBeforeExtension = fileName[0:15]
print(fileNameBeforeExtension)

# 5. Extract the first eight characters using a slice with an omitted start index.
firstEightCharacters = fileName[:8]
print(firstEightCharacters)

# 6. Extract everything from index 8 to the end using a slice with an omitted stop index.
fromIndexEightToEnd = fileName[8:]
print(fromIndexEightToEnd)


# Reasoning Question: python starts from beginning(0) all the way to the end of the string





# EXERCISE 8(Extract information from an alert ID)
# Your SIEM generates this alert identifier:

alertID = "SOC-20261016-CRIT-042"

# Using slicing, extract the following parts:
# Information	    Expected value
# Team identifier	SOC
# Date	            20261016
# Severity code	    CRIT
# Alert sequence	042

# Your task is to create a separate variable for each extracted part and print a formatted report using an f-string.




# ANSWER

teamIdentifier = alertID[0:3]
print(teamIdentifier)

alertDate = alertID[4:12]
print(alertDate)

severityCode = alertID[13:17]
print(severityCode)

aletSequence = alertID[18:]
print(aletSequence)

alertReport = f"""
===== ALERT IDENTIFIER =====
Team: {teamIdentifier}
Date: {alertDate}
Severity: {severityCode}
Sequence: {aletSequence}
============================
"""

print(alertReport)







# Exercise 9: Predict before you execute
# Study the following code:

sourceIP = "192.168.10.25"

print(sourceIP[0:3])
print(sourceIP[4:7])
print(sourceIP[8:10])
print(sourceIP[11:13])
print(sourceIP[:7])
print(sourceIP[8:])
print(sourceIP[4:4])

# Before running it:
# 1. Predict the output of every print() statement.
# 2. Explain what the empty slice returns and why.
# 3. Run the code and compare the actual output with your predictions.

# ANSWER
# output prediction
# 192
# 168
# 10
# 25
# 192.168 #python slice from 0 by defalult when the start is not specified
# 10.25  #python slice  to the end by default when the end is not specified
# ""









# Exercise 10: Build a basic IOC extraction report
# A security alert contains the following suspicious URL:

suspiciousURL = "https://malicious.example/login"

# For this exercise, assume the URL always has this exact format.
# Write a script that:
# 1. Extracts the protocol https.
# 2. Extracts the domain malicious.example.
# 3. Extracts the path /login.
# 4. Stores each extracted value in a meaningful camelCase variable.
# 5. Prints the results using a multiline f-string report.
# 6. Prints the length of the extracted domain.

# Bonus question: Why might fixed-index slicing be unreliable when extracting domains and paths from URLs with different formats?


# ANSWER
# 1. Extracts the protocol https.
urlProtocol = suspiciousURL[0:5]

# 2. Extracts the domain malicious.example.
urlDomainName = suspiciousURL[8:25]

# 3. Extracts the path /login.
urlPath = suspiciousURL[25:]

# 5. Prints the results using a multiline f-string report.
urlReport = f"""
===== URL Report =====
Protocol: {urlProtocol}
Domain Name: {urlDomainName}
URL Path: {urlPath}
======================
"""

print(urlReport)


# 6. Prints the length of the extracted domain.
lengthOfDomain = len(urlDomainName)
print("Domain Length: ", lengthOfDomain)


# Bonus question: Because URLs with different formats have different lengths



# EXERCISE 11

alertMessage = "The system displayed \"Access Denied\"."
print(alertMessage)

analystMessage = "The analyst\'s account is locked."
print(analystMessage)


# EXERCISE 12
filePath = "C:\\Users\\Admin\\Downloads\\malware.exe"
print(filePath)


# EXERCISE 13
userName = "adminRoot"
sourceIP = "192.168.10.25"
severity = "Critical"

report = f"===== SECURITY ALERT =====\nUsername: {userName}\nSource IP: {sourceIP}\nSeverity: {severity}\nAction: Investigate Immediately"
print(report)
