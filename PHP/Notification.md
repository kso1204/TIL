# Notification

웹 애플리케이션에서 발송된 대부분의 메일은 실제로 사용자에게 어떤 일이 발생했거나 어떤 조치가 필요하다고 알려주기 위한 것이다.

라라벨은 이런 알림을 위한 기능을 제공하는데 알림은 메일러블 클래스와 같이 사용자에게 보내고자 하는 하나의 커뮤니케이션을 표현하는 PHP 클래스다.

php artisan make:notification WorkoutAvailable

```
class WorkoutAvailable extends Notification
{
    use Queueable;

    public function __constrcut()
    {

    }

    //알림을 조회할 채널 가져오기

    public function via($notifiable)
    {
        return ['mail'];
    }

    //알림을 메일 형식으로 가져오기

    public function toMail($notifiable)
    {
        return (new MailMessages)->line('알림 안내')->action('알림 실행', url('/'))->line('우리 앱을 사용해주셔서 감사합니다');
    }

    //알림을 배열형식으로 가져오기
    public function toArray($notiable)
    {
        return [

        ];
    }
}
```

첫째, 알림에서 필요한 데이터는 생성자로 전달한다.

둘째, via() 메서드로 어떤 알림 채널을 사용할지 정한다. 

($notiable은 시스템에서 알림을 보내고자 하는 대상을 나타낸다. 대부분의 애플리케이션에서 $notiable은 사용자이지만 항상 그런 것은 아니다.)

셋째, 각 알림 채널별 메서드가 있다. 이 메서드에서 각 채널로 알림을 어떻게 전달할지 구체적으로 정의한다.

```
class WorkoutAvailable extends Notifiaction
{
    use Queueable;

    public $workout;

    public function __construct($workout)
    {
        $this->workout = $workout;
    }

    public function via($notiable)
    {
        return $notiable->preferredNotificationChannels();
    }

    public function toMail($notiable)
    {
        return (new MailMessage)->line('새 운동이 할당되었습니다!')->action('지금 확인하세요', route('workout.show', [$this->workout]))->line('함께 운동하게 되어 기쁩니다.');
    }

    public function toArray($notiable)
    {
        return [];
    }

}
```

# 알림 가능한 대상을 위한 via() 메서드


가장 간단하게 사용 가능한 via() 메서드

```
public function via($notiable)
{
    return 'nexmo';
}
```

# 알림을 보내는 두가지 방법

//단일

엘로퀀트 클래스 (예를 들어 User 클래스)에 Notifiable 트레이트를 추가해서 사용

Laravel\Notifications\Notifiable 트레이트를 가져다 쓰는 모든 모델은 알림을 파라미터로 받는 notify() 메서드를 사용할 수 있다.

$user->notify(new WorkoutAvailable($workout));

//다중

Notification 퍼사드를 사용

Notification::send($users, new WorkoutAvailable($workout));

# 알림을 큐로 처리하기

대부분의 알림 드라이버가 알림을 전송하기 위해 HTTP 요청을 필요로 하는데, 이는 애플리케이션의 응답 시간을 느리게 하여 사용자 경험을 저해한다.

모든 알림은 기본적으로 Queueable 트레이트를 가져와 사용하고, 따라서 알림에 ShouldQueue 인터페이스 구현을 추가하기만 하면 큐를 이용할 수 있다.

