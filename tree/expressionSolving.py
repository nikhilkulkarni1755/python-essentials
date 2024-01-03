import math

def solveExpression(expression):
    expression = expression[::-1]
    values = []
    val = 0
    power = 0

    for c in expression:
        if __isNumber(c):
            # check if next number is number too
            # print('is number')
            print(int(c) * math.pow(10,power))
            val += int(c) * math.pow(10,power)

            power+=1
        else:
            values.append(val)
            val = 0
            power = 0
    if val != 0:
        values.append(val)
    print(values)
    sum = 0
    for v in values:
        sum += v
    return sum

def __isNumber(c):
    if c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9' or c == '0':
        return True
    else:
        return False