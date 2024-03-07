# WARNING: THIS GENERATES GIANT WORDLISTS!

import itertools

print("WARNING: THIS GENERATES GIANT WORDLISTS!")

def generate_passwords():
    strings = []
    num_strings = 10
    continuecode = False
  
    for i in range(num_strings):
        user_input = input("Enter string " + str(i+1) + ": ")
        strings.append(user_input)

    while continuecode == False:
      length = int(input("Enter the number of characters in each password: "))
      if length >= 8:
        continuecode = True
      else:
        print("Passwords generated must be at least 8 characters long.")
        
    passwords = []
    
    for i in range(2, len(strings)+1):
        permutations = itertools.permutations(strings, i)
        for perm in permutations:
            new_password = "".join(perm)[:length]
            passwords.append(new_password)

    return passwords

generated = generate_passwords()

print("Passwords have been generated. Adding to text file. Please wait...")

with open("passwords.txt", "w") as file:
  for password in generated:
    file.write(password + "\n")

print("Password list successfully made!")