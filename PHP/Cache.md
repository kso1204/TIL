# Cache

캐시는 세션과 구조가 매우 비슷하다.

키를 전달하면 라라벨이 이를 전달한다.

가장 큰 차이는 캐시 데이터는 애플리케이션별로,

세션 데이터는 사용자별로 캐시된다는 것이다.

이는 데이터베이스 쿼리, API 호출, 슬로우 쿼리 결과 등을 저장하는 데 캐시가 더 일반적으로 사용됨을 의미한다.

캐시 설정은 config/cache.php에서 할 수 있다.

세셔과 마찬가지로 드라이버별로 자세한 사항을 설정할 수 있고, 어떤 드라이버를 기본으로 사용할지 정할 수 있다.

라라벨은 file 캐시 드라이버를 기본으로 사용하지만, 멤캐시나 레디스, APC, DynamoDB, 데이터베이스 혹은 직접 만든 캐시 드라이버를 사용할 수 있다.

캐시 매뉴얼(https://laravel.kr/docs/cache)을 읽어보고 사용하려는 드라이버별로 준비해야 하는 의존성과 설정을 알아두자.

# 캐시에 접근하기

파사드 사용하기

$users = Cache::get('users');

글로벌 cache() 헬퍼 사용하기

//캐시에서 가져오기
```
$users = cache('key', 'default value');
$users = cache()->get('key', 'default value');
```
//$seconds 동안 저장하기
```
$users = cache(['key' => 'value'], $seconds);
$users = cache()->put('key', 'value', $seconds);
```

# 캐시 인스턴스에서 사용할 수 있는 메서드

cache()->get($key, $fallbackValue)와 cache()->pull($key, $fallbackValue)

get()은 키에 해당하는 값을 가져온다. pull()은 값을 가져온 다음 제거한다는 점을 제외하고는 get()과 같다.

cache()->put($key, $value, $secondsOrExpiration)

put()은 주어진 시간(초) 동안 키에 값을 저장한다.

시간을 입력하는 것보다 만료 시점을 설정하는 것을 선호한다면 세 번째 파라미터로 Carbon 객체를 넘겨주자

cache()->put('key', 'value', now()->addDay());

cache()->add($key, $value);

add()는 put()과 비슷한데 값이 이미 존재하면 재설정하지 않는다.

그리고 add()는 값이 실제로 추가됐는지 여부를 불리언 값으로 반환한다는 점도 다르다.

```
$someDate = now();

cache()->add('someDate', $someDate); -> true

$someOtherDate = now()->addHour();

cache()->add('someDate', $someOtherDate); -> false
```

cache()->forever($key, $value)

forever()는 키에 값을 저장한다. 값이 만료되지 않는다는 것(forget()으로 지우기 전까지)을 제외하고는 put()과 같다.

cache()->has($key)

has()는 키에 값의 존재 여부를 불리언 값으로 반환한다.

