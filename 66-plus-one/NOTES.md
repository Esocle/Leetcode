# python map function

* 숫자 list -> 문자열
* 
numbers = [10, 20, 30]
' '.join(map(str, numbers))

출력 결과
10 20 30

---------------------------------
* 문자열 -> 숫자 list

n = 12345
n_list = list(map(int, str(n)))

출력 결과
[1, 2, 3, 4, 5]
