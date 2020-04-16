a = int(input())
b = int(input())
c = a/b
def is_power(a,b):
    if a/b == 0 and is_power(a/b,b) == True:
        return True
    else:
        return False

print(is_power(a,b))



