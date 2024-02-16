def fibo_recursion(number: int) -> int:
    """
    fibonacci function by recursion.
    :param number: integer number
    :return: integer number
    """
    global cnt_recu
    cnt_recu += 1
    if number <= 1:
        return 1
    else:
        return fibo_recursion(number - 1) + fibo_recursion(number - 2)


def fibo_DP(number: int) -> int:
    global cnt_dp
    global memo
    if number >= 2 and len(memo) <= number:
        memo.append(fibo_DP(number - 1) + fibo_DP(number - 2))
        cnt_dp += 1
    return memo[number]


cnt_recu, cnt_dp = 0, 0
memo = [1, 1]

print(" ## 30번째 피보나치 수열 ## ")

print(f"재귀 방식 --> {fibo_recursion(30)}, {cnt_recu} ")
print(f"DP 방식 --> {fibo_DP(30)}, {cnt_dp} ")
