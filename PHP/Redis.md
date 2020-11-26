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

docker-compose.yml에 정의된 잘 모르겠는 부분

command: redis-server --appendonly yes --requirepass "${REDIS_PASSWORD}"

이 부분 삭제


REDIS_HOST=redis
REDIS_PASSWORD=secret
REDIS_PORT=6379
SESSION_CONNECTION=session

redis 호스트와 port를 변경하면서 config:cache 명령어를 입력했더니 새로운 오류가 발생했다.

`AUTH` failed: ERR AUTH <password> called without any password configured for the default user. Are you sure your configuration is correct? [tcp://redis:6379]

그래도 이건 연결하려고 하는데 패스워드가 없다는 것이기 때문에.. 그럼 위에 지운 게 잘못된건가

The REDIS_PASSWORD variable is not set. Defaulting to a blank string.

이 부분을 해결해야 할 것 같다..

기존 설정

redis:
    image: redis:alpine
    container_name: redis
    command: redis-server --appendonly yes --requirepass "${REDIS_PASSWORD}"
    
변경

redis:
    image: redis:alpine
    container_name: redis
    command: redis-server --appendonly yes --requirepass secret
    
나는 REDIS_PASSWORD를 .env파일에 설정한 데이터를 가져오는줄 알았는데..
아니면 저 내부 환경변수에 설정한 데이터를 가져오던지..

직접 삽입하는거라니; 

```
/var/www/html/game # php artisan tinker
Psy Shell v0.10.4 (PHP 7.4.11 — cli) by Justin Hileman
>>> Illuminate\Support\Facades\Redis::connection()->ping();
=> Predis\Response\Status {#3321}
>>> Illuminate\Support\Facades\Redis::connection("default")->ping();
=> Predis\Response\Status {#3328}
>>> Illuminate\Support\Facades\Redis::connection("session")->ping();
=> Predis\Response\Status {#3331}
>>> Illuminate\Support\Facades\Redis::connection("cache")->ping();
=> Predis\Response\Status {#3341}
>>> Illuminate\Support\Facades\Redis::connection("queue")->ping();
=> Predis\Response\Status {#3351}
```

정상적으로 작동하는 것 같다 아닌가?

Redis 파사드

```
/var/www/html/game # php artisan tinker
Psy Shell v0.10.4 (PHP 7.4.11 — cli) by Justin Hileman
>>> $has = Illuminate\Support\Facades\Redis::exists('foo');
=> 0
>>> Illuminate\Support\Facades\Redis::expire('foo',60);
=> 0
>>> Illuminate\Support\Facades\Redis::set('foo','bar');
=> Predis\Response\Status {#3319}
>>> Illuminate\Support\Facades\Redis::expire('foo',60);
=> 1
>>> $has = Illuminate\Support\Facades\Redis::exists('foo');
=> 1
>>> $has = Illuminate\Support\Facades\Redis::exists('foo');
=> 1
>>> $has = Illuminate\Support\Facades\Redis::exists('foo');
=> 0
>>>
```

세션파사드

>>> Illuminate\Support\Facades\Session::put('foo','bar');
=> null
>>> $bar = Illuminate\Support\Facades\Session::get('foo');
=> "bar"
>>> $has = Illuminate\Support\Facades\Session::exists('users');
=> false
>>> Illuminate\Support\Facades\Session::forget('foo');
=> null
>>> $data = Illuminate\Support\Facades\Session::all();
=> []


이건 캐시파사드

```
> Cache::put('foo','bar');
=> true
>>> $bar = Cache::get('foo');
=> "bar"
>>> Cache::forget('foo');
=> true
>>> Cache::put('tmp', 'bar', 60);
=> true
>>> $has = Cache::has('tmp');
=> true
>>> $has = Cache::has('tmp');
=> false
```

캐시 + 저장소 파사드
```
>>> Cache::store('redis')->put('foo','bar');
=> true
>>> $bar = Cache::store('redis')->get('foo');
=> "bar"
>>> Cache::store('redis')->forget('foo');
=> true
>>> $bar = Cache::store('redis')->get('foo');
=> null
```

큐 파사드 및 큐 디스패치 사용
대기열 액세스 방법은 다음의 구성 설정을 사용합니다 config/queue.php.

먼저 백그라운드 처리를 위해 대기 할 수있는 Job 클래스를 만들어야합니다.
테스트를 위해 작업 로그를 메시지로 만들 것입니다.

```
/var/www/html/game # php artisan queue:table
Migration created successfully!
/var/www/html/game # php artisan migrate
Migrating: 2020_11_24_050425_create_jobs_table
Migrated:  2020_11_24_050425_create_jobs_table (167.11ms)
```

Queue로 메일 보내려는 걸 한참 삽질하다가 드디어 해결했는데..

https://www.codechief.org/article/laravel-queues-example-using-redis-and-horizon 도움 된 링크

.env 파일에서


QUEUE_CONNECTION=database

이 부분을 redis로 설정했다

why?

또한 기본 저장 / 연결을 저장 / 연결로 선택하려면 QUEUE_CONNECTIONin .env파일을 로 설정해야 합니다.jobjob

QUEUE_CONNECTION=job

얘가 job으로 설정하라 했는데 나는 redis로 설정했기 때문에 당연히 redis로 설정..

저걸 database로 변경하니까 jobs table에 정상적으로 저장되는 것 확인했다.

2. jobs database로 저장은 안 되더라도 queue에는 저장이 되는지 확인하고 싶었는데,

이 부분이 데이터베이스로 보이지 않으니 어떻게 확인해야 할지 몰랐다.

그래서 log로는 찍히나 봤는데 그 부분도 찍히지 않았다..

php artisan queue:work redis를 하니 이제까지 queue에 쌓여있던 게 전부 failed로 떴는데

왜 failed로 뜨는지 확인할 수 없었고.. 이 부분을 해결하기 위해 구글링 했더니

config/queue.php에서

 'failed' => [
        'driver' => env('QUEUE_FAILED_DRIVER', 'database-uuids'),
        'database' => env('DB_CONNECTION', 'redis'),
        'table' => 'failed_jobs',
    ],

DB_CONNECTION 부분을 mysql->redis로 변경했더니 정상적으로 오류가 저장됐고?

그 오류 내용을 failed_jobs 데이터베이스에서 확인할 수 있었다.

Log::info("ASDF")라는 부분을 넣었는데 클래스를 찾을 수 없다고 오류가 났던 것.. 이 부분이 왜 안되는지 모르겠다.

Log부분을 지우고 queue를 재시작하니 드디어 정상적으로 메일이 왔다.

WelcomeEmailJob::dispatch()->delay(now()->addSecond(3)); 3초후에 queue테이블로 들어가고

php artisan queue:work 하면 queue에 있는 내용이 실행

실패할 경우 failed_job으로 들어가고 성공하면 queue가 삭제되면서 실행된다.

Queue::push(new WelcomeEmailJob());

이건 그냥 Queue에 데이터 넣는 것

이제 redis를 사용해 기존 데이터를 이용한 랭킹 System을 구축해보자 

https://github.com/predis/predis

```
$client = new Predis\Client();
$client->set('foo', 'bar');
$value = $client->get('foo');
dd($value);
```

```
1) Tests\Feature\RedisRankingTest::testExample
Error: Class 'Tests\Feature\Predis\Client' not found
```

흠.. predis로 하니까 zrange가 없는듯하다

https://gist.github.com/lesstif/99a65bc7058e0db1bdea85fd4c726d0e 예제.. 안되고

https://github.com/phpredis/phpredis#zrange phpredis에 zrange가 있다.

$redis-> 뭐를 하려고 하면 다 에러.. connect connection에러 그냥 Redis::get하면 잘 되는데?

phpredis 설치 다시 도전.. C 컴파일러 없다고 했으니까 GCC부터 다시 설치

https://copycoding.tistory.com/285

