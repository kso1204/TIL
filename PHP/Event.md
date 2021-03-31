# Event

잡을 이용할 때는 호출된 코드가 애플리케이션에게 어떤 일(CrunchReports나 NotifyAdminOfNewSignup)을 해야 한다고 알려준다.

반면 이벤트를 이용하면 호출된 코드가 애플리케이션에게 어떤 일이 일어났다고 알려준다.

예를 들어 사용자가 구독했다든지(UserSubscribed),

회원가입을 했다든지(UserSignedUp),

연락처가 추가됐다(ContactWasAddes)는 것들이다.

이벤트는 발생한 어떤 일에 대한 시스템의 알림이다.

이벤트가 발생하는 것만으로는 아무 일도 일어나지 않고, 이 이벤트를 수신하는

이벤트 리스너를 생성해야 한다.

리스너의 목적은 특정 이벤트가 발생하는 걸 감지하고 이에 대응해 필요한 동작을 처리하는 것이다.

모든 이벤트는 이벤트 리스너를 하나도 안 가질 수도 있고 여러 개 가질 수도 있다.

라라벨의 이벤트 관찰자 혹은 발행/구독(pub/sub) 패턴과 같은 구조를 갖는다.

애플리케이션에서 많은 이벤트가 발생하지만 어떤 이벤트는 리스너가 하나도 없는 반면,

어떤 이벤트는 리스너 수십 개를 가질 수도 있다.

이벤트는 리스너가 있는지 없는지 신경 쓰지 않는다.

# 이벤트 발생시키기

이벤트를 발생시키는 방법은 총 세 가지다.

Event 퍼사드를 사용하거나,

Dispatcher를 주입하거나

event() 글로벌 헬퍼를 사용할 수 있다.

Event::fire(new UserSubscribed($user, $plan));

$dispatcher = app(Illuminate\Contracts\Events\Dispatcher::class),

$dispatcer->fire(new UserSubscribed($user, $plan));

event(new UserSubscribed($user, $plan));

새로운 이벤트 클래스를 생성하려면 make:event 아티즌 명령어를 사용한다.

php artisan make:event UserSubscribed

```
class UserSubscribed
{
    use Dispatchable, InteractsWithSockes, SerializesModels;

    //새로운 인스턴스 생성하기

    public function __construct()
    {

    }

    //이벤트가 브로드캐스트될 채널 가져오기

    public function broadcastOn()
    {
        return new PrivateChannel('channel-name');
    }
}
```

broadCastOn() 메서드는 WebSockets()을 이용해서 이벤트를 브로드캐스트하는 데 필요한 기능을 제공한다.

handle()이나 fire() 메서드가 보이지 않는다는 점이 다소 의아해 보일 수도 있다.

하지만 이 객체는 특정 로직을 처리하기 위해서가 아니라 단순히 어떤 데이터를 캡슐화하기 위해 존재한다는 점을 기억하자.

먼저클래스명 UserSubscribed는 사용자의 구독이라는 이벤트가 발생했다는 것을 알려준다.

그리고 생성자 메서드에는 이 이벤트가 나타내고자 하는 데이터와 연결되는 정보를 담는 변수가 정의될 수 있다.

다음은 UserSubscribed 이벤트 클래스에 어떤 데이터를 추가할 수 있는지에 대한 예다.

```
class UserSubscribed
{
    use InteractsWithSockets, SerailizesModels;

    public $user;
    public $plan;

    public function __construct($user, $plan)
    {
        $this->user = $user;
        $this->plan = $plan;
    }
}
```

이제 발생한 이벤트를 적절히 표현하느 객체를 갖게 됐다.

$event->user가 $event->plan 요금제를 구독한 것이다.

event(new UserSubscribed($user, $plan))로 이 이벤트를 발생시킬 수 있다.

# 이벤트 수신하기

새로운 구독자가 있을 때마다 애플리케이션 운영자에게 이메일을 보낸다고 가정하자.

php artisan make:listener EmailOwnerAboutSubscription --event=UserSubscribed

```
class EmailOwnerAboutSubscription
{
    //이벤트 리스너 생성하기

    public function __construct()
    {
        //
    }

    //이벤트 처리하기

    public function handle(UserSubscribed $event)
    {
        //
    }
}
```

모든 일은 handle() 메서드에서 일어난다.

이 메서드는 UserSubscribed 타입의 이벤트를 넘겨받고 이 이벤트에 들어있는 데이터를 사용하여 필요한 동작을 처리한다.

이벤트를 수신하여 이메일을 보내는 코드

```
class EmailOwnerAboutSubScription
{
    public function handle(UserSubscribed $event)
    {
        Log::info('새로운 사용자에 대한 이메일을 운영자에게 발송했다.'. $event->user->email);

        Mail::to(config'app.owner-email')->send(new UserSubscribedMessage($event->user, $event->plan));
    }
}
```

이제 이 리스너가 UserSubscribed 이벤트를 수신할 수 있도록 설정하는 일만 남았다.

EventServiceProvider 클래스의 $listen 속성에 다음과 같이 설정한다.

class EventServiceProvider extends ServiceProvider
{
    protected $listen = [
        \App\Events\UserSubscribed::class => [
            \App\Listeners\EmailOwnerAboutSubscription::class,
        ],
    ];
}

각 배열 항목의 키는 이벤트의 클래스명이고, 값은 리스너 클래스명의 배열이다.

UserSubscribed 키에 필요한 클래스명을 추가할 수 있고, UserSubscribed 이벤트를 발생하면 여기에 추가한 모든 리스너가 이 이벤트를 수신하고 반응할 것이다.

# 이벤트 자동 발견

라라벨 5.8부터는 EventServiceProvider에서 직접 이벤트와 리스너를 연결하지 않아도 이벤트와 리스너를 자동으로 연결하게 설정할 수 있다.

이 기능은 기본적으로 비활성화 되어 있다.

활성화하려면

EventServiceProvider의 ShouldDiscoverEvents 메서드가 true를 반환하도록 설정한다.

```
public function shouldDiscoverEvents()
{
    return true;
}
```

이 기능을 활성화하면 리스너에 타입힌트된 것을 기반으로 이벤트와 리스너를 매칭한다.

매 요청마다 매칭을 실행하므로 전체적으로 애플리케이션의 성능이 조금 안 좋아진다.

php artisan event:cache 명령어를 사용해 이벤트 캐시 기능을 사용하면 성능 저하를 방지할 수 있다.

# 이벤트 구독자

이벤트와 이를 처리하는 리스너의 관계를 정의하는 또 다른 구조가 있다.

라라벨은 이벤트 구독자라는 개념을 가지고 있는데, 이는 여러 이벤트에 대해 각각의 리스너로 작동하는 메서드 여러 개를 가진 클래스다.

또한 어떤 이벤트를 어떤 메서드에 처리할지 매핑하는 클래스다.

```
namespace App\Listeners;
class UserEventSubscriber
{
    public function onUserSubscription($event)
    {
        //UserSubscribed 이벤트를 처리한다.
    }

    public function onUserCancellation($event)
    {
        //UserCanceled 이벤트를 처리한다.
    }

    public function subscribe($event)
    {
        $event->listen(
            \App\Events\UserSubscribed::class,
            'App\Listeners\UserEventSubscriber@onUserSubscript'
        );

        $event->listen(
            \App\Events\UserCanceled::class,
            'App\Listeners\UserEventSubscriber@onUserCancellation'
        );
    }
}
```

구독자 클래스는 subscribe() 메서드를 가지고 있어야 한다.

subscribe() 메서드는 이벤트 디스패처 객체 인스턴스를 인자로 전달받는다.

이 디스패처를 이용해서 어떤 이벤트가 리스너를 통해서 처리될지 알려주어야 한다.

여기서는 별도의 리스너 클래스 대신 구독자 클래스의 메서드와 연결했다.

구독자 클래스명을 EventServiceProvider의 $subscribe 속성에 추가해야 한다.

```
protected $subscribe = [
    \App\Listeners\UserEventSubscriber::class
];
```

# 웹소켓과 라라벨 에코를 이용한 이벤트 브로드캐스팅

웹소켓이란 HTTP와는 다른 별개의 프로토콜을 의미한다.

우리가 흔히 사용하는 HTTP 또는 HTTPS 접속은 서버의 클라이언트(일반적으로는 브라우저)의 연결이 한 번 데이터를 전송 받은 뒤에는 끊어지지만 웹소켓은 이 연결을 계속 유지한다.

따라서 푸셔(웹소켓 SaaS)와 같은 서비스를 이용하면 거의 실시간으로 웹 디바이스간 커뮤니케이션을 제공할 수 있다.

지메일이나 페이스부겡서의 채팅 기능은 실시간처럼 보이지만 웹소켓이 아닌 자바스크립트 Ajax를 기반으로 하는 기능이기 때문에,

브라우저 내부에서 지속적으로 데이터를 요청하는 동작이 필요하다.

웹소켓 라이브러리는 HTTP 요청을 사용하여 데이터를 전달받는 대신 클라이언트와 서버 간 직접 연결을 주고받는다.

그래서 기다릴 필요가 없고 실시간으로 데이터를 주고 받는다.

# 웹소켓 이벤트의 구조

웹소켓으로 보내는 이벤트는 이름, 채널, 데이터 세 가지로 구성된다.

라라벨은 App\Events\UserSubscribed와 같이 이벤트의 정규화된 클래스명을 사용한다.

이벤트 클래스에서 broadcastAs() 메서드를 정의한다면, 이 메서드가 반환하는 문자열을 이름으로 사용하고 그렇지 않다면 클래스명을 사용한다.

채널은 메시지를 수신할 클라이언트가 누구인지 나타내는 것이다.

개별 사용자를 위한 채널, 특정 유형에 소속된 사용자들을 위한 채널, 비공개 채널 등이 있다.

데이터는 이벤트와 관련된 정보의 페이로드로 보통 JSON을 사용한다. 

이벤트가 브로드캐스트하는 데이터는 채팅 메시지일 수도 있고, 사용자 정보일 수도 있고, 이를 소비하는 자바스크립트를 위한 참조 데이터일 수도 있다.

# 메시지 수신하기

레디스를 웹소켓 서버로 사용할 때 socket.io와 ioredis를 이용해서 설정하는 방법이 https://laravel.kr/docs/broadcasting#Socket.IO 에 잘 나와있다.

# 스케줄러

배치 작업 등을 처리하기 위해서 크론 잡을 사용해본 경험이 있는가?

크론보다 좋은 방법 -> 스케줄러

app/Console/Kernel.php에 정의된 schedule() 메서드를 이용해서 예약 작업을 등록할 수 있다.

클로저를 사용해 라라벨 스케줄러에 작업을 등록

```
public function schedule(Schedule $schedule)
{
    $schedule->call(function () {
        CalculateTotals::dispatch();
    })->everyMinute();
}
```

# 작업의 결과 처리하기

예약 작업이 실행될 때 로그를 남기거나 알림을 보내거나 단순히 작업이 정사적으로 실행됐는지 확인하는 등의 작업 결과를 처리하고 할 때가 있다.

작업이 실행될 때 발생하는 출력 결과를 파일에 작성하고 싶으면 sendOutputTo()를 사용한다.

# 작업 훅

예약 작업이 실행되기 전후에 무엇인가 추가적인 작업을 하려면 before(), after() 훅 기능을 사용한다.

