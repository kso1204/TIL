# Server and Deploy

출처 : https://modernpug.github.io/php-the-right-way/

PHP는 내장된 FastCGI Process Manager (FPM) 덕분에 nginx에서 아주 잘 동작합니다.
nginx(‘엔진 엑스’라고 읽습니다)는 가볍고 아주 빠른 웹서버입니다.
Apache에 비해 더 적은 메모리를 사용하고, 더 많은 수의 요청을 동시에 처리할 수 있습니다.
메모리를 충분히 확보할 수 없는 가상 서버에서라면 이러한 특징이 더 중요합니다.

Apache와 PHP
PHP와 Apache는 함께한 역사가 아주 깁니다.
하지만 nginx에 비교하면 기본적으로 Apache가 더 많은 리소스를 사용하고, 처리할 수 있는 동시접속 수도 적습니다.

회사에서 사용하고 있는것은 Apache를 사용하고 있는데, 로컬에서 도커를 사용하여 서버를 구성할 때나..

AWS, GCP에 올릴 때는 nginx를 사용하고 있다.

nginx의 default.conf 설정 server_name과 root폴더의 변경만으로 간단하게 이용할 수 있다.

```
server {
    listen 80;
    index index.php index.html;
    server_name localhost;
    error_log /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    root /var/www/html/public;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        try_files $uri = 404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass php:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}
```

어플리케이션 빌드와 배포
여러분이 어플리케이션을 업데이트할 때, 업데이트도 수작업으로 하는데 데이터베이스 스키마 변경도 수작업으로 하고 테스트도 수작업으로 하고 있다면 다시 한 번 생각해 보시기 바랍니다. 어플리케이션 업데이트 때마다 사람이 직접해야 하는 작업이 있고, 그 작업의 수만큼 치명적인 실수가 발생할 가능성도 올라갑니다. 간단한 업데이트를 하는 상황이든지, 복잡한 빌드 과정을 수행하고 있든지, 지속적인 통합 전략을 사용하려고 하든지 간에 빌드 자동화가 여러분에게 꼭 필요할 것입니다.

아마도 다음과 같은 작업을 자동화하고 싶다는 생각이 들 것입니다.

의존성 관리
컴파일, 리소스의 최소화나 압축
테스트 수행
문서 제작
패키지 만들기
배포

배포도구

Phing은 패키징, 배포, 테스팅 과정을 XML 빌드 파일 하나로 설정할 수 있습니다.
https://www.slideshare.net/michieltcs/building-and-deploying-php-applications-with-phing

 - xml형태로 뭐를 써서 어떻게 하는 것 같은데.. 입문하기 좀 복잡해보인다.

Ansistrano는 PHP, Python 및 Ruby와 같은 스크립팅 응용 프로그램의 배포 프로세스(배포 및 롤백)를 쉽게 관리할 수 있는 Ansible과 같은 역할을 합니다.

https://github.com/ansistrano/deploy

 - Ansible에 대해서도 찾아봐야 할 것 같지만.. 이 내용자체가 쉽게 이해되는 내용은 아닌 것 같다.

Deployer는 PHP로 작성된 배포도구이며, 단순하고 함수형으로 작성되었습니다. 병렬적으로 태스크들을 실행하고, 원자적으로 배포하며, 서버간의 일관성을 유지하는 기능들을 포함하고 있습니다. Symfony, Laravel, Zend Framework, Yii를 위한 일반적인 레시피가 있습니다.

https://deployer.org/recipes/npm.html

여러 레시피들이 있는데.. npm 설치를 해준다는 건가..?

https://deployer.org/docs/how-to-deploy-laravel.html

흠.. 지금까지 보기에는 이게 젤 나아보인다.

서버 프로비저닝

많은 수의 서버를 맡게 되었을때 서버를 관리하고 구성하는 일은 곤란한 일이 될 수 있습니다. 알맞은 서버를 적절히 구성할 수 있도록 인프라를 자동화하여 이것을 해결할 도구들이 있습니다. 이 도구들은 보통 매우 쉽게 어플리케이션을 스캐일링하는 것과 같은 인스턴스 관리를 위해 대형 클라우드 호스팅 제공업체(아마존 웹 서비스, 헤로쿠, 디지털오션 등)와 연동됩니다.

Ansible은 YAML 파일로 인프라를 관리하는 도구입니다.
https://www.ansible.com/use-cases/provisioning

PHP 프로젝트에서 지속적인 통합 기법을 사용하는 방법에는 여러가지 방법이 있습니다. Travis CI가 작은 규모의 프로젝트에도 현실성있게 적용할 수 있도록 멋진 결과물을 내놓고 있습니다. Travis CI는 오픈소스 커뮤니티를 위한, 인터넷에서 호스팅되는 지속적인 통합 서비스입니다. GitHub와 통합되어 있기도 하고, PHP를 포함한 많은 프로그래밍 언어를 아주 잘 지원하고 있습니다.

https://www.jenkins.io/

가상화 

laravel에서 지원하는 homestead환경의 vagrant를 사용해봤을 때 처음 부팅되는 2분정도의 시간 소요가 되는데

가상화 입문용으로는 아주 좋았다. 한창할 때 test 도메인이 10개가 넘어가서 hosts파일에서 못 읽는 상황도 발생했다.

laravel homestead가 잘 되어 있어서 좋았다.

homestead의 경우 2분 정도 부팅이 소요 되는데 docker의 경우 한 5초정도 시간이 걸리는 것 같다..

집이랑 노트북 회사 컴퓨터로 작업을 하다보니 homestead로 환경을 맞추고 작업하는 게 좀 어려운 것 같아서..

노트북 같은 경우에는 왠지 모르겠지만 homestead vagrant 초기 실행하는데 1시간 정도 걸렸던 기억도 있다.

도커를 사용하면 간단하게 환경도 맞추고 컨테이너도 금방 만들고 뭐 여러가지 장점이 있다고 해서 쓰고있는데

도커에 적응하는 게 생각보다 어렵다.. 아직도 적응이 안됨 이미지 불러와서 컨테이너 열고 연동해서 사용하면 되는데

이 부분이 쉽지 않다.. aws에서 도커를 구동하는 것도 이상하게 쉽지 않았다.

여러가지 사용해보고 싶으면 이렇게 사용해봐도 되지만 입문할 때 어려울 수도 있다!


Vagrant
Vagrant는 간단한 설정 파일 하나만 있으면, VMware 등 잘 알려져 있는 가상 환경에 가상 머신을 만들어 줍니다. 이렇게 만든 깨끗한 가상 머신에서 출발하여 수작업으로 환경을 설정할 수도 있고, Puppet이나 Chef와 같은 “프로비저닝(provisioning)” 도구를 사용하여 가상 머신을 설정할 수도 있습니다.

Docker
Docker 는 완전한 가상 머신을 대체할 수 있는 경량의 도구로 “컨테이너”로 이루어져 있어서 그렇게 불립니다. 가장 간단한 경우에 컨테이너는 웹 서버 하나를 동작시키는 것과 같이 특정한 하나의 역할을 하는 구성 단위입니다. “이미지”는 컨테이너를 만들이 위해서 사용하는 패키지입니다. Docker는 이미지들로 채워진 저장소가 있습니다.

전형적인 LAMP 어플리케이션은 웹 서버, PHP-FPM 프로세스, MySQL, 이렇게 세 개의 컨테이너로 구성될 수 있습니다. Vagrant 의 공유 폴더와 같이 Docker가 어디에서 어플리케이션을 찾을 위치를 알려줄 수 있습니다.

캐시
PHP는 별로 손을 대지 않아도 꽤 빠른 편이긴 하지만, 원격 시스템과 연결을 맺거나 파일을 불러들여야 할 때에는 병목지점이 발생할 수 있습니다. 고맙게도 이렇게 시간을 소요하는 작업을 줄여서 어플리케이션의 성능을 올리는 일을 도와주는 많은 도구들이 있습니다.

여기서도 나온김에 redis를 사용해 cache 데이터로 랭킹을 구축하는 방법에 대해서 시도해봐야겠다.

물론 도커로..

