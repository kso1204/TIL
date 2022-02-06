# Do it 점프 투 파이썬

# 파이썬의 특징?

1. 파이썬은 인간다운 언어이다.

2. 파이썬과 C는 찰떡궁합이라는 말이 있다.

3. 즉 프로그램의 전반적인 뼈대는 파이썬으로 만들고, 빠른 실행 속도가 필요한 부분은 C로 만들어서 파이썬 프로그램 안에 포함시키는 것이다.

4. 파이썬은 배우기 쉽고, 간결하다.

5. 파이썬은 들여쓰기를 하지 않으면 실행 되지 않는다.

6. 파이썬은 줄을 맞추지 않으면 실행 되지 않는다.

7. 파이썬은 개발 속도가 빠르다.

# 파이썬 프로그래밍의 기초, 자료형

# 숫자형 자료형

1. x의 y제곱을 나타내는 ** 연산자

- a = 3, b = 4 

- a ** b = 81

2. 나눗셈 후 몫을 반환하는 // 연산자

- 7 / 4  = 1.75

- 7 // 4 = 1

# 문자열 포맷팅

1. 숫자 바로 대입 "I eat %d apples." % 3 => 숫자 %d

2. 문자열 바로 대입 "i eat %s apples." % "five" => 문자열 %s

3. 변수 대입하기

- number = 3

- "I eat %d apples." % number

4. 2개 이상의 값 넣기

- number = 10

- day = "three"

- "I ate %d apples. so I was sick for %s days." % (number, day)

5. 필살기? %s를 사용하면 다 알아서 포맷팅 해준다.

6. format함수 사용하기

- "I eat {0} apples".format(3)

7. 파이썬 3.6 버전 부터 사용 가능한 f 문자열 포매팅

- name = '홍길동'

- age = 30

- f'나의 이름은 {name}입니다. 나이는 {age + 1}입니다."

# 문자열 관련 함수

1. 문자 개수 세기(count)

- a = "hobby"

- a.count('b') => 2

2. 위치 알려주기 1 (find)

- a = "Python is the best choice"

- a.find('b') = 14

- a.find('k') = -1

3. 위치 알려주기 2 (index)

- a = "Life is too short"

- a.index('t') = 8

- a.index('k') => Error 발생

4. 문자열 삽입 (join)

- ",".join('abcd') = 'a,b,c,d'

5. ",".join([' a ', ' b ' , ' c ', ' d ']) = 'a,b,c,d'

6. 소문자를 대문자로 바꾸기(upper)

- a = "hi" 

- a.upper() => 'HI'

7. 대문자를 소문자로 바꾸기(lower)

- a = "HI"

- a.lower() = 'hi'

8. 왼쪽 공백 지우기 (lstrip)

- a = " hi "

- a.lstrip() => "hi "

9. 오른쪽 공백 지우기 (rstrip)

- a = " hi "

- a.rstrip() = " hi"

10. 양쪽 공백 지우기 (strip)

- a = " hi "

- a.strip() = "hi"

11. 문자열 바꾸기 (replace)

- a = "Life is too short"

- a.replace("Life", "Your leg")

- 'Your leg is too short'

12. 문자열 나누기 (split)

- a = "Life is too short"

- a.split() = 공백을 기준으로 문자열 나눔 = ['Life', 'is', 'too', short']

- b = "a:b:c:d"

- b.split(":") = ['a', 'b', 'c', 'd']

- 아무 값도 넣어주지 않으면 공백으로 알아서 나눠준다.

# 리스트 자료형 

# 리스트는 어떻게 만드는가?

- odd = [1, 3, 5, 7, 9]

- 리스트명 = [요소1, 요소2, 요소3, ...]

- a = []

- b = [1, 2, 3]

- c = ['Life', 'is', 'too', 'short']

- d = [1, 2, 'Life', 'is']

- e = [1, 2, ['Life', 'is']]

- 리스트는 a처럼 아무것도 포함하지 않아 비어 있는 리스트 or b처럼 숫자, c처럼 문자값, d처럼 숫자, 문자, e처럼 리스트 자체를 포함하기도 한다. 즉 리스트 안에는 어떤 자료형도 가능

- a = [1, 2, 3]

- a[0] = 1, a[-1] = 3 

- 리스트에서 -1을 사용하는 부분이 가장 신선한 듯 하다..

- a = [1, 2, 3, ['a', 'b', 'c']]

- a[0] = 1, a[-1] = ['a', 'b', 'c'], a[3] = ['a', 'b', 'c']

- a[-1][0] = 'a'

- 삼중 리스트도 가능하다

# 리스트의 슬라이싱?

- a = [1, 2, 3, 4, 5]

- a[0:2] = [1, 2] 0<=리스트<2

# 리스트 연산하기

1. 리스트 더하기?

- a = [1, 2, 3]

- b = [4, 5, 6]

- a + b = [1, 2, 3, 4, 5, 6]

2. 리스트 반복하기

- a = [1, 2, 3]

- a * 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]

3. 리스트 길이 구하기

- a = [1, 2, 3]

- len(a) = 3

4. 문자열과 숫자는 더할 수 없다. 즉 "ab" + 3은 에러 => "ab" + str(3)은 가능하다 

- str은 함수는 정수나 실수를 문자열의 형태로 바꾸어 주는 파이썬의 내장 함수이다.

# 리스트 관련함수

1. 리스트에 요소 추가 (append)

- a = [1, 2, 3]

- a.append(4) = [1, 2, 3, 4]

2. 리스트에 리스트 추가

- a.append([5, 6])

- [1, 2, 3, 4, [5, 6]]

3. 리스트 정렬 (sort)

- a = [1, 4, 3, 2]

- a.sort() => [1, 2, 3, 4]

- a = ['a', 'c', 'b']

- a.sort() => ['a', 'b', 'c']

4. 리스트 뒤집기 (reverse)

- a = ['a', 'c', 'b']

- a.reverse() => ['b', 'c', 'a']

- 정렬하고 역순으로 보여주는 것이 아닌, 그저 그대로 뒤집을 뿐이다.

5. 위치 반환 (index)

- a = [1, 2, 3]

- a.index(3) = 숫자3의 위치는 a[2] 이므로 2이다.

- a.index(1) = 숫자1의 위치는 a[0] 이므로 0이다.

- a.index(0) = 없으므로 Error

6. 리스트에 요소 삽입 (insert) 

- insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수, 숫자는 0부터 센다

- a = [1, 2, 3]

- a.insert(0, 4) = [4, 1, 2, 3]

- a.insert(3, 5) = [4, 1, 2, 5, 3]

7. 리스트 요소 제거 (remove)

- remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수

- a = [1, 2, 3, 1, 2, 3]

- a.remove(3) = [1, 2, 1, 2, 3]

- a.remove(3) = [1, 2, 1, 2]

8. 리스트 요소 끄집어내기(pop)

- pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.

- a = [1, 2, 3]

- a.pop() = 3

- a = [1, 2]

- pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다.

- a = [1, 2, 3]

- a.pop(1) = 2

- a = [1, 3]

9. 리스트에 포함된 요소 x의 개수 세기(count)

- count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수

- a = [1, 2, 3, 1] 

- a.count(1) = 2

10. 리스트 확장 (extend)

- extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다.

- a = [1, 2, 3]

- a.extend([4, 5])

- a = [1, 2, 3, 4, 5]

# 튜플 자료형

- 튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다

- 리스트는 []으로 둘러싸지만 튜플은 ()으로 둘러싼다.

- 리스트는 그 값의 생성-삭제-수정이 가능하지만 튜플은 그 값을 바꿀 수 없다 (?! 불변성?)

- t1 = ()

- t2 = (1, )

- t3 = (1, 2, 3)

- t4 = 1, 2, 3

- t5 = ('a', 'b', ('ab', 'cd'))

- t2처럼 단지 1개의 요소만 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다

- t4처럼 괄호를 생략해도 무방하다

# 딕셔너리 자료형

1. 딕셔너리란? '해시' 또는 '연관 배열' 

2. key, value를 한 쌍으로 갖는 자료형

3. 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고 key를 통해 value를 얻는다.

# 딕셔너리는 어떻게 만들까?

1. {key1: value1, key2: value2}

2. 쌍 여러 개가 {}로 둘러싸여 있다. 각각의 요소는 key:value 형태로 이루어져 있고 쉼표(,)로 구분되어 있다.

3. key에는 변하지 않는 값, value는 변해도 됨

4. dic = {'name' : 'pey', 'phone' : '01012345678', 'birth' : '1234'}

# 딕셔너리 쌍 추가, 삭제하기

- a = {1: 'a'}

- a[2] = b

- {1: 'a', 2: 'b'}

- a['name'] = 'pey'

- {1: 'a', 2: 'b', 'name' : 'pey'}

- a[3] = [1, 2, 3]

- {1: 'a', 2: 'b', 'name' : 'pey', 3: [1, 2, 3]}

# 딕셔너리 요소 삭제하기

1. del a[1]

2. {'name' : 'pey', 3: [1, 2, 3], 2: 'b'}

# 딕셔너리를 사용하는 방법

1. 딕셔너리에서 key 사용해 value 얻기

2. grade = {'pey' : 10, 'july' : 20}

3. grade['pey'] = 10, grade['july'] = 20

4. 동일한 key가 2개 이상 존재할 경우 하나를 제외하고는 모두 무시된다.

5. 리스트를 key로 사용하면 Error

# 딕셔너리 관련 함수

1. Key 리스트 만들기(keys)

2. a = {'name' : 'pey', 'phone' : 01012345678, 'birth' : '1234'}

3. a.keys() => dict_keys(['name', 'phone', 'birth']) 딕셔너리 a의 key만을 모아서 dict_keys 객체를 돌려준다.

```

>>> for k in a.keys():
    
    print(k) 

name
phone
birth

print(k)를 입력할 때 들여쓰기를 하지 않으면 오류가 발생한다.

```

4. dict_keys 객체를 리스트로 변환하려면?

- list(a.keys()) => ['name', 'phone', 'birth']

5. dict_keys 객체를 사용하는 것은 리스트와 차이가 없지만, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.

6. Value 리스트 만들기 (values)

- a.values()

- dict_values(['pey', '01012345678', '1234'])

7. Key, Value 쌍으로 얻기 (items)

- a.itmes() => dict_items([('name', 'pey'), ('phone', '01012345678'), ('birth', '1234')])

8. key: value 쌍 모두 지우기 (clear)

- a.clear() => a

9. a = {'name' : 'pey', 'phone' : 01012345678, 'birth' : '1234'}

10. a.get('name') = 'pey'

11. a.get('n') => None,  a['n'] = Error

12. 해당 key가 딕셔너리 안에 있는지 조사하기(in)

13. 'name' in a => True, 'email' in a => False

# 집합 자료형

1. 집합 자료형은 set 키워드를 사용해 만들 수 있다.

2. s1 = set([1, 2, 3]) => {1, 2, 3}

3. s2 = set("Hello") => {'e', 'H', 'l', 'o'} => ????????? => set에는 다음과 같은 특징이 있다.

4. 중복을 허용하지 않는다. 순서가 없다 (Unordered)

5. set 자료형은 인덱싱이 없기 때문에 list로 변환하거나 tuple로 변환해야 한다. list(s1) or tuple(s1)

# 교집합, 합집합, 차집합 구하기

1. set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때이다.

2. s1 = set([1, 2, 3, 4, 5, 6])

3. s2 = set([4, 5, 6, 7, 8, 9])

4. s1과 s2의 교집합

- s1 & s2 = {4, 5, 6} or s1.intersection(s2) or s2.intersection(s1)

5. s1과 s2의 합집합

- s1 | s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9} or s1.union(s2) or s2.union(s1) // 중복은 제거

6. s1과 s2의 차집합

- s1 - s2 = {1, 2, 3} or s1.difference(s2)

- s2 - s1 = {7, 8, 9} or s2.difference(s1)

# 집합 자료형 관련 함수

1. 값 1개 추가하기(add)

- s1 = set([1, 2, 3])

- s1.add(4)

- s1 = {1, 2, 3, 4}

2. 값 여러 개 추가하기(update)

- s1 = set([1, 2, 3])

- s1.update([4, 5, 6])

- s1 = {1, 2, 3, 4, 5, 6}

3. 특정 값 제거하기 (remove)

- s1 = set([1, 2, 3])

- s1.remove(2)

- s1 = {1, 3}

# Bool 자료형

1. True or False

2. a = True, B = False

3. 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면("", [], (), {}) 거짓이 된다. 당연히 비어 있지 않으면 참이 된다. 숫자에서는 그 값이 0일 때 거짓이 된다.

```

a = [1, 2, 3, 4]

while a: // a가 참인 동안
    a.pop() // 리스트의 마지막 요소를 하나씩 꺼낸다.

4
3
2
1

```

# 자료형의 값을 저장하는 공간, 변수

```

a = 1

b = "python"

c = [1, 2, 3]

id(a) => 430302029896(주소)

a = [1, 2, 3]

b = a

b 변수에 a 변수를 대입하면?

id(a) = id(b) = 430302029896 동일하다.

a is b => True // 동일한 객체를 가리키고 있는지에 대해서 판단하는 파이썬 명령어 is

a[1] = 4

a => [1, 4, 3]

b => [1, 4, 3]

다른 주소를 가리키게 만드는 방법?

1. [:] 사용 => 리스트 전체를 가리키는[:]을 사용해서 복사하는 것 

a = [1, 2, 3]

b = a[:]

a[1] = 4

a = [1, 4, 3]

b = [1, 2, 3]

2. copy 모듈 사용

a = [1, 2, 3]
 
b = copy(a) =>  b = a[:] 와 동일하다.

b is a => False 즉 다른 객체

```

# 변수를 만드는 여러 가지 방법

1. a, b = ('python', 'life') 튜플로 a, b에 값을 저장하는 방법 => (a, b) = 'python', 'life' 와 동일하다

2. [a, b] = ['python', 'life'] 리스트를 변수로 만드는 방법

3. a = b = 'python' 같은 값을 대입하는 방법

4. python에서 스왑하는 방법

```

a = 3

b = 5

a, b = b, a //a와 b의 값을 바꿈

a = 5, b = 3

```

# 조건문

1. if 조건문 뒤에는 반드시 콜론(:)이 붙는다. 

2. 그리고 그 밑에 들여쓰기를 해서 문장을 작성해야 한다. 탭을 사용하거나 스페이스 네 번을 사용하거나 상관없지만 하나만 사용해야 한다.

3. 조건문에서 아무 일도 하지 않게 설정하고 싶다면? (pass)

```

pocekt = ['paper', 'money' ,'cellphone']

if ('money') in pocket:
    pass
else
    print("카드를 꺼내라")

```

4. else if => elif

```

pocekt = ['paper', 'card' ,'cellphone']

if ('money') in pocket:
    pass
elif ('paper') in pocket:
    print("종이?")
else
    print("카드를 꺼내라")


```

# 조건부 표현식

```

if score >= 60:
    message = "success"
else:
    message = "fail"

조건부 표현식(conditional expression)

message = "success" if score >= 60 else "failure"

조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우

```

# while문

```

treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


```

1. while문 만들기

```
>>> prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0

while number != 4:
    print(prompt)
    number = int(input())

1. Add
2. Del
3. List
4. Quit

Enter number:

```

# for문

1. 

```

for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1

```

```

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

```

2. 다양한 for문의 사용

```

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
3
7
11

```

3. for문과 함께 자주 사용하는 range 함수

```

a = range(10)

a => range(0, 10)

0부터 10 미만의 숫자를 포함하는 range 객체를 만들어준다.

marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if makrs[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

```

4. for와 range를 사용한 구구단

```

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end = " ")
    print('')

```

5. 리스트 내포 사용하기

```

a = [1, 2, 3, 4]

result = []

for num in a:
    result.append(num * 3)

result = [3, 6, 9, 12]


리스트 내포를 사용하면?

result = [num * 3 for num in a]

짝수에만 3을 곱하여 담고 싶다면?

result = [num * 3 for num in a if num % 2 == 0]

```

6. 표현식 for 항목 in 반복 가능 객체 if 조건

7. 여러 개 사용도 가능한데.. 잘 쓰려나?


```

result = [x*y for x in range(2, 10)
    for y in range(1, 10)]

```

# 함수

# 파이썬 함수의 구조

```

def 함수 이름(매개변수):
    수행할 문장1
    수행할 문장2

def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b) = 7

```

# 입력값이 몇 개가 될지 모를 때??

```

def 함수 이름(*매개변수):
    수행할 문장


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

add_many(1, 2, 3, 4, 5)

add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

응용한다면?

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5) = 15

result = add_mul('mul', 1, 2, 3, 4, 5) = 120

```

2. 키워드 파라미터

```

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name='foo', age=3)

{'age' : 3, 'name' : 'foo'}

매개변수 이름 앞에 **을 붙이면 매개변수 kwagrs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.

```

# 함수의 결괏값은 언제나 하나이다

```

def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4) = (7, 12)

result1, result2 = add_and_mul(3, 4)

result1 = 7

result2 = 12

```

# lambda

```

def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

lambda 매개변수1, 매개변수2, ... : 매개변수를 사용한 표현식

add = lambda a, b: a+b
result = add(3, 4) = 7

```

# 사용자 입력과 출력

```

input의 사용

a = input()

Life is too short

a

'Life is too short'

input("질문 내용")

number = input("숫자를 입력하세요: ")


```

# 프린트 사용법

```

큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다

문자열 띄어쓰기는 콤마로 한다.

print("aa" + "BB") aaBB
print("aa" "BB") = aaBB
print("aa", "bb") = aa, bb

```

# 파일 읽고 쓰기

```

f = open("새파일.txt", 'w')
f.close()

파일 객체 = open(파일 이름, 파일 열기 모드)

파일 열기 모드

r 읽기 모드 - 파일을 읽기만 할 때 사용

w 쓰기 모드 - 파일에 내용을 쓸 때 사용

a 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용


f = open("새파일.txt", 'w')

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

```

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

1. readline 함수 사용하기

```


f = open("새파일.txt", 'r') <- r
line = f.readline()
print(line)
f.close()

1번째 줄입니다.

만약 모든 줄을 읽어서 화면에 출력하고 싶다면 다음과 같이 작성하면 된다.

f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

readline()은 더이상 읽을 줄이 없을 경우 None을 출력한다.


```

2. readlines 함수 사용하기

```

f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines
    print(line)
f.close()

readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.

따라서 위 예에서 lines는 리스트 ["1번째 줄입니다", "2번째 줄입니다", ...]

```

3. read 함수 사용하기

```

f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f.read()는 파일의 내용 전체를 문자열로 돌려준다. 

```

# 파일에 새로운 내용 추가하기

```

쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다.

하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있다.

이런 경우에는 파일을 추가 모드('a')로 열면 된다.

f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

파일을 열고 닫는 것을 자동으로 처리할 수 있는 with

with open("새파일.txt", 'w') as f:
    f.write("Life is too short")

```

# 명렬 프롬포트 명령어 [인수1, 인수2]

```

sys.py 파일이라고 하면

import sys

args = sys.argv[1:]

for i in args:
    print(i.upper(), end = ' ')

python sys.py life is too short

=> LIFE IS TOO SHORT



```

# 클래스 구조 만들기

```

class FourCal:
    pass

a = FourCal()
type(a)
<<class '__main__.FourCal'>>

```

# 객체에 숫자 지정할 수 있게 만들기

```

a.setData(4, 2)

class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second

파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.

객체를 호출할 때 객체 자신이 전달되기 때문에 self를 사용한 것이다.

메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징이다.

```


```

a = FourCal()
b = FourCal()
a.setData(4, 2)
b.setData(3, 7)
id(a.first) //a의 first주소
1839194944
id(b.first) //b의 first주소
1839194928

주소 값이 서로 다르므로 각각 다른 곳에 그 값이 저장된다는 것을 알 수 있다. 

객체변수는 그 객체의 고유 값을 저장할 수 있는 공간이다.

객체변수는 다른 객체들 영향받지 않고 독립적으로 그 값을 유지한다는 점을 꼭 기억하자.

```

1. 더하기 기능 만들기

```

class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setData(4, 2)
print(a.add())
6

```

2. 곱하기 나누기 빼기 만들기

```

class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result

```

3. 클래스에 생성자 추가하기

```

class FourCal:
    def __init__(self, first, second)
        self.first = first
        self.second = second

a = FourCal(2, 4)

```

# 클래스의 상속

1. FourCal 클래스에 a^b(a의 b제곱)을 구할 수 있는 기능을 추가해 보자.

```

class MoreFourCal(FourCal):
    pass

클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.

class 클래스 이름(상속할 클래스 이름)

a = MoreFourCal(4, 2)
a.add()
a.mul()

왜 상속을 해야할까?

보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기능을 변경하려고 할 때 사용한다.

기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
a.pow()
16

```

# 메서드 오버라이딩

```

a = FourCal(4, 0)
a.div()

4를 0으로 나누려고 하면 ZeroDevisionError 오류가 발생 

하지만 0으로 나눌 때 오류가 아닌0을 돌려주도록 만들고 싶다면?

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다.

```

# 클래스 변수

1. 객체변수는 다른 객체들에 영향받지 않고 독립적으로 그 값을 유지한다는 점을 이미 알아보았다.

2. 이번에는 객체변수와는 성격이 다른 클래스 변수에 대해 알아보자.

```

class Family:
    lastName = "김"

Family 클래스에 선언한 lastName이 바로 클래스 변수이다.

클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다.

print(Family.lastName)
김

a = Family()
b = Family()

print(a.lastName)
김

print(b.lastName)
김

Family 클래스의 lastName을 "박"이라는 문자열로 바꾼다면?

Family.lastName = "박"

print(a.lastName)
박

print(b.lastName)
박

클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastName 값도 모두 변경된다는 것을 확인할 수 있다.

즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다.

id(Family.lastName)
4480159136
id(a.lastName)
4480159136
id(b.lastName)
4480159136

id값이 모두 같으므로 모두 같은 메모리를 가리키고 있다.

클래스 변수를 가장 늦게 설명하는 이유는 클래스에서 클래스 변수보다는 객체 변수가 훨씬 중요하기 때문이다.

실무 프로그래밍을 할 때도 클래스 변수보다는 객체변수를 사용하는 비율이 훨씬 높다.

```

# 모듈

1. 모듈이란 함수나 변수 또는 클래스를 모아 높은 파일이다.

2. 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있다.

```

# mod1.py
def add(a, b):
    return a + b
def sub(a, b):
    return a - b

add함수와 sub함수만 있는 파일mod1.py를 만들고 저장하자.

이mod1.py 파일이 바로 모듈이다.

파일이 저장된 디렉터리로 이동한 다음

import mod1

print(mod1.add(3, 4))

import의 사용 방법

import 모듈 이름

mod1.add, mod1.sub처럼 쓰지 않고 add, sub처럼 모듈 이름 없이 함수 이름만 쓰고 싶을 경우도 있을 것이다.

이럴 때는 'from 모듈 이름 import 모듈 함수'를 사용하면 된다.

from 모듈 이름 import 모듈 함수

from mod1 import add
add(3, 4)
7

add 함수와 sub 함수를 둘 다 사용하는 두 가지 방법

from mod1 import add, sub

from mod1 import *

import *는 mod1.py의 모든 함수를 불러서 사용하겠다는 뜻이다.

```

```

__name__ 변수란?

파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.

만약 pyhon mod1.py 처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.

하지만 파이썬 쉘이나 다른 파이썬 모듈에서 mod1을 import할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.

```

# 패키지

1. 패키지는 도트(.)를 사용하여 파이썬 모듈을 계층적으로 관리할 수 있게 해준다.

2. 예를 들어 모듈 이름이 A.B인 경우에 A는 패키지 이름이 되고 B는 A패키지의 B 모듈이 된다.

```

__init__.py의 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.

파이썬 3.3버전부터는 없어도 패키지로 인식하지만 하위 호환이 필요하다면 파일을 생성하는 것이 안전한 방법이다.

```

# 예외 처리

1. 파이썬은 try, except를 사용해서 예외적으로 오류를 처리할 수 있게 해준다.

```

자주 등장하는 오류

0으로 나누기, 없는 파일 읽기, 없는 인덱스 불러오기

try, except문

try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...

[] 기호를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다.

즉 except 구문은 다음 3가지 방법으로 사용할 수 있다.

1.  try:
        ...
    except:
        ...

2.  try:
        ...
    except 발생 오류:
        ...


3.  try:
        ...
    except 발생 오류 as 오류 메시지 변수:
        ...

try :
    4 / 0
except ZeroDivisionError as e:
    print(e)

결괏값 : division by zero


finally 절 사용하기

예외 발생 여부에 상관없이 항상 수행된다.

f = open('foo.txt', 'w')

try:
    #수행
finally:
    f.close()

예외 발생 여부와 관계없이 finally 절에서 f.close()로 열린 파일을 닫을 수 있다.

여러 오류 사용하기?

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)



```

# 오류 일부러 발생시키기

1. 파이썬은 raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.

```

예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우가 있을 수 있다.

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird): //Eagle클래스는 Bird 클래스를 상속 받음
    pass


eagle = Eagle()
eagle.fly()

Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에 Bird 클래스의 fly 함수가 호출된다.

그리고 raise 문에 의해 NotImplementedError 가 발생한다.

```

# 예외 만들기

```

프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용한다.

예외는 다음과 같이 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")

천사가 한 번 출력된 후 MyError가 발생한다.

예외 처리 했을 경우?

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명")

오류 메시지를 사용하고 싶다면?

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

이 상태로는 오류 메시지를 구현하지 않았기 때문에 아무것도 출력되지 않음

오류 메시지가 보이게 하려면 오류 클래스에 다음과 같은 __str__ 메서드를 구현해야 한다.

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다"


```

# 내장 함수

```

Don't Reinvent The Wheel, 이미 있는 것을 다시 만드느라 쓸데없이 시간을 낭비하지 말라

= 바퀴를 다시 발명할 필요는 없다.

```

1. abs = 절대 값 반환

- abs(-3) = 3

2. all = 반복 가능한 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 반환

- all([1, 2, 3]) = True

- all([1, 2, 3, 0]) = False

3. any = x 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때만 False를 돌려준다.

- all([1, 2, 3, 0]) = True

4. chr = chr(i)는 아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수

- chr(97) = 'a' 

- chr(48) = '0'

5. dir = dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.

다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여주는 예이다.

```

dir([1, 2, 3])
['append', 'count', 'extend', 'index', 'insert', 'pop', ...]

dir({'1' : 'a'})
['clear', 'copy', 'get', 'has_key', 'items', 'keys', ...]


```

6. divmod = divmod(a, b)는 2개의 숫자를 입력으로 받아서 몫과 나머지를 튜플 형태로 돌려주는 함수

- divmod(7, 3) = (2, 1) //2는 몫, 1은 나머지\

7. enumerate = 열거하다. 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.

```

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

0 body
1 foo
2 bar

for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때 enurmerate 함수를 사용하면 매우 유용하다.

```

8. eval = eval(expression)은 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수

- eval('1+2') = 3

- 보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.

9. filter = 무엇인가를 걸러낸다. 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.

```

그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서 돌려준다.

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(num)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

리스트를 입력값으로 받아 각각의 요소를 판별해서 양수 값만 돌려주는 함수

filter를 사용한다면?

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

간결하다.

positive를 구현하지 않고 lambda를 사용한다면?

list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))

```

10. hex = hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수

- hex(234) = '0xea'

11. id = id(object)는 객체를 입력받아 객체의 고유 주소 값(reference)을 돌려주는 함수

- a = 3, id(a) = 135072304

12. input = input([prompt])은 사용자 입력을 받는 함수

13. int = int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수

- int('3') = 3, int('3.4') = 3

- int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.

- int('1A', 16) = 26 //16진수 1A를 10진수로 변환

- int('11', 2) = 3 //2진수 11을 10진수로 변환

14. isinstance = isinstance(object, class)는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.

```

입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.

class Person: pass

a = Person() //Person 클래스의 인스턴스 a 생성

isinstacne(a, person) //a가 Person 클래스의 인스턴스인지 확인
True

b = 3

isinstance(b, person)

//False

```

15. len = len(s)는 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수

- len("python") = 6

- len([1, 2, 3]) = 3

- len((1, 'a')) = 2

16. list = list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수

- list("python") = ['p', 'y', 't', 'h', 'o', 'n']

- list((1,2 ,3)) = [1, 2, 3]

17. map = map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.

```

map은 입력 받은 자료형의 각 요소를 f가 수행한 결과를 묶어서 돌려주는 함수이다.

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

위 예를 map함수를 사용하면

def two_times(x): return x*2

list(map(two_times, [1, 2, 3, 4]))
[2, 4, 6, 8]

lambda를 사용한다면?

list(map(lambda a: a*2, [1, 2, 3, 4]))
[2, 4, 6, 8]


```

18. max = max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수

- max([1, 2, 3]) = 3

- max("python") = 'y'

19. min = min(iterable)은 max함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수

- min([1, 2, 3]) = 1

- min("python") = 'h'

20. oct = oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수

- oct(34) = '0o42'

21. open = open(filename, [mode])은 '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 돌려주는 함수, 읽기 방법('mode')을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.

- b는 바이너리 모드로 파일 열기, b는 w, r, a와 함께 사용한다

- f = open("binary_file", 'rb')

- f = open("read_mode.txt", 'r')


22. ord = ord(c)는 문자의 아스키 코드 값을 돌려주는 함수

- ord('a') = 97, ord('0') = 48

23. pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수

- pow(2, 4) = 16

24. range = range([start,] stop [,step])는 for문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.

```

인수가 하나일 경우

range 함수는 0부터 시작한다.

list(range(5)) 

[0, 1, 2, 3, 4]

인수가 2개일 경우

입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자, 단 끝 숫자는 해당 범위에 포함되지 않는다는 것

list(range(5, 10))

[5, 6, 7, 8, 9]

인수가 3개인 경우

세 번째 인수는 숫자 사이의 거리를 말한다.

list(1, 10, 2)

[1, 3, 5, 7, 9]

```

25. round = round(number, [, ndigits]) 함수는 숫자를 입력받아 반올림 해주는 함수

- round(4.6) = 5, round(4.2) = 4

- round(5.678, 2) = 5.68 // 실수 5.678을 소수점 2자리가지만 반올림하여 표시

26. sorted = sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수

- sorted([3, 1, 2]) = [1, 2, 3]

27. str = str(object)은 문자열 형태로 객체를 반환하여 돌려주는 함수

- str(3) = '3'

28. sum = sum(iterable)은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수

- sum([1, 2, 3]) = 6

29. tuple = tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수. 

- tuple("abc") = ('a', 'b', 'c')

30. type = type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수

```

type("abc")

<class 'str'> //'abc'는 문자열 자료형

type([])

<class 'list'>

type(open("test", 'w'))

<class '_io.TextIOWrapper> 파일 자료형

```

31. zip = zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수

```

list(zip([1, 2, 3], [4, 5, 6]))

[(1, 4), (2, 5), (3, 6)]

list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))

[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

list(zip("abc", "def"))

[('a', 'd'), ('b', 'e'), ('c', 'f')]


```

# 외장 함수

1. 자주 사용되고 꼭 알아 두면 좋은 라이브러리

2. sys = sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.

```

# argv_test.py

import sys
print(sys.argv)

python argv_test.py you need python

['argv_test.py', 'you', 'need', 'python']

python 명령어 뒤의 모든 것들이 공백을 기준으로 나뉘어서 sys.argv 리스트의 요소가 된다.



```

3. 강제로 스크립트 종료하기 - sys.exit()

4. 자신이 만든 모듈 불러와 사용하기 - sys.path()

- sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타낸다.

- 즉 이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다.


```

# path_append.py
import sys
sys.path.append("C:/doit/Mymod)

sys.path.append를 사용해 경로 이름을 추가할 수 있다.

```

4. pickle = pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.

```

pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법

import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

pickle.dump로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태로 그대로 불러오는 예

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
{1: 'python', 2: 'you need'}


언제쓰지?

```

5. OS - OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다

```

os.environ은 현재 시스템의 환경 변수 값을 보여 준다.

import os
os.environ

시스템 정보를 보여준다.

os.environ['PATH']

시스템의 PATH 환경 변수를 보여준다.


디렉터리 위치 변경하기 -os.chdir

현재 디렉터리 위치를 변경할 수 있다.

os.chdir("C:\Windows")



디렉터리 위치 돌려받기 - os.getcwd

os.getcwd는 현재 자신의 디렉터리 위치를 돌려준다.

os.getcwd()

시스템 명령어 호출하기 -os.system

os.system("dir")

실행한 시스템 명령어의 결괏값 돌려받기 os.popen

f = os.popen("dir")

읽어 들인 파일 객체의 내용을 보기 위해서는?
print(f.read())

os.mkdir(dir) - 디렉터리 생성
os.rmdir(dir) - 디렉터리 삭제
os.unlink(fileName) - 파일 삭제
os.rename(src, dst) - src 파일이름을 dst로 변경

```

6. shutil = shutil은 파일을 복사해 주는 파이썬 모듈이다.

```

import shutil
shutil.copy("src.txt", "dst.txt")

src.txt 파일과 동일한 내용이 dst.txt에 복사되고 dst.txt파일이 존재할 경우 덮어 씌운다.

```

7. glob 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다. 이럴 때 사용하는 모듈이 glob이다.

```

디렉터리에 있는 파일들을 리스트로 만들기 - glob(fileName)

glob 모듈은 디렉터리 안의 파일들을 읽어서 돌려준다.

*.? 등 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다.

다음은 C:/doit 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일을 모두 찾아서 읽어 들이는 예이다.

import glob
glob.glob("c:/doit/mark*")
['C:/doit\\marks1.py', 'C:/doit\\marks2.py', 'C:/doit\\marks3.py', ...]

```

8. tempfile - 파일을 임시로 만들어서 사용할 때 유용한 모듈, tempfile.mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.

```

import tempfile
filename = tempfile.mktemp()
filename
~~

tempfile.TemporyFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다.

이 파일은 기본적으로 wb를 갖는다. f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.

import tempfile
f = tempfile.TemporaryFile()
f.close()

```

9. time - 시간과 관련된 time 모듈

```

time.time - UTC를 사용하여 현재 시간을 실수 형태로 돌려주는 함수

import time
time.time()
988458015~...

time.localtime

time.localtime은 time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초, ...의 형태로 바꾸어 주는 함수

time.localtime(time.time())
time.struct_time(tm_year=2013, tm_mon=5, ...)

time.asctime은 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.

time.asctime(time.localtime(time.time()))
'Sat Apr 28 20:50:20 2001'

time.ctime은 항상 현재 시간을 time.asctime 형태로 돌려준다.

time.ctime
'Sat Apr 28 20:50:20 2001'

time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))

strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.

%a 요일 줄임말 Mon
%b 달 줄임말 Jan
%c 날짜와 시간 출력 06/01/01 17:22:22
%d 날(day) [00, 31]

...


import time
time.strftime('%x', time.localtime(time.time()))
'05/01/01'

time.strftime('%c', time.localtime(time.time()))
'05/01/01 17:22:22'

time.sleep 함수는 주로 루프 안에서 많이 사용한다.

이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다.

import time
for i in range(10):
    print(i)
    time.sleep(1)

1초 간격으로 0부터 9까지의 숫자를 출력한다. 

```

10. calendar - calendar는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.

```

calendar.calendar(연도)로 사용하면 그 해의 전체 달력을 볼 수 있다.

calendar.prcal(연도)를 사용해도 같은 결과를 얻을 수 있다.

calendar.prmonth(2015, 12) 2015년 12월의 달력만 보여 준다.

calendar.weekday(연도, 월, 일) 그 날짜에 해당하는 요일 정보를 돌려준다.

calendar.monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.

calendar.monthrange(2015, 12) => (1, 31)

2015년 12월 1일은 화요일이고 이 달은 31일까지 있다는 것을 보여줌

0 = 월요일 ~ 6 = 일요일

```

11. random - random은 난수를 발생시키는 모듈이다.

```

0.0에서 1.0 사이의 실수 중에서 난수 값을 돌려주는 예

import random
random.random()
0.534~~~~~~~23

1에서 10 사이의 정수 중에서 난수 값

random.randint(1, 10)
6

재미있는 함수?

# random_pop.py
import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))

random_pop함수는 random 모듈의 choice 함수를 사용하여 좀 더 직관적으로 만들 수도 있다.

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

random.choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 돌려준다.

리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 사용하면 된다.

import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
data
[5, 1, 3, 4, 2]



```

12. webbrowser - 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다.

```

import webbrowser
webbrowser.open("http://google.com")

웹 브라우저가 이미 실행된 상태라면 입력 주소로 이동하고, 실행되지 않은 상태라면 새로 웹 브라우저를 실행한 후 해당 주소로 이동한다.

open_new 함수는 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리게 한다.

webbrowser.open_new("http://google.com")



```

13. 스레드를 다루는 threading 모듈


```


# thread_test.py
import time

def long_task(): //5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1) //1초간 대기
        print("working:%s\n" % i)

print("Start")

for i in ragne(5):
    long_task()

print("End")

이 프로그램은 5초의 시간이 걸리는 long_task 함수를 5회 호출하여 25초가 걸린다.

쓰레드를 사용한다면?

# thread_test.py
import time
import threading // 스레드를 생성하기 위한 threading 모듈

def long_task(): //5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1) //1초간 대기
        print("working:%s\n" % i)

print("Start")

threads = []
for i in ragne(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start() - 스레드를 실행한다.


print("End")

5초 정도에 수행 된다.

threading.Thread를 사용하여 만든 스레드 객체가 동시 작업을 가능하게 해 주기 때문이다.

위 프로그램을 실행해보면 "start" + "end" 가 먼저 출력되고 그 이후에 스레드의 결과가 출력되는 것을 확인할 수 있고, 프로그램 또한 정상 종료되지 않는다.

해당 부분을 제어하기 위해서는?

# thread_test.py
import time
import threading // 스레드를 생성하기 위한 threading 모듈

def long_task(): //5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1) //1초간 대기
        print("working:%s\n" % i)

print("Start")

threads = []
for i in ragne(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start() - 스레드를 실행한다.

for t in threads:
    t.join() // join으로 스레드가 종료될 때까지 기다린다.

print("End")

```

# 정규 표현식

1. 정규 표현식(Regular Expressions)은 복잡한 문자열을 처리할 때 사용하는 기법

# 메타 문자

```

. ^ $ * + {} [] \ | ()

문자 클래스 []

[] 사이의 문자들과 매치

[abc] 
a yes
before yes
dude no

[]안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(From-To)를 의미한다. 예를 들어 [a-c]라는 정규 표현식은 [abc]와 동일하고 [0-5]는 [012345]와 동일하다

[a-zA-Z]알파벳 모두, [0-9]숫자

문자 클래스 안에 ^ 메타 문자를 사용할 경우에는 반대라는 의미를 갖는다.

[^0-9] 숫자가 아닌 문자만 매치

정규 표현식 

\d = [0-9]
\D = [^0-9]

\s = whitespace 문자(space or tab처럼 공백을 표현하는 문자와 매치)  = [\t\n\r\f\v]와 동일하다
\S = whitespace 문자가 아닌것과 매치 [^\t\n\r\f\v]

\w = 문자 + 숫자와 매치 [a-zA-Z0-9_]와 동일하다
\W = 문자 + 숫자가 아닌 문자와 매치 [^a-zA-Z0-9_]와 동일

대문자 = 소문자의 반대 의미

```

```

Dot(.)

정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치

a.b = a와 b사이에 줄바꿈 문자를 제외한 어떤 문자가 들어가도 매치


aab yes
a0b yes
abc no = a와b사이에 어떤 문자 하나라도 있어야함

반복(*)

ca*t = 문자 바로 앞에 있는 a가 0번 이상 반복되면 매치

ct yes
cat yes
caaaaat yes

반복(+)

ca+t = 문자 바로 앞에 있는 a가 1번 이상 반복되면 매치

ct no <= *와 다른 부분
cat yes
caaaat yes

반복({m,n}, ?)

[3,] 을 사용하면 반복 횟수가 3이상
[,3] 을 사용하면 반복 횟수가 3이하

{m}

ca{2}t

cat no
caat yes

{m, n}

ca{2, 5}t a가 2 ~ 5번 반복되면 매치

cat no
caat yes
caaat yes
caaaaat yes

?

ab?c = b가 0~1번 사용되면 매치 ?는 {0, 1}을 의미한다

abc yes
ac yes


```

# 정규 표현식을 지원하는 re 모듈

```

import re
p = re.compile('ab*')

정규식을 사용한 문자열 검색

match() 문자열의 처음부터 정규식과 매치되는지 조사

search() 문자열 전체를 검색하여 정규식과 매치되는지 조사

findall() 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.

finditer() 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.

import re
p = re.compile('[a-z]+')

match

m = p.match("python")
print(m)
<re.Match object span=(0,6), match='python'>

m = p.match("3 python")
print(m)
None

처음에 나오는 문자 3이 정규식 [a-z]+에 부합되지 않으므로 None을 돌려준다.

p = re.compile("정규 표현식")
m = p.match("조사할 문자열")
if m:
    print("match found:", m.group())
else:
    print("no match")

search

m = p.search("python")
print(m)
<re.Match object span(0, 6), match='python'>

m = p.search("3 python")
print(m)
<re.Match object span(2, 8), match='python'>

문자열을 처음부터 검색하는 것이 아니라 전체를 검색하기 때문에 문자열이 매치된다.

findall

result = p.findall("life is too short")
print(result)
['life', 'is', 'too', 'short']
각각 정규식과 매치해서 리스트로 돌려준다.

finditer

result = p.finditer("life is too short")
print(result)
<callable_iterator object at 0x01F5E390>
for r in result: print(r)

<re.Match object; span=(0, 4), match='life'>
...


```

# match 객체의 메서드

```

어떤 문자열이 매치되었는지?

매치된 문자열의 인덱스는 어디부터 어디까지인지?

group() 매치된 문자열을 돌려준다
start() 매치된 문자열의 시작 위치를 돌려준다.
end() 매치된 문자열의 끝 위치를 돌려준다.
span() 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.


import re
p = re.compile("[a-z]+")
m = p.match("python")
m.group()
'python'
m.start()
0
m.end()
6
m.span()
(0, 6)

m = p.search("3 python")
m.group()
'python'
m.start()
2
m.end()
8
m.span()
(2, 8)

compile과 match를 한번에

보통 한 번 만든 패턴 객체를 여러번 사용해야 할 때는 re.compile을 사용하지만 그 외는 이 방법을 사용한다.

m = re.match("[a-z]+", "python")



```

# 컴파일 옵션

```

DOTALL S dot 문자(.)가 줄바꿈 문자를 포함하여 모든 문자와 매치한다.
IGNORECASE I 대-소문자에 관계없이 매치한다.
MULTILINE M 여러 줄과 매치한다. 
VERBOSE X verbose 모드를 사용한다. (정규식을 보기 편하게 만들 수도 있고 주석 등을 사용할 수도 있따?)

DOTALL, S

import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)
None

p = re.compile('a.b', re.DOTALL)
m - p.match('a\nb')
print(m)
<re.Match object; span=(0,3), match='a\nb'>

IGNORECASE, I

p = re.compile('[a-z]', re.I)
p.match('python')
<re.Match object; span=(0, 1), match='p'>
p.match('Python')
<re.Match object; span=(0, 1), match='P'>

MULTILINE, M

p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.final(data))

['python one']

^ 메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶은 경우 사용하는 re.MULTILINE

p = re.compile("^python\s\w+", re.M)

['python one', 'python two', 'python three']


VERBOSE, X

지금껏 알아본 정규식보다 복잡한 정규식일 경우 주석 또는 줄 단위로 구분하기 위해 사용한다.

charref = re.compile("r'&[#][0[0-7]+ ...])

charref = re.compile(r"""
&[#] # start of a numeric
(
    0[0-7]+ #octal form
  | [0-9]+  #decimal form
  | x[0-9a-fA-F] # hexadecimal form
)
;
""", re.VERBOSE)

```

# 백슬래시 문제

```

\section

p = re.compile('\\\\section')

p = re.compile(r'\\section');

r' => Raw String?



```

# 메타 문자

```

| 메타 문자는 or과 동일한 의미로 사용. A|B라는 정규식이 있다면 A 또는 B라는 의미가 된다.

^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다. 

print(re.search("^Life", "Life is too short"))
match
print(re.search("^Life", "My Life is too short"))
None

$ 메타 문자는 ^ 문자열의 끝과 매치함을 의미한다.

print(re.search('short', "Life is too short"))
match
print(re.search('short', "Life is too short, you need python"))
None

\A 메타 문자는 문자열의 처음과 매치됨을 의미한다. 해당 부분은 멀티라인을 사용했을 때 ^와 다르다.

\Z 메타 문자는 문자열의 끝과 매치됨을 의미한다. 해당 부분을 멀티라인을 사용했을 때 $와 다르다.

\b 메타 문자는 단어 구분자이다. 보통 단어는 whitespace에 의해 구분된다.

p = re.compile(r'\bclass\b')

print(p.search("no class at all"))
match
print(p.search("no declassfied algorithm"))
None

\B 메타 문자는 \b와 반대.


```

# 그루핑

```

ABC 문자열이 계속해서 반복되는지 조사하는 정규식을 작성한다면?

(ABC)+

p = re.compile("(ABC)+")
m = p.search("ABCABCABC OK?")
print(m)
<re.Match; span=(0, 9), match='ABCABCABC'>
print(m.group())
'ABCABCABC'

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")

이름 + "" + 전화번호 형태의 문자열을 찾는 정규식

이렇게 매치된 문자열 중에서 이름만 뽑아내고 싶다면?

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))
park

\w+ 부분을 그룹(\w+)으로 만들면 match 객체의 group(index) 메서드를 사용하여 그루핑된 부분의 문자열만 뽑아낼 수 있다.

group(0) 매치된 전체 문자열
group(n) n 번째 그룹에 해당하는 문자열

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))
010-1234-1234

전화번호 중에서 국번만 뽑아내고 싶다면?

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))
010

그룹이 중첩되어 있는 경우는 바깥쪽부터 시작하여 안쪽으로 들어갈수록 인덱스가 증가한다.

그루핑된 문자열 재참조하기?

p = re.compile(r'(\b\w+)\s+\1')

(그룹) + "" + 그룹과 동일한 단어와 매치됨을 의미한다..?

이렇게 정규식을 만들게 되면 2개의 동일한 단어를 연속적으로 사용해야만 매치된다.

이것을 가능하게 해주는 것이 바로 재참조 메타 문자인\1이다.

\1은 정규식의 그룹 중 첫 번째 그룹을 가리킨다.

p.search("paris in the the string").group()
'the the'




```

# 그루핑된 문자열에 이름 붙이기

```

p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")

?P<그룹 이름>


m = p.search("park 010-1234-1234")
print(m.group("name"))



```

# 전방탐색

```

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group)
http:

http: 라는 검색 결과에서 :을 제외하고 출력하려면?

이럴 때 사용할 수 있는 것이 바로 전방 탐색이다.

전방 탐색에는 긍정과 부정의 2종류가 있다.

(?=...) 긍정 = ...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

(?!...) 부정 = ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

p = re.complie(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
http

기존 정규식과 검색에서는 동일한 효과를 발휘하지만 :에 해당하는 문자열이 정규식 엔진에 의해 소비되지 않아(검색에는 포함되지만 검색 결과에는 제외됨) 검색 결과에서는 :이 제거된 후 돌려주는 효과가 있다.

.*[.].*$

파일이름 + . + 확장자

확장자가 bat인 파일은 제외해야 한다면?

부정형 전방 탐색 이용

.*[.](?!bat$).*$

확장자가 bat가 아닌 경우에만 통과된다.

bat 문자열이 있는지 조사하는 과정에서 문자열이 소비되지 않으므로 bat가 아니라고 판단되면 그 이후 정규식 매치가 진행된다.

exe 역시 제외하라는 조건이 추가되더라도 다음과 같이 표현할 수 있다.

.*[.](?!bat$|exe$).*$

문자열 바꾸기

sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 잇다.

p = re.compile("(blue|white|red"))
p.sub('colour', 'blue socks and red shoes')
'colour socks and colour shoes

딱 한번만 바꾸고 싶은 경우?

count=1 변수를 넘겨주면 된다.


p = re.compile("(blue|white|red"))
p.sub('colour', 'blue socks and red shoes', count=1)
'colour socks and colour shoes

p.subn을 사용하면 몇 번의 바꾸기가 발생했는지까지 같이 튜플로 돌려준다.

sub 메서드를 사용할 때 참조 구문 사용하기

p = re.compile(r"(?P<name>\w+)\s+\(?P<phone>(\d+)[-]\d+[-]\d+"))
print(p.sub("\g<phone><name>", "park 010-1234-1234"))
010-1234-1234 park

이름 + 전화번호의 문자열을 전화번호 + 이름으로 바꾸는 예이다.

sub의 바꿀문자열 부분에 \g(그룹이름)을 사용하면 정규식의 그룹이름을 참조할 수 있게 된다.

```