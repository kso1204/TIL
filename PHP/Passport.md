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