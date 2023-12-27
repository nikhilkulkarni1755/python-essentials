
def toLowerCase(test):
    result = []
    for c in test:
        if c.isalnum():
            if ord(c) <= ord('Z'):
                result.append(chr(ord(c) + 32))
            else:
                result.append(chr(ord(c)))
        else:
            result.append(chr(ord(c)))
            
    return ''.join(result)