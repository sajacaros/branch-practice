def print_hello(num: int):
    """
    print hello
    :param num: loop count
    :return: None
    """
    for i in range(num):
        print(f'{i}번째 안녕')

if __name__=='__main__':
    print_hello(10)