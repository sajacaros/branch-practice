def fizzbuzz(num):
    """
    if num is 5's multiple, print buzz
    """
    for n in range(num):
        if n%5 == 0:
            print('buzz')
        else: print(n)


if __name__ == '__main__':
    fizzbuzz(15)
