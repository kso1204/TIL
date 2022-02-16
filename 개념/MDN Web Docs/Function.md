# Function

1. Function 생성자는 새 Function 객체를 만든다.

2. 이 생성자를 직접 호출하여 동적으로 함수를 생성할 수도 있으나, 보안 문제 및 eval과 유사한 성능 문제가 발생할 수 있다.

3. 하지만 eval과 달리, Function 생성자는 전역 범위로 한정된 함수만 생성한다.

```

const sum = new Function('a', 'b', 'return a + b');

console.log(sum(2, 6)); //8

```

4. 모든 JavaScript 함수는 사실 Function 객체이다.

5. 이는 (function(){}).constructor === Function 이 참을 반환하는 것에서 알 수 있다.

# 설명

1. Function 생성자로 생성한 Function 객체는 함수를 생성할 때 구문 분석을 수행한다.

2. 반면, 함수 표현식이나 함수 선언문으로 함수를 정의하고 코드 내에서 호출한 경우 나머지 코드와 함께 구문 분석되므로, Function 생성자가 더 비효율적이다.

3. 함수로 전달되는 모든 인수는 생성될 함수의 매개 변수 식별자 이름으로 전달되는 순서대로 처리된다.

4. (new 연산자를 사용하지 않고) 함수로써 Function 생성자를 호출하는 것은 생성자로 호출하는 것과 같다.

5. 하지만 new 연산자가 제거됨으로써 코드의 크기를 약간(4 바이트 더 작게) 줄일 수 있으므로 Function에 대해서는 new 연산자를 사용하지 않는 것이 좋다.

# Function의 속성과 메서드

1. 전역 Function 객체는 자신만의 메서드 또는 속성이 없다.

2. 그러나, 그 자체로 함수이기에 Function.prototype 에서 프로토타입 체인을 통해 일부 메서드 및 속성을 상속 받는다.

# Function 인스턴스

1. Function 인스턴스는 Function.prototype 에서 메서드 및 속성을 상속 받는다.

2. 모든 생성자와 마찬가지로, 생성자의 프로토타입 객체를 바꿈으로써 모든 Function 인스턴스에 변화를 줄 수 있다.

# 예제

# Function 생성자와 함수 선언의 차이

1. Function 생성자로 만들어지는 함수는 생성 컨텍스트에 대한 클로저(closure)를 생성하지 않는다.

2. 이들 함수는 항상 전역 범위에서 생성된다.

3. 함수가 실행될 때, 자신의 지역 변수와 전역 변수에만 접근할 수 있으며 Function 생성자가 호출된 그 범위의 변수에는 접근할 수 없다.

```

var x = 10;

function createFunction1() {
    var x = 20;
    return new Function('return x;'); // 여기서 x는 전역 범위에 있는 x를 참조함
}

function createFunction2() {
    var x = 20;
    function f() {
        return x; // 여기서 x는 위의 지역에 있는 x를 참조함
    }
    return f;
}

var f1 = createFunction1();
console.log(f1()); // 10

var f2 = createFunction2();
console.log(f2()); // 20

```

4. 위 코드는 브라우저에서는 정상 동작하지만, Node.js에서는 X를 찾을 수 없어 f1()이 ReferenceError를 생성한다.

5. 이는 Node.js의 최상위 스크립트 범위가 전역이 아닌 모듈이므로, x도 모듈 범위에 종속되기 때문이다.