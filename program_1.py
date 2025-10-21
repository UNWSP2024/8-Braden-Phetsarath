#Braden Phetsarath
#10/20

# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names,
# and displays their first, middle, and last initials.
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    personsInitials = ""
    #    Add your logic here
    name = personsName.split()
    for string in name:
        print(string[0].upper(), sep='', end='')
        print('.', sep='', end='')
    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name')

initials = initials_generator(personsName)

print(initials)
