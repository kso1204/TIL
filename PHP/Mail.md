# Mail

라라벨의 메일 기능은 스위프트 메일러를 기반으로 한다.

별다른 설정 없이도 라라벨은 메일건, SES, SMTP, 포스트마크, 로그, 배열, 샌드메일용 드라이버를 기본으로 제공한다.

클라우드 서비스를 사용하려면 config/services.php에 인증정보를 설정해야 한다.

파일을 열어보면 이미 키가 적혀 있고 (config/mail.php에도), .env의 MAIL_MAILER와 MAILGUN_SECRET 같은 변수를 사용해서 

애플리케이션의 메일 기능을 맞춤 설정할 수 있는 것을 볼 수 있다.

클라우드 기반 API 드라이버를 사용한다면

composer require guzzlehttp/guzzle을 프로젝트에 추가해야 한다.

# Mailable 클래스

라라벨에서는 메일 전송 기능을 담당하는 Mailable이라는 클래스가 있다.

이 클래스를 상속한 클래스는 전통적인 메일 문법과 똑같이 작동하고 각각의 메일을 표현하는 역할을 한다.

php artisan make:mail AssignmentCreated

```
class AssignmentCreated extends Mailable
{
    use Queueable, SerializesModels;

    public function __construct()
    {

    }

    public function build()
    {
        return $this->view('view.name');
    }
}
```

이 클래스는 메일을 큐로 처리하기 위한 Queuable 트레이트와 엘로퀀트 모델의 의존성이 추가되어도 문제없이 직렬화할 수 있도록 SerializesModels 트레이트를 사용한다.

build() 메서드를 통해 어떤 뷰를 사용하여 메일 본문을 채워 넣을지, 제목은 무엇으로 할지 등 메일과 관련된 내용을 정의한다.

단 누구에게 보낼지에 대한 정보는 가지고 있지 않다.

만약 메일에서 필요한 데이터가 있다면 생성자에 추가한다.

메일러블에 정의한 public 속성을 템플릿에서 사용할수 있다.

```
class AssignmentCreated extends Mailable
{
    use Queueable, SerializesModels;

    public $trainer;
    public $trainee;

    public function __construct($trainer, $trainee) 
    {
        $this->trainer = $trainer;
        $this->trainee = $trainee;
    }

    public function build()
    {
        return $this->subject($this->trainer->name. '으로부터 새 운동이 할당 되었습니다.')->view('emails.assignment-creted');
    }
}
```

메일러블을 전송하는 방법

Mail:to($user)->send(new AssignmentCreated($trainer, $trainee));

# 큐

애플리케이션에서 이메일을 전송하는 기능은 응답 시간을 느리게 만들 수 있는 작업이다.

따라서 이를 사용자의 요청/응답 과정에서 처리하지 않고, 별도의 백그라운드 큐로 옮겨 비동기로 처리하는 것이 일반적이다.

사실 너무 일반적이어서 라라벨은 이메일 전송을 위한 큐잡을 작성하지 않고도 바로 큐를 사용하여 메시지를 쉽게 처리할 수 있는 기능을 제공한다.

queue()

즉시 전송하는 매일 객체를 큐에 넣는다.

간단하게 메일러블 객체를 Mail::send() 대신 Mail::queue()에 넘겨준다.

Mail::queue(new AssignmentCreated($trainer, $trainee));

later()

Mail::later()는 Mail::queue()와 똑같이 작업하지만 이메일을 언제 큐에서 가져와서 보낼지 정하고 지연하게 해준다.

몇 분 지연할지 지정할 수도 있고 DateTime이나 Carbon 인스턴스를 이용해서 특정 시각을 지정해줄 수 있다.

$when = now()->addMinutes(30);

Mail::later($when, new AssignmentCreated($trainer, $trainee));

queue()와 later() 둘 다 메일이 추가될 큐나 큐 커넥션을 지정하고 싶으면 메일러블 객체에서 onConnection()과 onQueue()메서드를 사용한다.

$message = (new AssignmentCreated($trainer, $trainee))->onConnection('sqs')->onQueue('emails');

Mail:to($user)->queue($message);

지정된 메일러블을 언제나 큐로 처리하고 싶으면 메일러블이 Illuminate\Contracts\Queue\ShouldQueue 인터페이스를 구현하게 한다.

# Mailtrap.io

메일트랩은 개발 환경에서 이메일을 대신 수신하고 검사하는 데 사용하는 서비스다.

