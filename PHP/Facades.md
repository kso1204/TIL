# Facades

https://laravel.kr/docs/8.x/facades

파사드는 애플리케이션의 서비스 컨테이너에서 사용가능한 클래스들에 대한 "정적" 인터페이스를 제공합니다.

라라벨은 대부분의 라라벨의 기능에 엑세스하는 많은 파사드들을 제공합니다.

라라벨의 파사드 는 서비스 컨테이너에 등록된 클래스들에 대한 일종의 "정적 프록시" 역할을 수행하는데,

이를 통해서 전통적인 정적 메소드 보다 간결한 문법과 테스트의 용이성 그리고 코드의 유연성을 유지하는 이점을 제공합니다.

```
use Illuminate\Support\Facades\Cache;

Route::get('/cache', function () {
    return Cache::get('key');
});
```

파사드 Vs 의존성 주입

주입된 클래스의 구현체를 변경한다..???

의존성 주입의 주요한 장점중 하나는 주입된 클래스의 구현체를 변경할 수 있다는 특성입니다.

이는 테스팅을 수행하는 동안 모킹 객체(mock) 과 스터브(stub) 를 주입할 수 있게 하고, 다양한 메소드가 호출되는 것을 확인할 수 있게 하여 유용합니다.

일반적으로, 정적 클래스 메소드에 대해서는 모킹 객체(mock) 나 스터브(stub) 사용이 불가합니다.

하지만 파사드는 서비스 컨테이너에 의해서 의존성이 해결되는 클래스 객체의 프록시 메소드로 다이나믹 메소드를 사용하기 때문에,

실제 주입된 클래스 인스턴스를 테스트하는 것과 마찬가지로 파사드를 테스트할 수 있습니다.

예를 들어 다음의 주어진 라우트를 보겠습니다.

```
use Illuminate\Support\Facades\Cache;

Route::get('/cache', function () {
    return Cache::get('key');
});
```

파사드 Vs. 헬퍼 함수

파사드 뿐만 아니라, 라라벨은 뷰 파일을 생성하거나, 이벤트를 발생시키거나, Job을 실행시키거나 또는 HTTP 응답을 반환하는등의 공통된 작업을 수행하는 다양한 "헬퍼" 함수를 포함하고 있습니다.

이러한 다수의 헬퍼 함수들은 파사드와 일치하는 동일한 동작들을 수행합니다.

예를 들어 다음의 파사드 호출과 헬퍼 함수 호출은 동일합니다.

```
return View::make('profile');

return view('profile');
```

파사드와 헬퍼 함수에 대한 구분은 가능..

파사드는 어떻게 동작하는가

라라벨 애플리케이션에서, 파사드는 컨테이너의 객체에 엑세스하는 방법을 제공하는 클래스라고 할 수 있습니다.

이 작업을 수행하는 주요 매커니즘이 파사드 클래스안에 있습니다.

라라벨의 파사드들과 여러분이 작성한 파사드들은 기본 Illuminate\Support\Facades\Facade 클래스를 상속받습니다.

Facade 기본 클래스는 __callStatic() 매직 메소드를 사용하여 여러분이 작성한 파사드에 대한 호출을 컨테이너에서 의존성이 해결된 객체로 전달합니다.

다음의 예제에서 라라벨의 캐시 시스템을 호출합니다.

이 코드를 보자면, 아마 Cache 클래스의 get static 메소드를 호출한다고 생각할 수 있습니다.

```
<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Cache;

class UserController extends Controller
{
    /**
     * Show the profile for the given user.
     *
     * @param  int  $id
     * @return Response
     */
    public function showProfile($id)
    {
        $user = Cache::get('user:'.$id);

        return view('profile', ['user' => $user]);
    }
}
```

Facade https://laravel.com/api/8.x/Illuminate/Support/Facades.html

파일의 상단에 Cache 파사드를 사용하고 있는 부분에 주목해 주십시오.

이 파사드는 Illuminate\Contracts\Cache\Factory 인터페이스의 구현체에 접속할 수 있는 프록시로 동작합니다.

파사드를 사용한 어떠한 호출이라도 라라벨의 캐시 서비스의 구현체에 전달됩니다.

실제로 Illuminate\Support\Facades\Cache를 살펴보면 get이라는 static 메소드는 찾을 수가 없습니다.

https://github.com/laravel/framework/blob/8.x/src/Illuminate/Support/Facades/Cache.php#L36

대신에, Cache 파사드는 기본 Facade 클래스를 상속하고 getFacadeAccessor() 메소드를 정의하고 있습니다.

이 메소드의 역할이 서비스 컨테이너의 바인딩 이름을 반환한다는 것입니다.

사용자가 Cache 파사드의 어떤 스태틱 메소드를 참조하려고 할 때 라라벨은 [서비스 컨테이너]로 부터 cache 로 이름지어진 바인딩 객체를 찾아 메소드 호출을 요청할 것입니다(이 경우 get 메소드) -> 무슨말인지..?

파사드 클래스 목록 https://laravel.kr/docs/8.x/facades#%ED%8C%8C%EC%82%AC%EB%93%9C%20%ED%81%B4%EB%9E%98%EC%8A%A4%20%EB%AA%A9%EB%A1%9D
