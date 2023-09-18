def fizzbuzz(num: int):
    """
    if num is 3's multiple, print fizz,
    if num is 5's multiple, print buzz
    otherwise print num

    """
    for n in range(1, num + 1):
        print('fizz' * (n % 3 == 0) + 'buzz' * (n % 5 == 0) if n % 3 == 0 or n % 5 == 0 else n)


if __name__ == '__main__':
    fizzbuzz(15)
