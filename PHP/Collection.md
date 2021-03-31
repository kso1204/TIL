# Collection

컬렉션은 라라벨에서 만든 개념은 아니다.

PHP의 array*() 함수를 사용하면 너저분한 코드를 좀 덜 너저분하게 바꿀 수 있따.

```
$users = [...];

$admins = [];

foreach ($users as $user) {
    if ($user['status'] == 'admin') {
        $user['name'] = $user['first']. ' ' . $user['last'];
        $admins[] = $user;
    }
}

return $admins;
```

```
$users = [...];

return array_map(function ($user) {
    $user['name'] = $user['first']. ' ' .$user['last'];
    return $user;
}), array_filter($users, function ($user) {
    return $user['status'] == 'admin';
});
```

임시 변수 ($admin)를 제거하고 하나의 복잡한 foreach 반복문을 맵과 필터라는 두 작동으로 바꾸었다.

PHP배열 함수는 일관된 시그니처를 가지고 있지 않다.

라라벨의 컬렉션은 PHP의 배열 조작 함수의 기능은 살리되, 더 깔끔하고 쓰기 편한 문법을 제공한다.

배열을 라라벨의 컬렉션으로 바꿔주는 collect 헬퍼 함수를 쓰면 다음과 같이 할 수 있다.

```
$users = collect([...]);

return $users->filter(function ($user) {
    return $user['status'] == 'admin';
})->map(function ($user) {
    $user['name'] = $user['first']. ' ' .$user['last'];
    return $user;
});
```

다른 무엇보다도 컬렉션이 제공하는 가장 큰 혜택은 배열을 조작하기 위해 해야 하는 동작을 단순하고 개별적이고 이해하기 쉬운 작업으로 나눈다는 것이다.

```
$users = [...];

$coutAdmins = collect($users)->filter(function ($user) {
    return $user['status'] == 'admin';
})->count();
```

# 주요 메서드

https://laravel.kr/docs/collections 매뉴얼

all()과 toArray()

컬렉션을 배열로 변환하고 싶으면 all()이나 toArray()를 이용한다.

toArray()는 컬렉션뿐 아니라 그 하위의 모든 엘로퀀트 객체도 배열로 바꾼다.

all()은 컬렉션만 배열로 바꾸고 컬렉션에 담긴 엘로퀀트 객체는 그대로 유지된다.

filter()와 reject()

클로저로 각 아이템을 확인해서 원본 컬렉션의 일부만 얻고 싶을 때에는 filter() (클로저가 true를 반환하는 아이템을 유지), reject() (클로저가 false를 반환하는 아이템을 유지)

where()

특정 키가 특정 값인 하위 집합을 얻을 수 있따.

$admins = $users->where('role', 'admin');

first()와 last()

컬렉션에서 아이템 하나만 가져올 때, 앞에서는 first() 뒤에서는 last()

each()

컬렉션이 각 아이템 자체를 변경하지 않으면서 각 아이템으로 뭔가 하고 싶으면 each()를 사용한다.

```
$users->each(function ($user) {
    EmailUsersAThing::dispatch($user);
});
```

map()

컬렉션의 모든 아이템을 순회하면서 변경한 후 변경된 새로운 컬렉션을 반환하려면 map()을 사용한다.

```
$users = $users->map(function ($user) {
    return [
        'name' => $user['first']. ' ' .$user['last'];
        'email' => $user['email'],
    ];
});
```

reduce()

컬렉션의 모든 아이템에 특정 작업을 수행하여 하나의 결과 값으로 만들려면 reduce()를 사용한다.

이 메서드는 초깃값(캐리)을 취하고 컬렉션의 각 아이템이 이를 변경하는 식으로 작동한다.

```
$points = $users->reduce(function ($carry, $user) {
    return $carry + $user['points'];
}, 0); //캐리를 0부터 시작함
```

pluck()

컬렉션에 있는 각 아이템의 특정 키에 해당하는 값만 뽑아내고 싶으면 pluck()를 사용한다.

chunk()와 take()

chunk()를 사용하면 미리 정한 크기의 그룹으로 컬렉션을 분리할 수 있다.

take()는 지정한 숫자만큼의 아이템을 가져온다.

groupBy()

컬렉션에 있는 모든 아이템을 하나의 속성값으로 그룹지으려면 groupBy()를 사용한다.

reverse()와 shuffle()

reverse()는 컬렉션에 있는 아이템 순서를 반대로 바꾸고 shuffle()은 순서를 섞는다.

```
$numbers = collect([1,2,3]);

$numbers->reverse()->toArray(); [3, 2, 1];
$numbers->shuffle()->toArray(); [2, 3, 1];

sort(), sortBy(), sortByDesc()

아이템이 단순 문자열이나 정수열이면 sort()로 정렬할 수 있다.

countBy()

countBy는 컬렉션 내에 같은 값이 몇 개 있는지 세어준다.

```
$collection = collect([10, 10, 20, 20, 20, 30]);

$collection->countBy()->all(); //[10 => 2, 20 => 3, 30 => 1]
```

countBy 메서드는 컬렉션에서 아이템을 세는 데 사용할 값을 커스터마이징하는 콜백을 파라미터로 받을 수도 있다.

```
$collection = collect(['laravel.com', 'laravel.co']);

$collection->countBy(function ($address){
    return Str::after($address, '.');
})->all();

// ['com' => 1, 'co' => 1]
```
컬렉션에 아이템이 몇 개 있는지 count(), isEmpty(), isNotEmpty()로 확인할 수 있다.

join()

join()은 컬렉션 값을 하나의 문자열로 합쳐준다. 필요시 마지막 연결 문자열을 별도로 정의할 수도 있다.

```
$collection = collect(['a', 'b', 'c', 'd', 'e']);

$collection->join(' ,', ', and');

// 'a, b, c, d, and e'
```

composer require tightenco/collect 명령어를 실행하기만 하면 Illuminate\Support\Collction 클래스와 collect() 헬퍼를 사용할 수 있다.

