from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from statistics import mean

l = [1, 2, 3, 4, 5]


def int_num(x):
    for i in x:
        print("int型 " + str(int(i)), " float型 " + str(float(i)), " complex型 " + str(complex(i, i + 1)),
              complex(i, i + 1).conjugate(), end=" ")
        print(complex(i, i + 1).real, complex(i, i + 1).imag, end="\n")

    print("\n")

    for j in x:
        print("10進数を16進数: " + str(hex(j)).replace('0x', '"0x"') + " formatを使う: ", format(j, 'x'))
        print("16進数を10進数: " + str(int(hex(j), 16)))
        print("10進数を2進数: " + bin(j).replace('0b', '"0b" '), format(bin(i)).replace('0b', '"0b" '), 'b')
        print("2進数を10進数: " + str(int(bin(j), 2)))
        print("10進数を8進数: " + str(oct(j)).replace('0o', '"0o"') + "formatを使う: ", format(j, 'o'))
        print("8進数を10進数: " + str(int(oct(j), 8)))
        print("\n")


def tips():
    # 数値を含むか判断
    x = "4583"
    print(x.isdecimal())

    # 四捨五入round
    print(round(100.568))
    print(round(100.568, 1))  # 小数2桁目
    print(round(100.568, 2))  # 小数３桁目
    print("\n")

    # 四捨五入 quantize
    x = Decimal(str(100.567)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    y = Decimal(str(100.567)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    z = Decimal(str(100.567)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    u = Decimal(str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

    print(x)
    print(y)
    print(z)
    print(u)

    # 平均を求める1
    lst = [1, 2, 3, 4, 5]
    mea = mean(lst)
    print(mea)

    # 平均を求める2
    mea = sum(lst) / len(lst)
    print(mea)

    # べき乗
    num = pow(10, 2)
    print(num)

    num = 3 ** 2
    print(num)


def main():
    int_num(l)
    tips()


if __name__ == "__main__":
    main()
