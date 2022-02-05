# print("-------------------------------------Cryptography-------------------------------------")
# print("\n1. Encrypt")
# print("2. Decrypt")
# print("BACK")
# print("\nEnter 'END' to complete program.\n")
# value = input("Please input your value: ")
# while value != 'END' or 'end':
#     print("-------------------------------------Cryptography-------------------------------------")
#     print("\n1. Encrypt")
#     print("2. Decrypt")
#     print("BACK")
#     print("\nEnter 'END' to complete program.\n")
#     value = input("Please input your value: ").upper()
#     if value == '1':
#         print("-------------------------------------Encryption-------------------------------------")
#         print("\n1. Upload File")
#         print("2. Input")
#         print("\nEnter 'END' to complete program.\n")
#         value = input("Please input your value: ")
#     elif value == '2':
#         print("-------------------------------------Decryption-------------------------------------")
#         print("\n1. Upload File")
#         print("2. Input")
#         print("\nEnter 'END' to complete program.\n")
#         value = input("Please input your value: ")
# print("\n[END OF PROGRAM]")

# Function for Encryption
def cryptography():
    print("-------------------------------------Cryptography-------------------------------------")
    print("Which tool would you like to use? ")
    print("\n1. Encryption Tool")
    print("2. Decryption Tool")
    print("\nEnter 'BACK' to go back.")
    print("Enter 'END' to complete program.\n")
    return input("Please input your value: ")


def encryption():
    print("-------------------------------------Encryption-------------------------------------")
    print("\n1. Upload File")
    print("2. Input")
    print("\nEnter 'BACK' to go back.")
    print("Enter 'END' to complete program.\n")
    return input("Please input your value: ")


def decryption():
    print("-------------------------------------Decryption-------------------------------------")
    print("\n1. Upload File")
    print("2. Input")
    print("\nEnter 'BACK' to go back.")
    print("Enter 'END' to complete program.\n")
    return input("Please input your value: ")


value = cryptography()
while value != 'END' or 'end':
    if value == '1':
        encryption()
    elif value == '2':
        decryption()
    elif value == 'BACK' or 'back':
        cryptography()
    print("\n[END OF PROGRAM]")
