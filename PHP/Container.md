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




