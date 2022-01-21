import inspect

hello = "hello world"
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def iterator():
    # シーケンス演算
    if 'x' in "xx":
        print(hello)

    if 'j' not in 's':
        print(hello)

    print('ss' + 'tt')

    print(min(l))
    print(max(l))
    print(hello[1:5])
    print(l.count(1))


def iterator1():
    l.append(1)
    print(l)
    l.extend('1')
    print(l)
    l.insert(2, 'hello')
    print(l)

    print("\n")

    print(list(range(10)))
    print(list(range(0, 30, 5)))


def iterator2():
    print(hello.capitalize())  # 最初大文字
    print(hello.casefold())
    print(hello.center(1))
    print(hello.encode())
    print(hello.find('h'))


def main():
    # iterator()
    # iterator1()
    iterator2()


if __name__ == "__main__":
    main()
