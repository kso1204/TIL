# Contracts

https://laravel.kr/docs/8.x/contracts

라라벨의 Contract는 프레임워크에서 제공하는 코어 서비스들을 정의한 인터페이스들의 모음입니다.

예를 들어, Illuminate\Contracts\Queue\Queue Contract에는 어떤 작업들을 큐에서 다룰때 필요한 메소드들이 정의되어 있고,

Illuminate\Contracts\Mail\Mailer Contract에는 이메일을 보내기 위해 필요한 메소드들을 정의되어 있습니다.

라라벨 프레임워크에는 각각의 Contract에 상응하는 구현체(구현 클래스)가 있습니다.

예를 들어, 라라벨은 다양한 드라이버로 구현된 queue의 구현체를 가지고 있고, SwiftMailer를 mailer의 구현체로 가지고 있습니다.

라라벨의 모든 Contract는 각각의 Github 저장소를 가지고 있습니다.

이것은 별도의 패키지에 의존하지 않는 각각의 단일 패키지로, 개발자들이 사용할 수 있도록 하는 contract를 위한 하나의 레퍼런스를 제공합니다.

라라벨의 파사드는 서비스 컨테이너 외부에서 타입 힌트나, contracts 의 의존성 없이도 라라벨의 서비스를 사용할 수 있는 쉬운 방법을 제공합니다.

클래스 생성자에서 요구하지 않아도 되는 facade와 달리 contracts를 통해 클래스에 대한 명시적 의존성을 정의 할 수 있습니다.

일부 개발자는 이러한 방식으로 의존성을 명시적으로 정의하는 contracts를 선호하지만 대다수의 개발자는 facades의 편리함을 누리고 있습니다.

느슨한 결합과 강한 결합으로 설명하는데, 

강한 결합의 예


```
<?php

namespace App\Orders;

class Repository
{
    /**
     * The cache instance.
     */
    protected $cache;

    /**
     * Create a new repository instance.
     *
     * @param  \SomePackage\Cache\Memcached  $cache
     * @return void
     */
    public function __construct(\SomePackage\Cache\Memcached $cache)
    {
        $this->cache = $cache;
    }

    /**
     * Retrieve an Order by ID.
     *
     * @param  int  $id
     * @return Order
     */
    public function find($id)
    {
        if ($this->cache->has($id)) {
            //
        }
    }
}
```

느슨한 결합의 예

이 내용을 보고 단순한 인터페이스에 의존하도록 하여 코드를 개선했다는 걸 바로 알면 Contract에 대한 이해가 잘 된 것이다.

이렇게 접근하는 대신, 특정 벤더에 구속되지 않고 단순한 인터페이스에 의존하도록 하여 코드를 개선할 수 있습니다.

인터페이스에 의존한다. 객체지향..

https://github.com/illuminate/contracts Contract가 가지고 있는 수많은 인터페이스들.. 

```
<?php

namespace App\Orders;

use Illuminate\Contracts\Cache\Repository as Cache;

class Repository
{
    /**
     * The cache instance.
     */
    protected $cache;

    /**
     * Create a new repository instance.
     *
     * @param  Cache  $cache
     * @return void
     */
    public function __construct(Cache $cache)
    {
        $this->cache = $cache;
    }
}
```