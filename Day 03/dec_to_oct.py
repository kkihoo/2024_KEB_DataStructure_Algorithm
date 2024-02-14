def decimal_to_octal(number = int) -> str:
    """_summary_
    decimal number to octal number

    Args:
        number (int) : base decimal

    Returns:
        str: base octal
    """
    octal = " "
    while number > 0:
        octal = str(number % 8) + octal
        number = number // 8
    return octal

n = int(input("Input Decimal Number : "))
print(decimal_to_octal(n))