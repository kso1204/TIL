# Helper

https://laravel.kr/docs/helpers 에서 전체 헬퍼 목록을 찾아볼 수 있다.

라라벨 6.0부터 array_ 나 str_ 로 시작하는 모든 글로벌 헬퍼가 Arr과 Str 클래스 메서드로 대체됐다.

# 배열

Arr::first($array, $callback, $default = null)

콜백 클로저에 정의된 테스트를 통과하는 첫 번째 배열 값을 반환한다.

```
$people = [
    [
        'email' => 'a@a.com',
        'name' => 'aaaa',
    ],
    [
        'email' => 'b@b.com',
        'name' => 'bbb',
    ],
];

$value = Arr::first($people, function ($person, $key) {
    return $person['email'] == 'a@a.com';
});
```

Arr::get($array, $key, $default = null)

존재하지 않는 키를 요청해도 에러가 나지 않고, 중첩 배열에 점 표기법을 사용할 수 있는 두 가지 편의가 더해져 배열에서 값을 가져오기 더욱 편리하다.

$array = ['owner' => ['address' => ['line1' => '123 mian st']]];

$line1 = Arr::get($array, 'owner.address.line1', 'No Address');

$line2 = Arr::get($array, 'owner.address.line2');

Arr::has($array, $key)

중첩 배열을 가로지르는 점 표기법을 사용해서 배역이 특정 키에 값을 가지고 있는지 쉽게 확인할 수 있다.

Arr::pluck($array, $value, $key = null)

지정된 키에 해당하는 값의 배열을 반환한다.

```
$array = [
    ['owner' => ['id' => 4, 'name' => 'Tricia']],
    ['owner' => ['id' => 7, 'name' => 'Kim']],
];

$array = Arr::pluck($array, 'owner.name');

$array = ['Tricia', 'Kim'];
```

# 문자열

Str::startsWith($haystack, $needle), Str::endsWith($haystack, $needle), Str::contains($haystack, $needle)

제공된 $haystack 문자열이 $needle로 시작하는지 끝나는지, 포함하는지를 불리언 값으로 반환한다.

Str::limit($value, $limit = 100, $end='...');

문자열을 주어진 길이의 문자로 제한한다. 길면 주어진 길이로 잘라낸후 $end 문자열을 뒤에 붙인다.

Str::is($pattern, $value)

주어진 문자열이 주어진 패턴과 일치하는지 여부를 불리언 값으로 반환한다.

패턴은 정규 표현식 패턴을 사용할 수도 있고 와일드카드를 나타내는 별표(*)를 사용할 수도 있다.

Str::plural($value, $count = n)

문자열을 복수형으로 변경한다.

Str::plural('person')

=> people

Str::plural('person', 1)

=> person

