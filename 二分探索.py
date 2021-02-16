
# https://github.com/python/cpython/blob/96be3400a97946b0b3d032dd8c3c0561786796f1/Lib/bisect.py
def binary_search(val, input_lst):

    # 探索範囲の両端
    left, right = 0, len(input_lst)
    while left < right:
        # 探索範囲の中間値
        mid = (left + right) // 2

        # 中間値と一致した場合は重複を確認し、インデックスを返す
        if input_lst[mid] == val:
            return duplicate_checker_(mid, input_lst)

        # 中間値より大きい場合、探索範囲を右側へ
        elif input_lst[mid] < val:
            left = mid+1
        # 中間値より小さい場合、探索範囲を左側へ
        else:
            right = mid
            
    # 見つからなかった場合、左側のインデックスを返す
    return print(left)

def duplicate_checker_(idx, input_lst):
    val = input_lst[idx]
    search_list = input_lst[:(idx+1)]
    return print(search_list.index(val))

#numbers = [1, 2, 3, 3, 5, 7, 10, 13, 18, 20, 23, 33, 34, 50, 80, 99]
# 探索する要素をソート（今回はソートされていることが前提）
#numbers = sorted(numbers)
#binary_search(4, numbers)

#words = ['air', 'apple', 'ocean', 'orange', 'sea', 'zoo']
#binary_search('ocean', words) 
