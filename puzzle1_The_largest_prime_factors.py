def isPrime(num):
    stop = int(num ** 0.5) + 1
    temp = 0
    for i in range(1, stop):
        if num % i == 0:
            temp += 1
    if temp == 1:
        return True
    else:
        return False


def main():
    number = 600851475143
    stop_point = int(number ** 0.5)
    max_factor = 0

    # first check if it is prime
    if isPrime(number) == 1:
        max_factor = number
    # if not, find the maximum prime factor
    else:
        for i in range(2, stop_point):
            if number % i == 0:
                if isPrime(i) == 1:
                    max_factor = i
                if isPrime(number / i) == 1 and number / i > i:
                    max_factor = number / i
    # print the answer
    print (max_factor)
    return max_factor


if __name__ == "__main__":
    main()
