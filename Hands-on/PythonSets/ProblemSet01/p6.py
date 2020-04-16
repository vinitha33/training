s = input()

num = s.split(',')
sum = 0

for e in num:
    sum += float(e)

print(sum)