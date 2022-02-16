# var

1. var문은 변수를 선언하고, 선택적으로 초기화할 수 있다.

```

var x = 1;

if (x === 1) {
    var x = 2;

    console.log(x); // 2
}

console.log(X); // 2

```

# 설명

1. 어디에 선언이 되어있든 간에 변수들은 어떠한 코드가 실행되기 전에 처리가 된다.

2. var로 선언된 변수의 범위는 현재 실행 문맥인데, 그 문맥은 둘러싼 함수, 혹은 함수의 외부에 전역으로 선언된 변수도 될 수 있다.

3. 선언된 변수들의 값 할당은 할당이 실행될 때 전역변수(이것은 전역 오브젝트의 프로퍼티가 된다.)처럼 생성이 된다.

4. 선언된 변수들과 선언되지 않은 변수들의 차이점은 다음과 같다.

5. 선언된 변수들은 변수가 선언된 실행 콘텍스트(execution context) 안에서 만들어진다.

6. 선언되지 않은 변수들은 항상 전역변수 이다.

```

function x() {
    y = 1; // strict 모드에서는 ReferenceError를 출력
    var z = 2;
}

x();

console.log(y); // 1
console.log(z); // ReferenceError: z is not defined outside x

```

7. 선언된 변수들은 어떠한 코드가 실행되기 전에 만들어진다.

8. 선언되지 않은 변수들은 변수들을 할당하는 코드가 실행되기 전까지는 존재하지 않는다.

```

console.log(a); // ReferenceError
console.log("still going..."); // 결코 실행되지 않는다.

var a;
console.log(a); // 브라우저에 따라 "" or undefined 출력
console.log("still going..."); // 로그에 still going... 출력

```

9. 선언된 변수들은 변수들의 실행 콘텍스트(execution context)의 프로퍼티를 변경하지 않는다.

10. 선언되지 않은 변수들은 변경 가능하다. (삭제 될 수 있다.)

```

var a = 1;
b = 2;

delete this.a // strict 모드에서는 TypeError를 출력한다. 그렇지 않으면 자동적으로 실패?
delete this.b;

console.log(a, b); //Reference Error를 출력
// 'b' 프로퍼티는 삭제되었고, 어디에도 존재하지 않는다.

```

11. 이러한 세 가지 다른 점 때문에, 변수 선언 오류는 예기치 않은 결과로 이어질 가능성이 높다.

12. 그러므로 함수 또는 전역 범위인지 여부와 상관없이, 항상 변수를 선언하라

# var 호이스팅(hoisting)

1. 변수 선언들(그리고 일반적인 선언)은 어느 코드가 실행 되기 전에 처리하기 때문에, 코드 안에서 어디서든 변수 선언은 최상위에 선언한 것과 동등하다.

2. 이것은 변수가 선언되기 전에 사용 될 수 있다는 것을 의미한다.

3. 변수 선언이 함수 또는 전역 코드의 상단에 이동하는 것과 같은 행동을 "호이스팅(hoisting)"이라고 부른다.

```

bla = 2
var bla;

// 위 선언을 다음과 같이 암묵적으로 이해하면 된다.

var bla;
bla = 2;

```

# 예제

# 두 변수들의 선언 및 초기화

```

var a = 0, b = 0;

```

# 단일 문자열 값으로 두 변수들 할당

```

var a = "A"
var b = a;

// 다음과 같음

var a, b = a = "A"

// 순서에 유의하라

var x = y, y= "A"
console.log(x + y); undefinedA

```

1. x와 y는 어떠한 코드가 실행되기 전에 선언되었다. 

2. 할당은 후에 발생하였다.

3. "x = y"가 실행될 때, y는 존재하여 ReferenceError를 출력하지 않고 값은 "undefined"다.

4. 그래서 x는 undeifned 값이 할당 된다.

5. 그리고 나서 y는 "A" 값이 할당된다.

6. 결과적으로, 첫 번째 줄 이후에 x === undefined && y === "A" 와 같은 결과가 된다.

# 다수의 변수들의 초기화

```

var x = 0;

function f() {
    var x = y = 1; // x는 지역변수로 선언, y는 아니다.
}

f();

console.log(x, y); // 0, 1

```

# 암묵적인 전역변수와 외부 함수 범위

1. 암묵적인 전역변수가 될 것으로 보이는 변수는 함수 범위 밖에서 변수들을 참조할 수 있다.

```

var x = 0; // x는 전역으로 선언되었고, 0으로 할당

console.log(typeof z); // undefined

function a() {
    var y = 2; // y는 함수 a에서 지역변수로 선언, 2로 할당된다.

    console.log(x, y) // 0 2

    function b() { // b 함수를 호출하였을 때,
        x = 3; // 존재하는 전역 x값에 3을 할당, 새로운 전역 var 변수를 만들지 않는다.
        y = 4; // 존재하는 외부 y값에 4를 할당, 새로운 전역 var 변수를 만들지 않는다.
        z= 5; // 새로운 전역 z 변수를 생성하고 5를 할당, strict mode에서는 Reference Error
    }

    b(); // 호출되는 b는 전역 변수로 z를 생성

    console.log(x, y, z) // 3 4 5
}

a(); // 호출되는 a 또한 b 를 호출한다.
console.log(x, z); // 3 5
console.log(typeof y) // undefined y는 function a에서 지역 변수이다.

```