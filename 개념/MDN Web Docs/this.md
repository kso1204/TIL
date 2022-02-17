# this

1. JavaScript에서 함수의 this 키워드는 다른 언어와 조금 다르게 동작한다.

2. 또한 엄격 모드와 비엄격 모드에서도 일부 차이가 있다.

3. 대부분의 경우 this의 값은 함수를 호출한 방법에 의해 결정 된다.

4. 실행중에는 할당으로 설정할 수 없고 함수를 호출할 때마다 다를 수 있다.

5. ES5는 함수를 어떻게 호출했는지 상관하지 않고 this 값을 설정할 수 있는 bind 메서드를 도입했고,

6. ES2015는 스스로의 this 바인딩을 제공하지 않는 화살표 함수를 추가했다. (이는 렉시컬 컨텍스트 안의 this 값을 유지한다.)

```

const test = {
    prop: 42,
    func: function() {
        return this.prop;
    },
};

console.log(test.func()); // 42

```

# 전역 문맥

1. 전역 실행 맥락에서 this는 엄격 모드 여부에 관계 없이 전역 객체를 참조한다.

```

// 웹 브라우저에서는 window 객체가 전역 객체

console.log(this === winodw); // true

a = 37;

console.log(window.a); //37

this.b = "MDN"

console.log(window.b); // "MDN"
console.log(b);     // "MDN"

```

# 함수 문맥

1. 함수 내부에서 this의 값은 함수를 호출한 방법에 의해 좌우된다.

```

var obj = {a: 'custom'}; // call 또는 apply의 첫 번째 인자로 객체가 전달될 수 있으며 this가 그 객체에 묶임

var a = 'global'; // 변수를 선언하고 변수에 프로퍼티로 전역 window를 할당

function whatsThis() {
    return this.a; // 함수 호출 방식에 따라 값이 달라짐
}

whatsThis() // this는 'global', 함수 내에서 설정되지 않았으므로 global, window 객체로 초기 값을 설정한다.
whatsThis.call(obj); // this는 'custom'. 함수 내에서 obj로 설정한다.
whatsThis.apply(obj); // this는 'custom'. 함수 내에서 obj로 설정한다.

```

```

function add(c, d) {
    return this.a + this.b + c + d;
}

var o = {a: 1, b: 3};

add.call(o, 5, 7); // 16, 첫 번째 인자는 'this'로 사용할 객체이고, 이어지는 인자들은 함수 호출에서 인수로 전달된다.

add.apply(o, [10, 20]); // 34, 첫 번째 인자는 'this'로 사용할 객체이고, 이어지는 인자들은 함수 호출에서 인수로 사용될 멤버들이 위치한 배열이다.

```

# bind 메서드

1. ECMAScript 5는 Function.prototype.bind를 도입했다.

2. f.bind(someObject)를 호출하면 f와 같은 본문(코드)과 범위를 가졌지만 this는 원본 함수를 가진 새로운 함수를 생성한다.

3. 새 함수의 this는 호출 방식과 상관없이 영구적으로 bind()의 첫 번째 매개변수로 고정된다.

```

function f() {
    return this.a;
}

var g = f.bind({a: 'azerty'});
console.log(g()); // azerty

vr h = g.bind({a: 'yoo'}); // bind는 한 번만 동작함
console.log(h()); // azerty

var o = {a: 37, f: f, g: g, h: h};
console.log(o.a, o.f(), o.g(), o.h()); // 37, 37, azerty, azerty

```

# 화살표 함수

1. 화살표 함수에서 this는 자신을 감싼 정적 범위이다. 전역 코드에서는 전역 객체를 가리킨다.

```

var globalObject = this
var foo = (() => this);
console.log(foo() === globalObject) // true

var obj = {func: foo}; // 객체로서 메서드 호출
console.log(obj.func() === globalObject); // true

console.log(foo.call(obj) === globalObject); // true, call을 사용한 this 설정 시도

foo = foo.bind(obj); // bind를 사용한 this 설정 시도
console.log(foo() === globalObject); // true

어떤 방법을 사용하든 foo의 this는 생성 시점의 것으로 설정된다. (위 예시에서는 global 객체).

다른 함수 내에서 생성된 화살표 함수에도 동일하게 적용된다.

this는 싸여진 렉시컬 컨텍스트의 것으로 유지된다.

```