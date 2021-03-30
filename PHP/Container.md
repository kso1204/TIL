# Container

서비스 컨테이너, 바인딩, 프로바이더, 레지스터, 파사드에 대한 개념이 안 잡힐 때 도와주는 영상

https://laracasts.com/series/laravel-6-from-scratch/episodes/38?autoplay=true

https://laracasts.com/series/laravel-6-from-scratch/episodes/39?autoplay=true

https://laracasts.com/series/laravel-6-from-scratch/episodes/40?autoplay=true

https://laravel.kr/docs/8.x/container

라라벨의 서비스 컨테이너는 클래스의 의존성을 관리하고 의존성을 주입하는 강력한 도구 입니다.

의존성 주입이라는 멋진 말의 의미는 다음과 같습니다.

클래스간의 의존성은 클래스 생성될 때 또는 경우에 따라 "setter" 메소드에 의해서 "주입" 된다는 의미입니다.

의존성 주입 DI 

간단한 예제를 들어 봅시다.

```
<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Repositories\UserRepository;
use App\Models\User;

class UserController extends Controller
{
    /**
     * The user repository implementation.
     *
     * @var UserRepository
     */
    protected $users;

    /**
     * Create a new controller instance.
     *
     * @param  UserRepository  $users
     * @return void
     */
    public function __construct(UserRepository $users)
    {
        $this->users = $users;
    }

    /**
     * Show the profile for the given user.
     *
     * @param  int  $id
     * @return Response
     */
    public function show($id)
    {
        $user = $this->users->find($id);

        return view('user.profile', ['user' => $user]);
    }
}
```

이 예제에서 UserController는 데이터 소스로부터 사용자를 조회할 필요가 있습니다.

따라서 우리는 사용자를 조회할 수 있는 서비스를 주입 할 것입니다.

여기에서는, UserRepository 가 Eloquent를 사용하여 데이터베이스로부터 사용자 정보를 조회합니다.

repository 가 주입되었기 때문에, 원하는 경우 손쉽게 다른 구현 객체로 변경할 수 있습니다.

또한 애플리케이션을 테스트할 때 손쉽게 "목킹" 하거나, 더미 UserRepository 구현체를 생성할 수도 있습니다.

라라벨 서비스 컨테이너를 깊이 이해하는 것은 강력하고 큰 애플리케이션을 구축할 때나 라라벨 코어에 공헌하기 위해서 아주 중요한 부분입니다.

간단한 바인딩

서비스 프로바이더 안에서는 항상 $this->app 속성을 통해서 컨테이너 인스턴스에 접근 할 수 있습니다.

또한 bind 메소드를 사용하여 클래스나 인터페이스 이름에 대한 의존성을 우리가 원하는 클래스의 인스턴스를 반환하는 Closure를 등록하여 바인딩 할 수 있습니다.

```
$this->app->bind('HelpSpot\API', function ($app) {
    return new \HelpSpot\API($app->make('HttpClient'));
});
```

싱글톤으로 바인딩하기 -> 동일한 객체 인스턴스!!

singleton 메소드로 클래스나 인터페이스를 바인딩 하면 컨테이너는 한 번만 해당 의존성을 해결합니다.

싱글톤 바인딩으로 의존성이 해결되면, 컨테이너의 다른 부분에서 호출될 때 동일한 객체 인스턴스가 반환될 것입니다.

```
$this->app->singleton('HelpSpot\API', function ($app) {
    return new \HelpSpot\API($app->make('HttpClient'));
});
```

# 라라벨의 서비스 컨테이너

서비스 컨테이너 혹은 의존성 주입 컨테이너는 모든 기능 중에서 가장 핵심이다.

컨테이너는 인터페이스와 클래스와 인스턴스를 연결하고 의존성을 해결하는 데 사용할 수 있으며, 서로 연결된 의존성 네트워크를 관리하는 강력한 도구다.

컨테이너를 지칭하는 이름

- 애플리케이션 컨테이너
- 제어의 역전(IoC) 컨테이너
- 서비스 컨테이너
- 의존성 주입(DI) 컨테이너

# 의존성 주입

의존성 주입이란 어떤 로직을 처리하기 위해서 생성해야 되는 의존 객체를 new 키워드로 직접 생성하는 대신에 외부에서 주입하는 것을 의미한다.

이때 주입 방식에 따라 생성자주입이 가장 흔히 쓰이는데, 이는 의존 객체가 객체 생성 시 주입되는 것을 뜻한다.

이외에도 클래스가 의존성을 주입받기 위한 메서드를 사용하는 세터 주입과 메서드가 호출될 때 의존성이 주입되는 메서드 주입이 있다.

# app() 글로벌 헬퍼

app() 헬퍼에 정규화된 클래스명이나 라라벨 단축 키워드 문자열을 넣으면 해당 클래스의 인스턴스를 반환한다.

$logger = app(Logger::class);

이는 컨테이너를 사용하는 가장 간단한 방법이다. 이 방법은 쉽고 간편하게 클래스의 인스턴스를 생성해서 반환해준다.

곧 확인하겠지만 new Logger와 비슷하지만 훨씬 더 나은 방법이다.

# 인스턴스를 생성하는 여러 방법들

어떤 클래스나 인터페이스의 인스턴스를 만드는 가장 간단한 방법은 app('정규화된 클래스명')을 이용해서 글로벌 헬퍼에 직접 클래스나 인터페이스 이름을 넘겨주는 것이다.

하지만 현재의 로직에서 이미 컨테이너 인스턴스를 가지고 있따면 컨테이너 인스턴스에 필요한 인스턴스를 만드는 방법이 몇 가지 있다.

가장 일반적인 방법은 컨테이너 인스턴스의 make()메서드를 사용하는 방법이다.

$app->make('정규화된 클래스명')과 같이 사용한다.

# 컨테이너는 어떻게 의존 객체를 연결하는가?

라라벨 오토와이어링

class Bar
{
    public function __construct() {}
}

class Baz
{
    public function __construct() {}
}

class Foo
{
    public function __construct(Bar $bar, Baz $baz) {}
}

$foo = app(Foo::class);

컨테이너는 Foo 생성자에 있는 타입힌트를 읽고 Bar와 Baz 인스턴스를 확인한 다음 Foo 인스턴스가 생성될 때 이들을 주입한다.

이를 오토와이어링(자동으로 연결된다는 의미)이라고 한다. 오토와이어링은 개발자가 명시적으로 클래스를 컨테이너에 연결할 필요 없이 타입힌트에 기반해서 인스턴스를 식별하는 기능이다.

오토와이어링은 클래스가 컨테이너에 명시적으로 이 클래스와 저 클래스가 서로 연결되어 있다고 알리지 않아도(Foo, Baz, Bar처럼), 컨테이너가 이를 알고 알아서 해결한다는(인스턴스화할 수 있다는) 것을 의미한다.

이는 생성자 메서드에 의존성이 없는 (Bar와 Baz 같은) 클래스와 생성자 메서드에 의존성을 가지며 컨테이너가 식별할 수 있는(Foo 같은) 클래스가 컨테이너에 의해 인스턴스화될 수 있다는 것을 의미한다.

따라서 의존성을 해결할 수 없는 생성자 메서드 파라미터를 가진 클래스만 의존성 해결 방법을 따로 알려주면 된다.

로그 파일의 위치와 로그 레벨과 관련된 파라미터를 가진 $logger 클래스가 그 예다. 이런 것들을 위해 컨테이너에 대상 클래스 또는 인터페이스를 어떻게 인스턴스화하는지 명시적으로 등록(바인딩)하는 방법을 익혀야 한다.

# 컨테이너에 클래스 바인딩하기

라라벨 컨테이너에 클래스를 바인딩한다는 것은 본질적으로 컨테이너에게 '만약 개발자가 Logger 인터페이스의 반환을 요구하면, 이 파라미터를 가지고 의존성을 해결(즉 인스턴스화한 다음 반환)하라'고 이야기하는 것이다.

# 클로저를 바인딩하기

컨테이너에 바인딩하기 적절한 위치는 서비스 프로바이더의 register() 메서드다.

//LoggerServiceProvider

public funtion register()
{
    $this->app->bind(Logger::class, function($app) {
        return new Logger('/log/path/here', 'error');
    });
}

첫째, $this->app->bind()를 살펴보자.

$this->app은 모든 서비스 프로바이더에서 사용할 수 있는 컨테이너의 인스턴스다.

컨테이너의 bind() 메서드는 컨테이너에 바인드할 때 사용하는 메서드다.

bind()의 첫 번째 파라미터는 식별용 '키'다. 여기에 대개 정규화된 클래스명(::class로 표시하는)을 사용한다.

두 번째 파라미터는 무엇을 바인드하는지에 따라 달라진다. 하지만 본질적으로는 키에 연결된 인스턴스를 만들어서 돌려주려면 어떤 과정을 거쳐야 하는지 컨테이너에게 알려주는 무엇인가가 되어야 한다.

이 예제에서는 클로저를 전달한다. 그래서 이제 누군가가 app(Logger::class)를 실행하면 클로저의 실행 결과를 반환받는다.

클로저는 컨테이너 자체의 인스턴스($app)가 인자로 전달되므로 컨테이너에서 가져올 의존 객체가 있다면 클로저 내부에서 사용할 수 있다.

$this->app->bind(UserMailer::class, function ($app) {
    return new UserMailler(
        $app->make(Mailer::class),
        $app->make(Logger::class),
        $app->make(Slack::class)
    );
});

이 클로저는 클래스의 새로운 인스턴스를 요청할 때마다 실행되고, 새로운 인스턴스 결과물이 반환될 것이라는 점에 유의하자.

# 싱글턴, 별칭, 인스턴스에 바인딩하기

bind() 메서드와 다르게 바인딩한 클로저의 결과를 캐싱해서 인스턴스를 요청할 때마다 새로운 인스턴스를 생성하지 않고 캐싱한 인스턴스를 반환하게 할 수 있다.

이를 싱글턴패턴이라고 하며 singleton() 메서드를 사용해서 바인딩한다.

public function register()
{
    $this->app->singleton(Logger::class, function () {
        return new Logger('\log\path\here', 'error');
    });
}


