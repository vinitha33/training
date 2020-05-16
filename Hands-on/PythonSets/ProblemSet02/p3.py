def factI(n):   #Iterative method
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
    print(fact)

def factR(n):   #Recursive method
    if n == 0 or n == 1:
        return 1
    else:
        return n * factR(n - 1)

num1 = int(input("Enter the number:"))

factI(num1)
print(factR(num1))
