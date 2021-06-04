# Admin Page 자바 셋팅하는 법

# 신 비즈 중계센터 ECS 설정하는 법

1. make login

- 

2. make build

- 

```

Restarting Apache httpd web server: apache2AH00558: apache2:

Could not reliably determine the server's fully qualified domain name, using 172.17.0.2.

Set the 'ServerName' directive globally to suppress this message.


Dockerfile에서 해당 부분에 Run 추가했다.

EXPOSE 80
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
EXPOSE 443
```

3. make up

```

ERROR: for web  Cannot start service web: Ports are not available: listen tcp 0.0.0.0:80: bind: address already in use

docker-compose.yml 파일에 ports 

ports:

- "${PORT:-81}:81"
- "443:443"

기존에는 80:80으로 되어있었다.

```

4. make install-for-prod

# 



# AWS SSL uzzleHttp\Exception\RequestException: cURL error 60: SSL certificate problem

```

호출하는 클라이언트 쪽에 verify 설정 해당 오류는 네이버와 통신할 때 발생했다. 개발서버에서만 확인되는 문제

        $client = new Client([
            'verify' => false
        ]);
```
# brew로 php 버전 바꾸기

```

~/.zshrc 로 해당 php export 7.1 <-> 7.4 

export PATH="/usr/local/opt/php@7.4/bin:$PATH"
export PATH="/usr/local/opt/php@7.4/sbin:$PATH"

#처리 제거

source ~/.zshrc

brew services restart php@7.4 <-> php@7.1

```

# valet links 확인하고 index.php 열리는데 라라벨 안 될 경우?

1. env파일 확인

# index 잡는법

```

대용량 데이터는 인덱스가 잡혀있고 안 잡혀있고 시간차이가 많이 난다.

검색해야 할 필드가 세 개라고하면 (name, email, phone)

해당 인덱스는 name, email, phone, name_email, name_phone, email_phone, name_email_phone으로 잡아주는 게 가장 빠르다?

이 속도 차이는 직접 테스트해보면 된다. 

24382597 2천만짜리 데이터의 속도차이 

```

# CS 들어와서 수정해야 할 때

```

해당 CS번호..로 마스터에서 new brach (feature/SVCREQ-1234) 만들고

해당 내용 수정한 다음 dev로 머지하고 개발팀에 멘션 날리기

핫 픽스일 경우는 hotfix/SVCREQ-1234

```

# 갑자기 컴포저 꼬여서 안될 때

1. 해당 서버의 php버전으로 버전 변경한다음

2. restart하고..

2. composer.lock파일 지우고

3. 새로 컴포저 업데이트 + composer autoload

4. 하면 정상적으로 작동한다.

# 테이블 설정.. TB_CENTER_USER?

# jira

1. 이슈 만들기

2. 에픽 만들기

# Table

1. User-> id, password, name, phone + 중개법인 사업자등록번호? 중개등록번호?

1. User->belongsMany Center

2. Center -> role -> Master or Normal

# Git

1. main에서 branch 해당 에픽 프로젝트명으로 설정

# JWT 

1. https://onlinewebtutorblog.com/rest-api-development-in-laravel-8-with-jwt-authentication/

2. composer require tymon/jwt-auth

# User and Role

- 사용이유? 

```

관리센터 어드민 -> 담당자(마스터) -> 소속유저들 // 마스터도 어드민이 승인?


```

1. https://www.itsolutionstuff.com/post/laravel-8-user-roles-and-permissions-tutorialexample.html

2. 매물을 담당하는 product는 기본 테이블 사용..

3. 

# 궁금한 것?

1. 마스터는 누가 승인해주는지..? - 강제로 지정

2. 기존 테이블과 연동되는 테이블들..? - agency

3. 중개법인은 하나로 통일되는 것인지..? - 마스터는 하나 팀은 여러개일수도 당장은 하나

4. tb_agency랑 연동할 수 있는 키가 필요하다.

```

TB_CENTER_USER

id, name, email, password, aidx, phone, role_id

Role

id, type

type == 1 Wait
type == 2 Admin
type == 3 User

```

# ServiceProvider - Macro

```

ResponeMacroServiceProvider를 생성하고 해당 provider를 app/config/app.php provider에 등록한다.

 App\Providers\ResponseMacroServiceProvider::class,
 /**
     * Bootstrap the application services.
     *
     * @return void
     */
    public function boot()
    {
        //
        Response::macro('success');

    }
}

```

