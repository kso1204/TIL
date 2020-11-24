# Redis

Redis 설치 중 관련한 문제..

Laravel Docker 설정 https://aregsar.com/blog/2020/laravel-app-with-redis-in-docker/

이 상태로 설정 바꾸고 기존 홈페이지 들어갔더니

Please make sure the PHP Redis extension is installed and enabled.

이 부분을 해결하기 위해 질문했더니 composer로 설치를 해야 한다고 함..

composer require predis/predis 입력했는데 메모리 오류로 문제 발생..

메모리 오류일경우 swap memory로 해결할 수 있지만

predis말고 pecl로 설치하는 phpredis가 더 좋다고 해서 이 부분 설치하려고 찾아보는데,

설치하는 부분

https://www.lesstif.com/dbms/php-phpredis-redis-23757275.html


php shell 명령어..

```
/var/www/html/game # pecl install redis
downloading redis-5.3.2.tgz ...
Starting to download redis-5.3.2.tgz (266,814 bytes)
........................................................done: 266,814 bytes
29 source files, building
running: phpize
Configuring for:
PHP Api Version:         20190902
Zend Module Api No:      20190902
Zend Extension Api No:   320190902
Cannot find autoconf. Please check your autoconf installation and the
$PHP_AUTOCONF environment variable. Then, rerun this script.

ERROR: `phpize' failed
```

phpize 오류로 인해서

https://panic910.tistory.com/52

M4 및 autoconf 설치
```
# cd /usr/local/download
# wget http://ftp.gnu.org/gnu/m4/m4-1.4.9.tar.gz
# tar -zvxf m4-1.4.9.tar.gz
# cd m4-1.4.9/
# ./configure && make && make install
# cd ../
# wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.62.tar.gz
# tar -zvxf autoconf-2.62.tar.gz
# cd autoconf-2.62/
# ./configure && make && make install
```

오류..

```
/var/www/html/game/m4-1.4.9 # ./configure && make && make install
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... ./install-sh -c -d
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... no
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking for gcc... no
checking for cc... no
checking for cl.exe... no
configure: error: no acceptable C compiler found in $PATH
See `config.log' for more details.
```

해당 내용을 php shell에서 실행하다 보니까 path부분에서 에러가 나는 것 같기도 하다

```
pc11@DESKTOP-L07CI8S MINGW64 ~/php/src/game/m4-1.4.9 (master)
$ ./configure && make && make install
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... no
checking build system type... x86_64-pc-mingw32
checking host system type... x86_64-pc-mingw32
checking for gcc... no
checking for cc... no
checking for cl.exe... no
configure: error: no acceptable C compiler found in $PATH
See `config.log' for more details.
```

ㅜㅜ.. 로컬에서도 똑같이 에러가

https://junemoon.tistory.com/30

rpm도 없고.. yum -y install gcc로 하려면 ubuntu로 가던지 열심히 설치하던지 해야해서..

차라리 swap memory로 일단 진행해보자

ubuntu에서만 사용 가능한 것 같고..

window에서는

pc11@DESKTOP-L07CI8S MINGW64 ~/php/src/game (master)
$ SET COMPOSER_MEMORY_LIMIT=-1
bash: SET: command not found

pc11@DESKTOP-L07CI8S MINGW64 ~/php/src/game (master)
$ export COMPOSER_MEMORY_LIMIT=-1

pc11@DESKTOP-L07CI8S MINGW64 ~/php/src/game (master)
$ php -r "echo ini_get('memory_limit').PHP_EOL;"
128M

pc11@DESKTOP-L07CI8S MINGW64 ~/php/src/game (master)
$ set COMPOSER_MEMORY_LIMIT=-1

pc11@DESKTOP-L07CI8S MINGW64 ~/php/src/game (master)
$ php -r "echo ini_get('memory_limit').PHP_EOL;"
128M

흠..

```
$ COMPOSER_MEMORY_LIMIT=-1 composer.phar update
Loading composer repositories with package information
Updating dependencies (including require-dev)
Package operations: 1 install, 0 updates, 0 removals
  - Installing predis/predis (v1.1.6): Downloading (100%)
predis/predis suggests installing ext-phpiredis (Allows faster serialization and deserialization of the Redis protocol)
Package fzaninotto/faker is abandoned, you should avoid using it. No replacement was suggested.
Writing lock file
Generating optimized autoload files
Deprecation Notice: Class App\Models\BasicAttack located in C:/Users/pc11/php/src/game/app\Models\Decorator.php does not comply with psr-4 autoloading standard. It will not autoload anymore in Composer v2.0. in phar://C:/ProgramData/ComposerSetup/bin/composer.phar/src/Composer/Autoload/ClassMapGenerator.php:201
Deprecation Notice: Class App\Pattern\BasicAttack located in C:/Users/pc11/php/src/game/app\Patterns\Decorator.php does not comply with psr-4 autoloading standard. It will not autoload anymore in Composer v2.0. in phar://C:/ProgramData/ComposerSetup/bin/composer.phar/src/Composer/Autoload/ClassMapGenerator.php:201
Deprecation Notice: Class App\Pattern\Decorator located in C:/Users/pc11/php/src/game/app\Patterns\Decorator.php does not comply with psr-4 autoloading standard. It will not autoload anymore in Composer v2.0. in phar://C:/ProgramData/ComposerSetup/bin/composer.phar/src/Composer/Autoload/ClassMapGenerator.php:201
Deprecation Notice: Class App\Pattern\SkillNumberOne located in C:/Users/pc11/php/src/game/app\Patterns\Decorator.php does not comply with psr-4 autoloading standard. It will not autoload anymore in Composer v2.0. in phar://C:/ProgramData/ComposerSetup/bin/composer.phar/src/Composer/Autoload/ClassMapGenerator.php:201
Deprecation Notice: Class App\Pattern\SkillNumberTwo located in C:/Users/pc11/php/src/game/app\Patterns\Decorator.php does not comply with psr-4 autoloading standard. It will not autoload anymore in Composer v2.0. in phar://C:/ProgramData/ComposerSetup/bin/composer.phar/src/Composer/Autoload/ClassMapGenerator.php:201
Deprecation Notice: Class App\Pattern\SkillNumberThree located in C:/Users/pc11/php/src/game/app\Patterns\Decorator.php does not comply with psr-4 autoloading standard. It will not autoload anymore in Composer v2.0. in phar://C:/ProgramData/ComposerSetup/bin/composer.phar/src/Composer/Autoload/ClassMapGenerator.php:201
Deprecation Notice: Class App\Pattern\SkillNumberFour located in C:/Users/pc11/php/src/game/app\Patterns\Decorator.php does not comply with psr-4 autoloading standard. It will not autoload anymore in Composer v2.0. in phar://C:/ProgramData/ComposerSetup/bin/composer.phar/src/Composer/Autoload/ClassMapGenerator.php:201
> Illuminate\Foundation\ComposerScripts::postAutoloadDump
> @php artisan package:discover --ansi
Discovered Package: facade/ignition
Discovered Package: fideloper/proxy
Discovered Package: fruitcake/laravel-cors
Discovered Package: jn-jairo/laravel-ngrok
Discovered Package: laravel/tinker
Discovered Package: laravel/ui
Discovered Package: nesbot/carbon
Discovered Package: nunomaduro/collision
Package manifest generated successfully.
73 packages you are using are looking for funding.
Use the `composer fund` command to find out more
```

predis가 설치되고 

config/database.php에서 client 설정을

'redis' => [

        'client' => env('REDIS_CLIENT', 'predis'),

로 변경했더니 1차 에러는 사라졌지만,

Predis\Connection\ConnectionException
Connection refused [tcp://127.0.0.1:6379]

연결이 안 되는 상황이 발생했다.