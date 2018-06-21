def circleOfNumbers(n, firstNumber):
    divide = n/2
    if divide <= firstNumber:
        return firstNumber - divide
    else:
        return firstNumber + n/2 