# const

1. https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const

2. const 선언은 블록 범위의 상수를 선언한다.

3. 상수의 값은 재할당할 수 없으며 다시 선언할 수도 없다.

```

const number = 42;

try {
    number = 99;
} catch (err) {
    console.log(err);
    // expected output: TypeError : invalid assignment to const 'number'
    // Note - error messages will vary depending on broswer
}

console.log(number);

// expected output: 42

```

# 설명

1. 이 선언은 선언된 함수에 전역 또는 지역일 수 있는 상수를 만든다.

2. 상수 초기자(initializer)가 필요하다.

3. 즉 선언되는 같은 문에 그 값을 지정해야 한다.(이는 나중에 변경될 수 없는 점을 감안하면 말이 된다)

4. 상수는 let 문을 사용하여 정의된 변수와 마찬가지로 블록 범위(block-scope)이다.

5. 상수의 값은 재할당을 통해 바뀔수 없고 재선언 될 수 없다.

6. let에 적용한 "일시적 사각 지대"에 관한 모든 고려는, const에도 적용된다.

# 예제

1. 다음 예제는 상수가 어떻게 동작하는지 보여준다.

```

const MY_FAV = 7; // MY_FAV를 상수로 정의하고 그 값을 7로 함

MY_FAV = 20; //Error

console.log("my fav is : " + MY_FAV);

const MY_FAV = 20; // Uncaught SyntaxError: identifier "MY_FAV" has already been declared

var MY_FAV = 20; // Error

let MY_FAV = 20; // Error

if (MY_FAV == 7) { // 블록 범위의 특성을 아는게 중요
    // 블록 범위로 지정된 MY_FAV 라는 변수를 만드므로 괜찮다.
    let MY_FAV = 20;

    console.log("my fav is:" + MY_FAV) // 20

    var MY_FAV = 20; // 이 선언은 전역으로 호이스팅되고 에러가 발생한다.
}

console.log("my fav is:" + MY_FAV) // 7

const FOO; // const 선언시에 초기값을 생략해서 오류 발생

const MY_OBJECT = {'key' : 'value'}; // const는 오브젝트에도 동작한다.

MY_OBJECT = {'OTHER_KEY' : 'value'}; // 오브젝트를 덮어쓰면 오류 발생

MY_OBJECT.key = 'otherValue' // 하지만 오브젝트의 키는 보호되지 않는다, 오브젝트를 변경할 수 없게 하려면 Object.freeze()를 사용해야 한다.

const MY_ARRAY = [];

MY_ARRAY.push('A'); // ["A"] // 배열에 아이템을 삽입하는 것은 가능하다.

MY_ARRAY = ["B"] // 하지만 변수에 새로운 배열을 배정하면 에러 발생

```

