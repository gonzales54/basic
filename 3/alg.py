# Algorithm

import time
from functools import wraps


# 実行時間計測用デコレーター
def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        process_time = end_time - start
        print(f"{main.__name__}は{process_time}秒かかりました")
        return result

    return wrapper


# search
# 1 Linear Search(線形探索)

list_date = [1, 15, 8, 65, 48, 56, 2, 148, 6, 21, 4, 5, 26, 15, 4, 562, 21, 54, 51]
min = 0
max = len(list_date)
target1 = 5
target2 = 56

"""@stop_watch
def main():
    for i in range(max):
        if target2 == list_date[i]:
            print("探索成功 target1は{}番目にありました".format(i))
        else:
            pass
        # print(i)"""

"""@stop_watch
def main(target, list_date):
    i = 0
    while True:
        if target == list_date[i]:
            print("探索成功。targetは{}番目にありました".format(i))
            break
        else:
            i += 1

    # 実行main(target1, list_date)"""


@stop_watch
def main(target, date):
    min = 0
    max = len(date)

    i = 0  # targetの番地
    while True:
        middle = int(min + (max - min) / 2)
        if target == date[middle]:
            print("探索成功。{}は{}番目に発見しました。".format(target, middle))
            break

        elif target > date[middle]:
            min = middle + 1

        elif target < date[middle]:
            max = middle - 1


sort_date1 = [1, 2, 3, 4, 5, 6, 12, 45, 67, 89, 234, 581, 1256, 2345]
sort_date2 = [1, 2, 3, 4, 5, 6, 12, 45, 67, 72, 89, 234, 581, 1256, 2345]
# 実行    main(581, sort_date2)



if __name__ == "__main__":
    main()