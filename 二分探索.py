
# https://github.com/python/cpython/blob/96be3400a97946b0b3d032dd8c3c0561786796f1/Lib/bisect.py
def binary_search(input_lst, lst_val):

    input_lst = sorted(input_lst)

    # 探索範囲の両端
    left, right = 0,  len(input_lst)   
    while left < right:
        # 探索範囲の中央値
        mid = (left + right) // 2
        # 中央値と一致した場合は位置を返す       
        if input_lst[mid] == lst_val: 
            return mid
        # 中央値より大きい場合、探索範囲を右へ
        elif input_lst[mid] < lst_val:
            left = mid + 1
        # 中央値より小さい場合、探索範囲を左へ
        else:
            right = mid - 1
            
    # 見つからなかった場合
    return False           
