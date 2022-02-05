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
    return input("Please input your value: ")


# Function Encryption Tool Page
def encryption():
    clearConsole()
    print("-------------------------------------Encryption Tool-------------------------------------")
    print("\n1. Upload File")
    print("2. Input")
    print("\nEnter 'BACK' to go back.")
    print("Enter 'END' to complete program.\n")
    return input("Please input your value: ")


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
value = cryptography()
while value != 'END' or 'end':
    if value == '1':
        value = encryption()

    elif value == '2':
        value = decryption()

    elif value == 'BACK' or 'back':
        value = cryptography()

    print("\n[END OF PROGRAM]")
