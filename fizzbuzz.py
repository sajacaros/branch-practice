def fizzbuzz(num: int):
    """
    if num is 3's multiple, print fizz,
    otherwise print num

    """
    for n in range(num):
        if n%3 == 0:
            print('fizz')
        else: print(n)



if __name__ == '__main__':
    fizzbuzz(15)
