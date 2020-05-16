def sumDigits(s):
    digit_sum = 0
    for i in s:
        try:
            digit_sum += int(i)
        except ValueError:
            pass
    return digit_sum
print(sumDigits(input("Enter the string:")))
