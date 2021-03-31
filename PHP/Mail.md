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

