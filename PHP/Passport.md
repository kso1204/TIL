# Passport


대부분의 API는 데이터에 접근하기 위해서 인증을 요구한다. 라라벨은 API 인증을 처리하는 패스포트라는 도구를 제공한다. 패스포트는 별도 패키지로 분리되어 있으며 컴포저로 설치할 수 있다. 패스포트를 사용하면 애플리케이션에 클라이언트와 토큰을 관리하기 위한 API와 UI 컴포넌트를 포함한 완전한 기능을 갖춘 OAuth 2.0 서버를 손쉽게 구축할 수 있다.

인증 시스템 중 Passport를 이용한 API통신

1. composer require laravel/passport

2. php artisan migrate

3. php artisan passport:install

4. user 모델에 HasApiTokens 트레이트 추가

5. AuthServiceProvider -> boot()메서드 안에 PassPort::routes(); 추가

6. config/auth.php에서 api 가드의 token 드라이버를 passport 드라이버로 변경

7. JWT 사용할 경우 Laravel\Passport\Http\Middleware\CreateFreshApiTokens 미들웨어를 web 미들웨어그룹!에 추가

여기서 미들웨어그룹에 추가하지 않으면 Authenticated 오류 발생.. 이 오류를 찾는 게 오래 걸렸다 ㅠ

# 패스포트 스코프

스코프는 OAuth에서 '모든 것을 할 수 있다'가 아니라 '어떤 것을 할 수 잇는지' 정의해둔 것이다.

예를 들어 깃허브 API 토큰을 이전에 받아본 적이 있다면 어떤 애플리케이션은 여러분의 이름과 이메일 주소에 접근하길 원하고,

어떤 애플리케이션은 여러분의 모든 저장소에 접근하길 원하며,

어떤 애플리케이션은 여러분의 기스트에 접근하길 원한다는 것을 알 것이다.

이러한 것이 각각 스코프다.

스코프는 소비 애플리케이션이 작업을 수행하는 데 필요한 접근 범위를 사용자와 API 소비 애플리케이션이 정의할 수 있게 한다.

AuthServiceProvider의 boot() 메서드에서 스코프를 정의할 수 있다.

//AuthServiceProvider

use Laravel\Passport\Passport;

public function boot()
{
    Passport::tokenCans([
        'list-clips' => '사운드 클립 목록',
        'add-delete-clips' => '새 사운드 클립을 추가하고 오래된 것은 지운다.',
        'admin-account' => '관리자 계정 상세 정보',
    ]);
}

스코프를 정의해두면 소비 애플리케이션은 접근하고자 하는 스코프를 정의할 수 있다.

Route::get('tweeter/redirect', function () {
    $query = http_build_query([
        'client_id' => config('tweeter.id'),
        'redirect_uri' => url('tweeter/callback'),
        'response_type' => 'code',
        'scope' => 'list-clips add-delete-clips',
    ]);

    return redirect('http://tweeter.test/oauth/authorize?. $query);
});

사용자가 이 애플리케이션에 권한을 요청할 때 요청받은 스코프 목록을 보여준다.

미들웨어나 user 객체에서 스코프를 확인 가능하다.

Route::get('/events', function () {
    if (auth()->user()->tokenCan('add-delete-clips')) {
        //
    }
});

토큰 권한 확인에 사용할 수 있는 미들웨어도 2개 있다. scope와 scopes다.

이 두 미들웨어를 사용하기 위해서는 app/Http/Kernel.php 파일에 있는 $routeMiddleware에 추가해야한다.

'scopes' => \Laravel\Passport\Http\Middleware\CheckScopes::class,
'scope' => \Laravel\Passport\Http\Middelware\CheckForAnyScope::class,

scopes는 라우트에 접근하기 위해 사용자 토큰이 정의된 모든 스코프를 가져야 하는 반면, scope는 정의된 스코프 중 하나 이상만 있으면 된다.

Route::get('clips', function() {
    // 액세스 토큰이 'list-clips'와 'add-delete-clips' 스코프 둘 다 가지고 있다.
})->middleware('scopes::list-clips, add-delete-clips');

Route::get('clips', function() {
    // 액세스 토큰이 'list-clips'와 'add-delete-clips' 스코프 중 하나 이상을 가지고 있다.
})->middleware('scope::list-clips, add-delete-clips');

# 라라벨 생텀을 이용한 API 인증

라라벨 7.0부터 생텀이라는 새로운 패키지를 제공한다.

sanctum 인증 가드는 자체 spa에서 온 요청이면 세션 인증으로 처리하고, 그렇지 않으면 api 토큰 방식으로 인증을 처리한다.

