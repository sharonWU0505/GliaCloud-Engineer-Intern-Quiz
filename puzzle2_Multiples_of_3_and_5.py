def isMultiple(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


def main():
    number = 1000
    factor1 = 3
    factor2 = 5
    factor3 = 15
    result = 0
    for i in range(3, number):
        if isMultiple(i, factor1) == 1:
            result += i
        else:
            if isMultiple(i, factor2) == 1 and isMultiple(i, factor3) == 0:
                result += i
    # print the answer
    print(result)
    return result


if __name__ == "__main__":
    main()
