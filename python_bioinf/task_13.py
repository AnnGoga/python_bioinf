def counter(func):
    """
    декоратор, который при каждом вызове функции выводит количество ее вызовов
    """

    func.__invocation_count__ = 0

    def wrapper(*args, **kwargs):
        func.__invocation_count__ += 1
        res = func(*args, **kwargs)
        print("Количество вызовов функции {0}: {1}".format(func.__name__, func.__invocation_count__))
        return res

    return wrapper


@counter
def test():
    pass


if __name__ == "__main__":
    test()  # test была вызвана: 1 раз
    test()  # test была вызвана: 2 раз
    test()  # test была вызвана: 3 раз
