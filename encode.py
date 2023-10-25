def encode(original_pass):
    result = ''
    for i in range(len(original_pass)):
        char = original_pass[i]
        result += chr((ord(char) + 3))
    return result


