# A Caesar Cipher Program
# Coursework Assessment 1
# Name:Ginuka weragoda 
# Student No:2406982 

import os.path

def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
    return


def enter_message():
    mode = ''
    message = ''
    shift = 0
    # add your code here
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ('e', 'd'):
            break
        else:
            print("Invalid Mode")

    message = input("What message would you like to {}?: ".format("encrypt" if mode == 'e' else "decrypt")).upper()

    while True:
        try:
            shift = int(input("What is the shift number: "))
            break
        except ValueError:
            print("Invalid Shift")

    return (mode, message, shift)


def encrypt(message, shift):
    # add your code here
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted = shifted - 26
                encrypted_message = encrypted_message + chr(shifted)
            else:
                if shifted > ord('z'):
                    shifted = shifted - 26
                encrypted_message = encrypted_message + chr(shifted)
        else:
            encrypted_message = encrypted_message + char
    return encrypted_message


def decrypt(message, shift):
    # add your code here
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted = shifted + 26
                decrypted_message = decrypted_message + chr(shifted)
            else:
                if shifted < ord('a'):
                    shifted = shifted + 26
                decrypted_message = decrypted_message + chr(shifted)
        else:
            decrypted_message = decrypted_message + char
    return decrypted_message


def process_file(filename, mode, shift):
    list_messages = []
    # add your code here
    if is_file(filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if mode == 'e':
                    list_messages.append(encrypt(line.upper(), shift))
                else:
                    list_messages.append(decrypt(line.upper(), shift))
    return list_messages


def write_messages(lines):
    # add your code here
    with open('results.txt', 'w') as file:
        for line in lines:
            file.write(line + '\n')
    return


def is_file(filename):
    return os.path.isfile(filename) 


def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ('e', 'd'):
            break
        else:
            print("Invalid Mode")

    while True:
        location = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if location in ('f', 'c'):
            break
        else:
            print("Invalid Location")

    if location == 'c':
        message = input("What message would you like to {}?: ".format("encrypt" if mode == 'e' else "decrypt")).upper()
    else:
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")

    while True:
        try:
            shift = int(input("What is the shift number: "))
            if shift < 0 or shift > 25:
                raise ValueError("Shift number must be between 0 and 25")
            break
        except ValueError as e:
            print("Invalid Shift")  

    return (mode, message, filename, shift)


def main(): 
    welcome()
    while True:
        mode, message, filename, shift = message_or_file()

        if filename:
            messages = process_file(filename, mode, shift)
            write_messages(messages)
            print("Output written to results.txt")
        else:
            if mode == 'e':
                result = encrypt(message, shift)
                print(result)
            else:
                result = decrypt(message, shift)
                print(result)
                
        while True:
            repeat = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
            if repeat in ('y', 'n'):
                break
            else:
                print("Invalid Input")

        if repeat != 'y':
            break

    print("Thanks for using the program, goodbye!")
    return

if __name__ == '__main__':
    main()
