# let

1. https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let#%EC%8B%9C%EA%B0%84%EC%83%81_%EC%82%AC%EA%B0%81%EC%A7%80%EB%8C%80

2. let 명령문은 블록 스코프의 범위를 가지는 지역 변수를 선언하며, 선언과 동시에 임의의 값으로 초기화할 수도 있다.

```

let x = 1;

if (x === 1) {
    let x = 2

    console.log(x); //2
}

console.log(x) //1


```

# 구문

```

let var1 [= value1] [, var2 [=value2]] [, ..., varN [= valueN]];

```

# 매개변수

1. nameN

- 변수 이름, 모두 유효한 JavaScript 식별자여야 한다.

2. valueN Optional

- 각각의 변수 선언에 대해, 유효한 JavaScript 표현식을 지정해 변수의 초기 값을 지정할 수 있다.

3. 이 구문 대신 구조 분해 할당을 사용해서 변수를 선언할 수도 있다.

```

let {bar} = foo; // foo = { bar : 10, baz: 12};

// 10의 값을 가진 'bar' 변수를 생성

위 말은 무슨말인지 잘 모르겠다;

```

# 설명

1. let을 사용하면 블록 명령문이나 let을 사용한 표현식 내로 범위가 제한되는 변수를 선언할 수 있다.

2. 이는 let이 var 키워드와 다른 점으로, var는 변수를 블록을 고려하지 않고 현재 함수(또는 전역 스코프) 어디에서나 접근할 수 있는 변수를 선언한다.

3. 또한 let은 파서가 구문을 평가해야만 변수를 값으로 초기화한다는 점도 var와 다르다.

4. const와 마찬가지로 let 역시 전역 범위 선언에 사용(최상위 스코프 선언)해도 window 객체에 새로운 속성을 추가하지 않습니다.

5. let 변수가 가진 다양한 문제는, let 변수 선언을 현재 스코프의 맨 위에서 수행해서 피할 수 있다.

# 예제

# 스코프 규칙

1. let으로 선언한 변수는 자신을 선언한 블록과 모든 하위 블록을 스스로의 스코프로 가진다.

2. 이런 점에서는 let이 var와 유사하다.

3. 그러나 둘의 중요한 차이는, var의 경우 '자신을 선언한 블록'이 아니라, 자신의 선언을 포함하는 함수라는 점이다.

```

function varTest() {
    var x = 1
    if (true) {
        var x = 2;
        console.log(x); //2
    }
    console.log(x); //2
}

function letTest() {
    let x = 1;
    if (true) {
        let x = 2; //다른 변수
        console.log(x); // 2
    }
    console.log(x); // 1
}

```

4. 프로그램 최상위에서 사용할 경우 var는 전역 객체에 속성을 추가하지만 let은 추가하지 않는다.

```

var x = 'global'
let y = 'global'
console.log(this.x); // "global"
console.log(this.y); // undefined

```

# 시간상 사각지대

1. let 변수는 초기화하기 전에는 읽거나 쓸 수 없습니다(선언 구문에 초기 값을 지정하지 않은 경우 undefined로 초기화함)

2. 초기화 전에 접근을 시도하면 ReferenceError가 발생한다.

3. 변수 스코프의 맨 위에서 변수의 초기화 완료 시점까지의 변수는 "시간상 사각지대"(Temporal Dead Zone, TDZ)에 들어간 변수라고 표현한다.

```

function do_something() {
    console.log(bar) // undefined
    console.log(foo) // ReferenceError
    var bar = 1
    let foo = 2
}

```

4. "시간상" 사각지대인 이유는, 사각지대가 코드의 작성 순서(위치)가 아니라 코드의 실행 순서(시간)에 의해 형성되기 때문이다.

5. 예컨대 아래 코드의 경우 let 변수 선언 코드가 그 변수에 접근하는 함수보다 아래에 위치하지만, 함수의 호출 시점이 사각지대 밖이므로 정상 동작한다.

```
{
    // TDZ가 스코프 맨 위에서부터 시작
    const func = () => console.log(letVar); //OK

    //TDZ 안에서 letVar에 접근하면 ReferenceError

    let letVar = 3; // letVar의 TDZ종료

    func(); //TDZ 밖에서 호출함
}

```

# 기타 예제

1. 블록 내에서 사용한 경우 let은 변수의 스코프를 해당 블록으로 제한한다.

2. var는 스코프를 함수로 제한한다는 차이에 주의하라

```

var a = 1;
var b = 2;

if (a === 1) {
    var a = 11;
    let b = 22;

    console.log(a); //11
    console.log(b); //22
}

console.log(a); 11
console.log(b); 2

```

3. 그러나 var와 let을 아래와 같이 사용하면 SyntaxError이다. 호이스팅으로 인해 var가 블록 최상단으로 끌어 올려져, 변수 재선언을 하는 것과 같아지기 때문이다.

```

let x = 1;

{
    var x = 2; //재선언으로 인한 SyntaxError
}

```