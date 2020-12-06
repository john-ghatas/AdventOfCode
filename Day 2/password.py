#!/bin/python

def validate_passwords(requirements, passwords):
    valid = 0
    for i in range(len(requirements)):
        amount_and_letter = requirements[i].split(' ')
        verify_letter = amount_and_letter[1]
        min_amount = int(amount_and_letter[0].split('-')[0])
        max_amount = int(amount_and_letter[0].split('-')[1])
        occurances = []
        for letter in passwords[i]:
            if letter in verify_letter:
                occurances.append(letter)

        if(len(occurances) >= min_amount and len(occurances) <= max_amount):
            valid = valid + 1

    return valid


# Read file
passwords_stream = open('passwords.txt', 'r')
all_passwords = passwords_stream.readlines()

# Gather requirements and passwords
requirements = []
passwords = []

# Loop through the lines read
for password in all_passwords:
    formatted = password.strip()
    split_line = formatted.split(':')
    requirements.append(split_line[0])
    passwords.append(split_line[1])

print(validate_passwords(requirements, passwords))
