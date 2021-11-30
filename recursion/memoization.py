
memo_dict = {1: 1,
            0: 1}


def fib(num: int=3):
    if num in memo_dict:
        return memo_dict[num]

    result = fib(num-1) + fib(num-2)
    memo_dict[num] = result
    return result


print(fib(5))