# Session

세션 스토리지는 웹 애플리케이션에서 페이지 요청 간의 상태를 저장하는 데 사용하는 주요 도구다.

라라벨 세션 매니저는 세션 드라이버로 파일, 쿠키, 데이터베이스, 멤캐시, 레디스, DynamoDB, 인메모리 배열(페이지 요청이 끝나면 사라지므로 테스트용으로 쓰기 좋다)을 지원한다.

세션 설정과 드라이버에 관련된 모든 설정은 config/session.php에서 한다. 

세션 데이터를 암호화할지 말지 선택하고, 어떤 드라이버를 사용할지(파일이 기본이다) 고르고, 세션 스토리지의 길이나 사용할 파일 혹은 데이터베이스같이 커넥션에 특화된 자세한 사항을 명시할 수 있다.

세션의 메뉴얼(https://laravel.kr/docs/session)을 읽어보고 사용하려는 드라이버에 따라 다르게 준비해야 하는 의존성과 설정을 알아보자.

# 세션에 접근하는 방법

Session 파사드 이용

Session::get('user_id');

글로벌 seesion() 헬퍼 사용하기

//조회(get)

$value = session()->get('key');

$value = session('key');

//저장(put)

session()->put('key', 'value');

session(['key', 'value']);

# 세션 인스턴스에서 사용할 수 있는 메서드

가장 많이 쓰이는 건 get()과 put()이지만 세션 인스턴스에서 사용할 수 있는 모든 메서드를 하나씩 파라미터와 함께 살펴보자.

session()->get($key, $fallbackValue)

get()은 세션에서 키에 해당하는 값을 가져온다.

키에 설정된 값이 없으면 두 번째 파라미터에 적은 대체 값을 돌려준다.

대체값을 제공하지 않으면 null을 반환한다.

대체 값은 문자열도 될 수 있고 클로저도 될 수 있다.
```
$points = session()->get('points');

$points = session()->get('points', 0);

$points = session()->get('points', function () {

    return (new PointGetterService)->getPoints();

});
```
session()->put($key, $value)

put()은 $value를 세션의 $key에 저장한다.
```
session()->put('points', 45);

$points = session->get('points');

session()->push($key, $value)
```
세션값이 배열이면 push()를 써서 배열에 값을 추가할 수 있다.
```
session()->put('friends', ['sal', 'quan', 'mec']);
session()->push('friends', 'jav');
```

session->has($key)

has()는 키에 해당하는 값이 있는지 확인한다.

```
if(session()->has('points')) {
    //무엇인가?
}
```

키 배열을 넘겨줄 수도 있는데, 이때는 모든 키에 값이 존재해야만 참을 반환한다.

session()->exists($key)

exists()는 has()처럼 키에 값이 설정되어 있는지 확인한다. 단 has()와는 달리 null이 값으로 설정되어 있어도 참을 반환한다.

session()->all()

all()은 세션에 있는 모든 것을 배열로 반환한다. 여기에는 프레임워크가 설정한 값도 포함된다.

session()->only()

only()는 세션에서 지정한 값들만 배열로 반환한다 (라라벨 5.8이상)

session()->forget($key)와 session()->flush()

forget()은 이전에 설정한 세션 값을 지운다.

flush()는 모든 세션 값을 지우는데 프레임워크가 설정한 값도 지운다.

session()->pull($key, $fallbackValue)

pull()은 값을 가져온 다음 세션에서 지운다는 점을 제외하고는 get()과 같다.

# 플래시 세션 스토리지

session()->flash($key, $value)

flash()는 다음 페이지 요청에만 사용할 세션 키에 값을 설정한다.

session()->reflash()와 session()->keep($key)

이전 페이지의 플래시 세션 데이터를 다음 요청에서 또 써야 할 필요가 있으면, reflash()를 사용해서 전체를 복원하거나 keep($key)를 써서 특정 키에 해당하는 값만 복원할 수 있다.

