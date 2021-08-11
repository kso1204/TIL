# Composer 한글 설명

1. https://xpressengine.github.io/Composer-korean-docs/doc/03-cli.md/

# composer install

1. install 명령어는 현재 디렉토리에 있는 composer.json 파일을 읽고, 의존성을 해석하여, vendor에 패키지들을 설치합니다.

2. 만약 현재 디렉토리에 composer.lock 파일이 있으면, 의존성을 해석하는 대신 composer.lock에 있는 것과 일치하는 버전을 사용할 것입니다.

3. 이것은 라이브러리를 사용하는 사람들이 동일한 의존성 버전을 갖도록 보장해줍니다.

4. 만약 composer.lock 파일이 없다면, 컴포저는 의존성을 해석한 후 새롭게 파일을 만들 것입니다.

# composer update

1. 의존성을 설정한 패키지들의 최신버전을 다운받고, composer.lock 파일을 업데이트 하기 위해서는 update 명령어를 사용합니다.

2. 업데이트 명령어는 프로젝트의 모든 의존관계를 설정한 패키지들을 확인하고 composer.lock에 정확한 버전을 기입해줍니다.

3. 만약 전체 패키지가 아닌 일부 패키지만 업데이트하길 원한다면, 다음과 같이 할 수 있습니다.

```
php composer.phar update vendor/package vendor/package2
```

# composer require

1. require 명령어는 현재 디렉토리에 있는 composer.json 파일에 새로운 패키지들을 추가하는 명령어입니다.

composer.json 파일이 존재하지 않는 경우에는 파일을 직접 생성합니다.

필요로 하는 패키지를 추가하거나 변경한 이후에는 자동으로 설치하거나 업데이트가 수행됩니다.

# composer dump-autoload

1. 클래스맵 패키지 안의 새로운 클래스들 때문에 오토로더를 업데이트 할 필요가 있는 경우, install 또는 update를 통하지 않고 dump-autoload를 사용할 수 있습니다.

2. 또한, 성능상의 이유로 classmap에 psr-0/4 패키지를 변환환 최적화 된 오토로더를 덤프할 수 있습니다.

3. 많은 클래스를 가진 커다란 애플리케이션에서 오토로더는 매 요청 시간의 상당 부분을 차지할 수 있습니다.

4. 모든 클래스에 대해 클래스맵을 사용하는 것은 개발 중에 편리함이 적습니다.

5. 하지만 이 옵션을 사용하면 편리함을 위한 PSR-0/4와 성능을 위한 클래스맵을 여전히 사용할 수 있습니다.
