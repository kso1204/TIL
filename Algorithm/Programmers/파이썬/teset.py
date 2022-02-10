import enum
from itertools import combinations, permutations, product
import re

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

list4 = [i*j for i in range(1, 10) for j in range(1, 10)]


nums = [2, 7, 11, 15]

table = {num: i for i, num in enumerate(nums)}

target = 9

for i, num in enumerate(nums):
    if ((target-num) in table) and (i != table[(target-num)]):
        print (i, table[(target-num)])


list = [['po','상욱'], ['back','진수'], ['back', '승집'], ['front', '길동'], ['front', '상아']]
list1 = []
list2 = []
list3 = []
for i in list:

    if i[0] == 'po':
        list1.append(i[1])

    if i[0] == 'front':
        list2.append(i[1])
    
    if i[0] == 'back':
        list3.append(i[1])


list2.append(", ".join(list2))
list3.append(", ".join(list3))

num = 1

result = []

for back in list2:
    for front in list3:
        result.append(dict(zip(["no", "po", "back", "front"], [num, list1[0], back, front])))

        num+=1

print(result)
