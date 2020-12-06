#!/bin/python

def validate_passwords(requirements, passwords):
    valid = 0
    for i in range(len(requirements)):

        amount_and_letter = requirements[i].split(' ')
        verify_letter = amount_and_letter[1].strip()
        first_position = int(amount_and_letter[0].split('-')[0]) - 1
        second_position = int(amount_and_letter[0].split('-')[1]) - 1
        current_password = passwords[i]
        if(current_password[first_position] == verify_letter or current_password[second_position] == verify_letter):
            if not (current_password[first_position] == verify_letter and current_password[second_position] == verify_letter):
                valid += 1

    return valid


# Read file
passwords_stream = open('../passwords.txt', 'r')
all_passwords = passwords_stream.readlines()

# Gather requirements and passwords
requirements = []
passwords = []

# Loop through the lines read
for password in all_passwords:
    formatted = password.strip()
    split_line = formatted.split(':')
    requirements.append(split_line[0])
    passwords.append(split_line[1].strip())

print(validate_passwords(requirements, passwords))
