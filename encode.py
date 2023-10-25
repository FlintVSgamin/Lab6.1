def encode(original_pass):
    result = ''
    for i in range(len(original_pass)):
        num = original_pass[i]
        result += chr((ord(num) + 3))
    return result


