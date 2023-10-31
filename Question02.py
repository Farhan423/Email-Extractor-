import re

email = input("Enter an email address: ")

# Define a regular expression pattern to match email addresses
pattern = r'@([A-Za-z0-9.-]+)\.'

# Use the findall method to extract the domain name
matches = re.findall(pattern, email)

if matches:
    Output_name = matches[0]
    print("Output:", Output_name)
else:
    print("Invalid email address format")
