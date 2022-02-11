from collections import Counter


a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]

# Key 인자를 정하지 않은 기본적인 sort에선, 튜플 순서대로 우선순위 할당
b = sorted(a)

# print(b)

# key 인자에 함수를 넘겨주면 우선순위가 정해짐

c = sorted(a, key = lambda x : x[0])
# print(c)



d = sorted(a, key = lambda x : x[1])
# print(d)

# 비교할 아이템이 복수 개 일 경우, 튜플로 우선순위 정해줄 수 있다.

# - 를 붙이면 현재와 반대차순으로 정렬됨

e = sorted(a, key = lambda x : (x[0], x[1]))
# print(e)

# [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

f = sorted(a, key = lambda x : (x[0], -x[1]))
# print(f)

# [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]

# 뒤에 문자 순 정렬

s = ['2 A', '1 B', '4 C', '1 A']
s = sorted(s, key=lambda x: (x.split()[1], x.split()[0]))
# print(s)

a_list = ['a', 'b', 'd', 'd', 'b', 's']
a_counter = Counter(a_list).most_common()

# print(a_counter)

# 문자 역순 정렬 아스키 값 이용

a_counter = sorted(a_counter, key=lambda x : (-x[1], -ord(x[0])))
# print(a_counter)


# map 람다 표현식

print(list(map(lambda x: x+10, [1, 2, 3])))

# filter 람다 표현식

a = [8, 4, 2, 5, 2, 7, 9, 11, 26, 13]

print(list(filter(lambda x: x>7 and x<15, a)))


# reduce 람다 표현식

# reduce는 값을 누적시킨다.

from functools import reduce

t = [47, 11, 42, 13]

print(reduce(lambda x, y : x + y, t))
