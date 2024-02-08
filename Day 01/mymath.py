import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"elapsed time : {end - start}")
        return result
    return wrapper

def factorial (number) -> int :
    """_summary_
    factorial by repetition
    Args:
        number (int): 팩토리얼을 계산한 숫자

    Returns:
        int : factorial result
    """
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result

# def factorial (number) -> int :
#     """_summary_
#     factorial by recursion
#     Args:
#         number (int): 팩토리얼을 계산할 숫자

#     Returns:
#         int: factorial result
#     """
#     if number == 1:
#         return 1
#     else :
#         return number * factorial(number-1)

@timer
def nCr(n, r) -> int : # SRP, OCP violation
    """_summary_
    조합함수

    Args:
        n (int): 서로 다른 n개의 대상
        r (int): n개의 대상 중에서 선택하는 대상의 개수

    Returns:
        int: 순서 상관없이 선택하는 경우의 수
    """

    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)

    return int(numerator / denominator)

