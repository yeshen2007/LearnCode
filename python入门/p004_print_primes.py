"""
打印区间内的所有素数
"""


def is_prime(number):
    if number in (1, 2):
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True


def print_primes(begin, end):
    for number in range(begin, end+1):
        if is_prime(number):
            print(f"{number} is a prime")


if __name__ == '__main__':
    begin = 11
    end = 50
    print_primes(begin, end)