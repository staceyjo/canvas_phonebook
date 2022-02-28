""""""
#
""" $ python3 phonebook.py
Electronic Phone Book
""" 
# =====================

# 1. Look up an entry
# If they choose "look up and entry", 
# I prompt the user to enter: the person's name
# then I command print () for the output of 
# the person's name and phone number


# 2. Set an entry
# If they choose set an entry, 
# I will ask them to enter : 
# the person's name and their phone number


# 3. Delete an entry
# If the user selects "delete and entry"
# I will ask for the person's name
# The user will provide the name
# Then I command an output that deletes the entry



# 4. List all entries- COMPLETE
# Print all items in the list as option for a user to select


# 5. Quit
# If they select this open 
# I need to find a way to end the program
""""""

#Incorporate a header to print on the screen

# print("Electronic Phone Book")


#Create my List of phonebook options as strings 
''''''
# List = ["1. Look up an entry", "2. Set an entry", "3. Delete an entry", "4. List all entries", "5. Quit"]
# print ("\nMenu Options: ")
# print(List[0])
# print(List[1])
# print(List[2])
# print(List[3])
# print(List[4])
''''''

# def selection = input

# Prompt the user to enter a number 1 - 5- create an input

# print ("What would you like to do?", "Please select an option 1-5, then hit enter")
# Create an input

#This is one way:
""""
def my_function(phonebook_names):
  print(phonebook_names)
  
my_function("Beyonce")
my_function("Whitney") 
my_function("Rihanna")
"""
#This is another way to get the list of names
"""""
def my_function(names):
  for x in names:
    print(x)

names = ["Beyonce", "Rihanna", "Whitney"]

my_function(names)
"""
''''''
# 1 = Look up an entry
a = "Look up an entry"
b = "Set an entry"
c = "Delete an entry"
d = "List all entries"
e = "Quit"
''''''

# If the user enters 1, I want the output to be a list of names
# names = ("Beyonce", "Rihanna", "Whitney")

# def print(names_in_phonebook(Beyonce, Rihanna, Whitney):
  #  "Beyonce", "Rihanna", "Whitney"

  # STARTING OVER AGAIN

# Create a GitHub repo then pull down to your machine
# Clone it down: git clone

# Break down the problem by steps within a ticket

# Create a menu list: 
# git branch
# git checkout -b
# click on  the .py file to open text editor
# copy the list
# create a variable, menu()
# paste the list from Canvas: 


menu = """
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
"""

# Now let's test it to see if it works:
print (menu)

# check the status: git status
# git add .
# git commit - m ""
# git log --oneline
# git push
# git push -u origin list_menu 
# created a branch off main an
# switched at the same time
# compare and pull request
# write your details
# check diff at the bottom
# create pull request
# approval stage --> Approved
# Merge pull request to main on GitHub
# Pull request successful, workfornt complete. 

user_input
#Workfront Effort #2
# "What do you want to do? 1-5"
# Well first I want to rephrase it to make it spicy
# What would you like to do?"
# "Please select an option 1-5 then, hit enter to continue: 

# Next I want to create a new branch to do this workfront:
# git checkout -b creates a new branch and swithces at the same time
# git checkout -b user_input

#So now that it prints the menu, 
# we have to prompt the user to input 1-5

selected_option = input("Please select an option (1-5) then, hit enter to continue:") 

# to see if the file works to get their choice: 

# print(selected_option)

#NEW WORK EFFORT
#If they choose to input an entry, 
# you will 1: ask them to enter a name
# then you will 2: ask them to enter a phone number
# So since this is a new feature, 
# we need to cut a new branch off the main
# using git checkout - b
# but first make sure you're on the main branch