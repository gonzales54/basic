# SORT
import numpy as np

# bubble sort(バブルソート)

# bubble_sort.py
# bubble_date = [1, 5, 9, 3, 4, 8, 6, 7, 54, 2, 12, 63, 7, 25, 10]

"""def main(date):
    ally = len(date)

    for i in range(ally):
        for j in range(ally - 1, i, -1):
            if date[j] < date[j - 1]:
                date[j], date[j - 1] = date[j - 1], date[j]

    print(date)
# 実行    main(bubble_date)
"""

# selection sort 選択ソート

# selection_date = [1, 5, 9, 3, 4, 8, 6, 7, 54, 2, 12, 63, 7, 25, 10]


"""def main(date, n):
    for i in range(n):
        j = np.argmin(date[i:]) + i
        date[i], date[j] = date[j], date[i]
    print(date)
    main(selection_date, len(selection_date))
"""
"""insert_date = [1, 5, 9, 3, 4, 8, 6, 7, 54, 2, 12, 63, 7, 25, 10]
# insertion sort 挿入ソート

def main(x):
    n = len(x)
    for i in range(1, n):
        tmp = x[i]
        if tmp < x[i-1]:
            j = i
            while True:
                x[j] = x[j-1]
                j -= 1
                if j == 0 or tmp >= x[j-1]:
                    break
            x[j] = tmp
    print(x)


if __name__ == "__main__":
    main(insert_date)"""

shell_date = [1, 5, 9, 3, 4, 8, 6, 7, 54, 2, 12, 63, 7, 25, 10]

# shell sort シェルソート
def main(array):
    n = len(array)
    h = 0

    while h <= n/9 : h = 3*h + 1
    while h > 0:
        # print("while h =", h)
        # 間隔hで挿入ソート, 最終的に挿入ソート
        for i in range(h, n):
            tmp = array[i] # 挿入する値を退避
            if tmp < array[i-h]: # 挿入する必要があるか
                j = i # 挿入する位置
                while True:
                    array[j] = array[j-h] # h後ろにずらす
                    j -= h
                    if j < h or tmp >= array[j-h]:
                        break
                array[j] = tmp # 空いた位置に退避していた値を挿入
                # print(array)
        h = int(h/3)
    print(array)

if __name__ == "__main__":
    main(shell_date)