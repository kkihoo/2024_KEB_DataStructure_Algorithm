def factorial (number) -> int :
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result


def nCr(n, r) -> int :
    """_summary_
    조합함수

    Args:
        n (int): _description_
        r (int): _description_

    Returns:
        int: _description_
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)

if __name__ == '__main__':
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f'{n}C{r} = {nCr(n, r)}')
    