# Record the Combination we already compute
table = {}


def Combination(n, r):
    if r == 1:
        return n
    elif n == r:
        return 1
    else:
        if table[n - 1][r - 1] == -1:
            #recursive
            result = Combination(n - 1, r) + Combination(n - 1, r - 1)
            table[n - 1][r - 1] = result
            return result
        else:
            return table[n - 1][r - 1]


def main():
    num1 = 990
    num2 = 33
    #set all the component in table to -1
    for i in range(num1):
        table[i] = {}
        for j in range(num2):
            table[i][j] = -1
    result = Combination(num1, num2)

    print (result)
    return result


if __name__ == "__main__":
    main()
