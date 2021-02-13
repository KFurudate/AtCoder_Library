# bit全探索は、n個のリストから要素の二択の全パターン(2**n)を探索するアルゴリズム
# https://qiita.com/conf8o/items/548d0baaf505f9bee91f
from itertools import combinations

patterns = []
n = len(input_lst)
# n個のリストから要素の二択の全パターン
for i in range(n+1):
    for pattern in combinations(input_lst, i):
    	patterns.append(pattern)

# https://qiita.com/gogotealove/items/11f9e83218926211083a
# 注) n=20: 2**n → 10**7

patterns = []
n = len(input_lst)
# n個のリストから要素の二択の全パターン(2**n)
for i in range(2 ** n):
	pattern = []
	# 2進数表記でそれぞれの桁が0か1のどちらか判定
    for j in range(n):
    	# フラグが立っていた場合の処理
        if (i >> j) & 1:  
        	pattern.append(input_lst[j])

    patterns.append(pattern)
        