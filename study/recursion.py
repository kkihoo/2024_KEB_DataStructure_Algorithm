def add(num1, num2):
    if num2 <= num1:
        return num1
    return num2 + add(num1, num2 - 1)


num1 = int(input("First number : "))
num2 = int(input("Second number : "))

if num1 >= num2:
    num1, num2 = num2, num1

print(add(num1, num2))
