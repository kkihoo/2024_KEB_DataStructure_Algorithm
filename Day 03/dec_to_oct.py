def decimal_to_octal(number = int) -> str:
    """_summary_
    decimal number to octal number

    Args:
        number (int) : base decimal

    Returns:
        str: base octal
    """
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(n // 8) + str(n % 8)

n = int(input("Input Decimal Number : "))
print(decimal_to_octal(n))