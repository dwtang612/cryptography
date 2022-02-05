value = 0
while value != 'END':
    print("-------------------------------------Cryptography-------------------------------------")
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("BACK")
    print("\nEnter 'END' to complete program.\n")
    value = input("Please input your value: ").upper()
    if value == 1:
        print("-------------------------------------Encryption-------------------------------------")
        print("\n1. Upload File")
        print("2. Input")
        print("\nEnter 'END' to complete program.\n")
        value = input("Please input your value: ")
    elif value == 2:
        print("-------------------------------------Decryption-------------------------------------")
        print("\n1. Upload File")
        print("2. Input")
        print("\nEnter 'END' to complete program.\n")
        value = input("Please input your value: ")

print("\n[END OF PROGRAM]")
