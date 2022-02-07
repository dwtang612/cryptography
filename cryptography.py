import os


# Clear Console
def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


# Function for main page
def cryptography():
    clearConsole()
    print("-------------------------------------Cryptography Tool-------------------------------------")
    print("Which tool would you like to use? ")
    print("\n1. Encryption Tool")
    print("2. Decryption Tool")
    print("\nEnter 'END' to complete program.\n")
    value = input("Please input your value: ")
    if value == '1':
        encryption()
    elif value == '2':
        decryption()
    elif value == 'END' or 'end':
        return print('---------------------------------------END OF PROGRAM---------------------------------------')
    else:
        cryptography()


# Function Encryption Tool Page
def encryption():
    clearConsole()
    print("-------------------------------------Encryption Tool-------------------------------------")
    print("\n1. Upload File")
    print("2. Input")
    print("\nEnter 'BACK' to go back.")
    print("Enter 'END' to complete program.\n")
    value = input("Please input your value: ")
    if value == '1':
        print('Please provide file name: ')
    elif value == '2':
        decryption()
    else:
        cryptography()


# Function Decryption Tool Page
def decryption():
    clearConsole()
    print("-------------------------------------Decryption Tool-------------------------------------")
    print("\n1. Upload File")
    print("2. Input")
    print("\nEnter 'BACK' to go back.")
    print("Enter 'END' to complete program.\n")
    return input("Please input your value: ")


# Main Script
cryptography()
