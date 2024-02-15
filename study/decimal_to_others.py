def decimal_to_binary(number=int):
    if number < 2:
        return str(number)
    else:
        return decimal_to_binary(number // 2) + str(number % 2)


def decimal_to_octal(number=int):
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(number // 8) + str(number % 8)


def decimal_to_hexa(number=int):
    if number < 16:
        return str(number)
    else:
        return hex(number)  # 16진수 식 만들기 포기


while True:
    choose = input("1) 10 -> 2\n2) 10 -> 8\n3) 10 -> 16\n4) Quit\nChose number : ")
    if choose == "1":
        n = int(input("\nInput Decimal Number : "))
        print(f"\nBinary Number = {decimal_to_binary(n)}\n")
    elif choose == "2":
        n = int(input("\nInput Decimal Number : "))
        print(f"\nOctal Number = {decimal_to_octal(n)}\n")
    elif choose == "3":
        n = int(input("\nInput Decimal Number : "))
        print(f"\nHexadecimal Number = {decimal_to_hexa(n)}\n")
    elif choose == "4":
        print("\nExit the program.")
        break
    else:
        print("\nNot valid number, Please Enter 1 to 4")
