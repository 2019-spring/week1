# name = "akmal husanov" # string "", ''
first_name = "akmal"
last_name = "husanov"
name = first_name + " " + last_name
message = "     WELCOME!!!      "
message1 = "this the python class"

print(name)
print(name.title())  # titling for each word in your string
print(name.upper())
print(message.lower())

# whitespaces - non printable characters (spaces, tabs, newlines etc. )
print("original message with strip in print: " + message.strip())
trimmed_message = message.strip()
print("trimmed message in the variable: " + trimmed_message)
print(message)
print(message1)
print(message1.title())

# ADDING WHITESPACE TO STRING  \t - tab (4 spaces), \n - newline
print("**************** whitespace ***************************")
name_with_newline = first_name + "\n" + last_name
name_with_tab = first_name + "\t" + last_name
print(name_with_newline)
print(name_with_tab)
# firstName , lastName - camel case style

print("My favourite cars are :\nBMW\nLEXUS\nMERC\nTOYOTA\n\n\n\n\n\n")
print("My favourite cars are :\n\tBMW\n\tLEXUS\n\tMERC\n\tTOYOTA")

# hw:
# 1. names: title, upper, lowers,
# 2. print your favourite quote , save the quote in message variable , save the author in author variable.
#     Then print the message then Author underneath (put some indentations)

# commenting >> highlight the lines then  CTRL + /
# autoformat in VS code >> shift + Alt + F 

# f string 

