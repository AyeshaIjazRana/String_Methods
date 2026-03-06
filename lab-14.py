# Tasks:

# 1. new_password = " mySecretWord "
# • The user accidentally added spaces before and after their password. Create a new
# variable that removes these spaces.
# • Check if this cleaned password is all lowercase and print the result (True or False).
# • The system requires all passwords to be uppercase. Convert the cleaned password to
# uppercase and print it. 

new_password = " mySecretWord "
updated_pwd=new_password.strip()
print("Cleaned Password:",updated_pwd)
print("Password is all lowercase:",updated_pwd.islower())
print("Password:",updated_pwd.upper())

# 2. messy_inventory = "apples;bananas;rotten_pears;grapes"
# • There are "rotten_pears" in the inventory! Replace "rotten_pears" with "fresh_pears".
# • The data is currently separated by semicolons (;). Split this string into a proper Python
# list.
# • Now that it is a list, join the items back together into a single string, but this time
# separate them with a comma and a space (,). Print the final result.

messy_inventory = "apples;bananas;rotten_pears;grapes"
fresh_inventory=messy_inventory.replace("rotten_pears","fresh_pears")
inventory_list=fresh_inventory.split(";")
inventory=",".join(inventory_list) 
print(inventory)  
      
# 3. secret_message = "The quick rabbit runs past the resting turtle."
# • Count exactly how many times the letter "r" appears in the message and print the
# number.
# • Find the exact starting index position of the word "turtle", “runs” , “rabbit” & “past”
# and print it.

secret_message = "The quick rabbit runs past the resting turtle."
print("Letter r in secret message appears",secret_message.count("r"),"times.")
print("The word turtle is at index",secret_message.index("turtle"),"in secret_message.")
print("The word runs is at index",secret_message.index("runs"),"in secret_message.")
print("The word rabbit is at index",secret_message.index("rabbit"),"in secret_message.")
print("The word past is at index",secret_message.index("past"),"in secret_message.")

# 4. alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# • Extract and print the first 5 letters of the alphabet.
# • Use a negative index to extract and print the last 3 letters of the alphabet.
# • Use the step feature to print every second letter of the alphabet (A, C, E, etc.).
# • Use slicing to print the entire alphabet completely backward.
# Hint: Slicing [start:stop:step], Negative Indexing

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("First five letters:",alphabet[0:5])
print("Last three letters:",alphabet[-3:])
print("Backward alphabet:",alphabet[::-1])
print("Every second letter:",alphabet[::2])

# 5. encrypted_word = " >>p-y-t-h-o-n<< "
# • First, remove the extra spaces at the very beginning and end of the string.
# • Next, remove the >> and << symbols. (Hint: You can use replace to swap them with an
# empty string "").
# • Now, split the remaining string at each hyphen (-) to create a list of individual letters.
# • Join that list of letters back together into a single, solid word with no spaces in between.
# • Finally, convert the decoded word to all uppercase and print it. (If you did it right, it
# should print "PYTHON").

encrypted_word = " >>p-y-t-h-o-n<< "
without_space=print("Withput space encrypted_word is:",encrypted_word.strip())
enc_word=encrypted_word.replace(">>","").replace("<<","")
print(enc_word)
word=enc_word.split("-")
print(word)
decode_word="".join(word)
print(decode_word.upper())


