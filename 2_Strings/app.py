# To create strings i can use single quotes, double qoutes and thripple quotes.
# But it is advisable to be consistent with one

# #single qoutes
# course = "Python"
# print(course)


# #double qoutes
# userName = 'Godsway'
# print(userName)


# #Thripple quotes
# #thripple quotes can be used to format the output of a text

# message = """
# Hi Ben,
# I am doing great, what about you?

# Regards,
# Godsway Addo.
# """

# print(message)




# # Length Of A String
# # Use built in len() function to find the length of a string
# # A functon is a pieace of code that performs a task or calculates a value

# courseName = "Python Programming"
# stringLength = len(courseName)
# print(stringLength)





# #Accesing Individual Characters Of A String
# #Use the square bracket and the character index

# studyProgram = "Information Technology"
# # 0 upwards print from right to left
# print(studyProgram[0])

# # -1 downwards print from right to left
# print(studyProgram[-1])




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
# userName = "administrator"
# sourceIP = "192.168.1.25"
# severityLevel = "Critical"
# alertMessage = "Suspicious login detected"

# print("Username: ", userName)
# print("Source IP: ", sourceIP)
# print("Severity: ", severityLevel)
# print("Alert: ", alertMessage)


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
# profession = 'SOC Analyst'
# print(profession)

# specialty = "Security monitoring"
# print(specialty)

# incidentReport = """
# SECURITY INCIDENT REPORT
# Incident: Suspicious Login
# Severity: High
# Status: Under Investigation
# """
# print(incidentReport)


# # Extra challenge: i can use double or triple quotes with the apostrophe in it
# # this will prevent python from interpreting the single quote as the end of the string
# status = "The Analyst's account was locked."
# print(status)





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
# username = "admin_root"

# print(username)

# print(len(username))

# print(username[0])

# print(username[-1])

# print(username[6])

# print(username[0])

# print(username[1])

# print(username[2])

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
# source_ip = "10.20.30.45"

# print(len(source_ip))

# print(source_ip[0])

# print(source_ip[2])

# print(source_ip[8])

# print(source_ip[-1])

# # the index is out of range hece an error will be displayed
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
# userName = "svc_backup"
# sourceIP = "172.16.5.24"
# alertType = "Multiple Failed Login Attempts"
# severity = "Critical"


# alert = """
# ==== SECURITY ALERT ====
# Username: svc_backup
# Source IP: 172.16.5.24
# Alert Type: Multiple Failed Login Attempts
# Severity: Critical
# """

# print(alert)



# userNameLength = len(userName)
# print(userNameLength)


# print(userName[0])
# print(userName[1])


# alertTypeLength = len(alertType)
# print(alertTypeLength)


# print(severity[0])