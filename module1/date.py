import datetime as dt


def main():
    print(dt.date.today())

    print("\n")

    timea = dt.time(10, 30, 45, 123456)
    print(timea)
    timea = timea.replace(hour=5)
    print(timea)

    print("\n")

    print(dt.datetime.today())
    print(dt.datetime.now())

    x = dt.datetime.now()
    print(x.time())
    print(x.date())


if __name__ == "__main__":
    main()
