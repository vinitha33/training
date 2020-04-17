def sum_digits(str1):
    digitsum = 0
    for i in str1:
        try:
            digitsum += int(i)
            print(digitsum)
        except ValueError:
            pass

sum_digits("a1b2c3")