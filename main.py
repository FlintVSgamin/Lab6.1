def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')


def encode(original_pass):
    result = ''
    for i in range(len(original_pass)):
        num = original_pass[i]
        result += chr((ord(num) + 3))
    return result


def decode(encoded_pass):
    result = ''
    for i in range(len(encoded_pass)):
        num = encoded_pass[i]
        result += chr((ord(num) - 3))
    return result


if __name__ == '__main__':
    while True:
        menu()
        option = int(input('\nPlease enter an option: '))
        if option == 1:
           original_pass = str(input('Please enter your password to encode: '))
           encoded_pass = encode(original_pass)
           print('Your password has been encoded and stored!')
        elif option == 2:
            print(f'The encoded password is {encoded_pass}, and the original password is {original_pass}.')
        elif option == 3:
            break


