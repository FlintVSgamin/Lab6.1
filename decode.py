def decode(encoded_pass):
    result = ''
    for i in range(len(encoded_pass)):
        num = encoded_pass[i]
        result += chr((ord(num) - 3))
    return result

