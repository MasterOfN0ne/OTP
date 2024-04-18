import random

inputbinlist = []
asciibinlist = []

EOD = int(input("Encrypt(1) or Decrypt(2)?: "))

if EOD == 1:
    user_input = input("Enter the text you would like to encrypt: ")

    for c in user_input:
        input_binary = format(ord(c), '08b')  # Convert character to 8-bit binary string
        inputbinlist.append(input_binary)

    keylength = len(user_input)

    random_ascii = ''.join(chr(random.randint(32, 126)) for _ in range(keylength))
    for c in random_ascii:
        ascii_binary = format(ord(c), '08b')  # Convert character to 8-bit binary string
        asciibinlist.append(ascii_binary)

    print("Message converted to binary:", inputbinlist)
    print("Random ASCII converted to binary:", asciibinlist)


    # XOR function to use later to encrypt messages.
    def xor_lists(list1, list2):
        result = []
        for i in range(min(len(list1), len(list2))):
            result.append(''.join(str(int(x) ^ int(y)) for x, y in zip(list1[i], list2[i])))
        return result


    xor_result = xor_lists(inputbinlist, asciibinlist)
    print("XOR result list:", xor_result)

    # Turn the XOR from the random ascii and the text into the final ascii text to give back to the user.
    ascii_chars = ''.join(chr(int(x, 2)) for x in xor_result)
    print("Encrypted ASCII characters:", ascii_chars)

elif EOD == 2:
    def xor_lists(list1, list2):
        result = []
        for i in range(min(len(list1), len(list2))):
            result.append(''.join(str(int(x) ^ int(y)) for x, y in zip(list1[i], list2[i])))
        return result
    keydecrypt = []
    resultlistbinary = []
    key_length = int(input("Enter the amount of binary for the key: "))
    #key_binary = input("Enter the binary for the key: ")
    encrypted_length = int(input("Enter the amount of binary for the encrypted text: "))
    #encrypted_binary = input("Enter the binary for the encrypted text: ")

    for x in range(0,key_length):
        key_binary = input("Enter the binary for the key: ")
        keydecrypt.append(key_binary)
    for x in range(0,encrypted_length):
        encrypted_binary = input("Enter the binary for the encrypted text: ")
        resultlistbinary.append(encrypted_binary)
    xor_finalfinal = xor_lists(keydecrypt, resultlistbinary)
    dec_chars = ''.join(chr(int(y, 2)) for y in xor_finalfinal)
    print(dec_chars)
else:
    print("Invalid option. Please enter 1 for encryption or 2 for decryption.")
