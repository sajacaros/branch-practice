def fizzbuzz(num: int):
    """
    if num is 3's multiple, print fizz,
    if num is 5's multiple, print buzz
    otherwise print num

    """
    for n in range(1, num+1):
        if n%15 == 0:
            print('fizzbuzz')
        elif n%3 == 0:
            print('fizz')
        elif n%5 == 0:
            print('buzz')
        else: print(n)


if __name__ == '__main__':
    fizzbuzz(15)
