# Aws에서 Docker로 Game project 띄우기

우선.. aws에서 EC2로 인스턴스 생성하고 프리 티어 ubuntu 버전 20 선택

key 생성하고 인스턴스 생성하면 보안그룹 추가

http와 https를 추가하고..

ssh 연결

https://hcnam.tistory.com/25 도커 설치하는 부분 주소..

도커 설치되면 dockerfile이랑 docker-compose.yml 파일 등록하고
Dockerfile
```
FROM php:7.4-fpm-alpine

RUN apk add autoconf automake make gcc g++ libtool pkgconfig libmcrypt-dev re2c git zlib-dev xdg-utils libpng-dev freetype-dev libjpeg-turbo-dev openssh-client libxslt-dev ca-certificates gmp-dev 

RUN apk add --no-cache pcre-dev $PHPIZE_DEPS \
        && pecl install redis \
        && docker-php-ext-enable redis.so

RUN docker-php-ext-install pdo pdo_mysql sockets 

```

docker-compose.yml
```
version: '3'

networks:
    laravel:

services:
    nginx:
        image: nginx:latest
        container_name: nginx
        ports:
            - "80:80"
        volumes:
            - ./src:/var/www/html
            - ./nginx:/etc/nginx/conf.d
        depends_on:
            - php
            - mysql
        networks:
            - laravel

    mysql:
        image: mysql:5.7.22
        container_name: mysql
        restart: unless-stopped
        tty: true
        ports:
            - "4306:3306"
        volumes:
            - ./mysql:/var/lib/mysql
        environment: 
            MYSQL_DATABASE: homestead
            MYSQL_USER: homestead
            MYSQL_PASSWORD: secret
            MYSQL_ROOT_PASSWORD: secret
            SERVICE_TAGS: dev
            SERVICE_NAME: mysql
        networks:
            - laravel
    php:
        build:
            context: .
            dockerfile: Dockerfile
        container_name: php
        volumes:
            - ./src:/var/www/html
        ports:
            - "9000:9000"
        networks:
            - laravel
    phpmyadmin:
        image: phpmyadmin/phpmyadmin:latest
        environment:
            PMA_HOST: mysql
        ports:
            - "8080:80"
        networks: 
            - laravel
    redis:
        image: redis:alpine
        container_name: redis
        command: redis-server --appendonly yes --requirepass secret
        volumes:
            - ./redis:/data
        ports:
            - "6379:6379"
        networks:
            - laravel
```



각 폴더를 생성한 다음 docker-compose build

nginx 같은 경우 default.conf 생성해서

```
server {
    listen 80;
    index index.php index.html;
    server_name localhost;
    error_log /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    root /var/www/html/game/public;

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

해당 내용 넣어주고 

git clone으로 game 프로젝트 가져온 다음 composer install

git clone으로 데이터 가져올 때 ssh key 등록하려면

cd ~/.ssh && ssh-keygen

cat id_rsa.pub

해당 내용 복사해서 git - setting - ssh에서 key 등록한다음 clone하면 된다.

주소창에 인스턴스 IP 주소를 넣으면 연결이 되지 않는다..

원래 기존에 aws에서 작업했을 때 연결이 되지 않았을 경우 어떻게 해결하는지 알았는데;

그 방법을 까먹었어서.. 다신 까먹지 않기 위해 이번에 작성

nginx설정도 제대로 되어 있고 git으로 데이터도 제대로 가져 왔는데, .env 파일을 생성하지 않아서 아예 연결이 안 된듯?..

cp .env.example .env 설정하고 

mysql, redis 설정을 잡아준다.

php artisan key:generate하고

chown -R $USER:www-data storage
chown -R $USER:www-data bootstrap/cache
 
chmod -R 775 storage
chmod -R 775 bootstrap/cache

log파일이 권한 때문에 쓰기가 안 돼서 이 부분 작성해주고

php artisan migrate, php artisan db:seed 하면 초기 데이터 설정된다.

그다음 게임 플레이..! 

aws에서 docker를 사용해볼 때 테스트하기 좋고.. 한시간 내외로 걸리는 것 같다.



