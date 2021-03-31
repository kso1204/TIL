# Queue

큐란 무엇일까? 큐 = 은행

은행에가서 업무를 처리하기 위해서 대기표를 받고, 차례가 오면 서비스를 받는다.

애플리케이션은 '잡'을 큐에 추가한다.

잡은 어떻게 특정한 행동을 수행하는지 애플리케이션에 알려주는 일련의 코드다.

큐에 애플리케이션의 잡이 추가되면 일반적으로 큐 워커라는 물리적으로 구분된 애플리케이션 코드가 실행되어 큐에서 한 번에 하나씩 잡을 가져와서 필요한 동작을 수행하는 역할을 맡는다.

큐 워커는 큐에 등록된 잡을 삭제하거나, 지연시킨 뒤에 다시 큐로 돌려보내거나, 동작을 완료하고 성공적으로 처리했다고 표시할 수 있다.

라라벨은 큐 기능을 사용하기 위해서 레디스, 빈스토크, 아마존 심플 큐 서비스(SQS), 데이터베이스 테이블을 이용한 드라비어를 지원한다.

sync 드라이버를 선택하면 큐를 사용하지 않고(비동기 처리하지 않고) 바로 잡을 실행하고, null 드라이버를 선택하면 큐 처리하기 비활성화 된다.

sync와 null은 개발 환경이나 테스트 환경에서 주로 사용된다.

# 큐를 사용하는 이유

큐를 사용하면 동기 호출에서 비용이 많이 들거나 느린 프로세스를 비동기적으로 처리할 수 있다.

한번에 많은 일을 처리하는 크론잡이나 웹훅 호출을 받았을 때, 여러 작업을 연속으로 처리해야 할 때에도 큐를 사용할 수 있다.

또한 하나의 서버가 처리할 수 있는 처리량보다 처리해야 할 작업의 양이 훨씬 더 많은 경우,

일반 애플리케이션 서버 자체적으로 작업을 처리하기보다 큐에 작업을 넣어두고 2개 이상의 큐 워커를 사용하여 처리 속도를 높일 수도 있다.

# 큐 잡

php artisan make:jobb CrunchReports

```
class CrunchReports implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerealizesModels;

    //새로운 잡 인스턴스 생성하기

    public function __construct()
    {

    }

    //잡 실행

    public function handle()
    {

    }
}
```

Dispactable은 자기 자신을 큐에서 빼내는 메서드를 제공한다.

Queueable은 라라벨이 이 잡을 큐에 넣는 방법을 지정하게 하고,

InteractWithQueue는 각 잡이 처리되는 동안 큐에서 해당 잡을 삭제하거나 다시 큐에 넣는 등 큐와의 관계를 제어할 수 있게 한다.

SerializesModels는 엘로퀀트 모델을 직렬화, 역직렬화하는 기능을 제공한다.

```
class CrunchReports implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    protected $user;

    public function __construct($user)
    {
        $this->user = $user;
    }

    public function handle(ReportGenerator $generator)
    {
        $generator->generateReportsForUser($this->user);

        Log::info('보고서가 생성되었습니다');
    }

}
```

잡을 생성할 때 생성자를 통해 User 인스턴스를 주입받고, 이후 잡이 처리될 때 작동하는 handle() 메서드에는 

ReportGenerator를 타입힌트했다.

잡의 handle() 메서드에 작성한 타입힌트는 라라벨이 자동으로 의존성을 주입한다.

# 큐에 잡 추가하기

잡을 큐로 보내는 방법은 많지만, 가장 선호하는 방법은 dispatch() 메서드를 호출하는 방법이다.

이 메서드 외에도 컨트롤러에서 사용 가능한 몇몇 메서드와 글로벌 dispatch() 헬퍼를 호출하는 방법이 있다.

\App\Jobs\CrunchReports::dispatch($user);

# 커넥션 설정하기

DoThingsJob::dispatch()->onConnection('redis');

# 큐 맞춤 설정하기

잡을 어떤 큐에 넣을지 이름을 지정할 수 있다. 예를 들어 Low와 high라는 이름으로 큐를 만들고 중요도에 따라 큐를 구분할 수 있다.

DoThingJob::dispatch()->onQueue('high');

# 지연 시간 설정하기

$delay = now()->addMinutes(5);

DoThingJob::dispathc()->delay($delay);

# 잡 일괄 처리

라라벨 8부터 여러 잡을 한 번에 처리하는 기능이 추가됐다.

잡 일괄 처리는 Bus 퍼사드의 batch() 메서드를 이용해서 수행한다.

이 batch() 메서드에 then(), catch(), finally() 완료 콜백을 연결해서 일괄 처리가 완료되거나 실패하는 상황에 적절한 행동을 취할수 있다.
```
$batch = Bus::batch([
    new ProcessPodcast(Podcast::find(1)),
    new ProcessPodcast(Podcast::find(2)),
])->then(function (Batch $batch) {
    //모든 잡이 성공적으로 완수된 경우
})->catch(function (Batch $batch, Throwable $e) {
    //실패한 잡이 최초로 나타난 경우
})->finally(function (Batch $batch) {
    //일괄 처리가 끝난 후
})->dispatch();

return $batch->id;
```
잡 일괄 처리 기능을 사용하려면 우선 다음의 명령어를 이용하여 일괄 처리 정보를 저장하는 테이블을 만들어야 한다.

php artisna queue:batches-table

php artisan migrate

# 일괄 처리에 프로그래밍 방식으로 잡 추가하기

3개의 LoadImportBatch라는 잡을 일괄 처리하는 부분

```
$batch = Bus::batch([
    new LoadImportBatch,
    new LoadImportBatch,
    new LoadImportBatch,
])->then(function (Batch $batch) {
    //모든 잡을 성공적으로 처리하면 이곳의 코드가 실행됨
})->dispatch()
```

LoadImportBatch에서는 add() 메서드를 이용해서 일괄처리에 잡을 추가한다.
```
public function handle()
{
    if($this->batch()->cancelled()) {
        return;
    }

    $this->batch()->add(Collection::times(1000, function () {
        return new ImportContacts();
    }));
}
```

결과적으로 총 3000개의 ImportContracts 잡을 일괄 처리한다.

# 큐 워커 실행하기

큐 워커는 큐에 들어 있는 잡을 가져와서 실행하는 프로세스다.

다음의 아티즌 명령어를 입력하면 큐 워커가 시작되고 따로 멈추지 않는한 계속 실행된다.

php artisan queue:work

이 명령어를 큐를 수신하는 워커 데몬을 실행한다.

이 데몬은 큐에 잡이 있으면 첫번째 잡을 가져와서 처리하고 삭제한 후 다음 잡을 처리하는 작업을 무한 반복한다.

큐에 잡이 남아있지 않으면 대기 상태로 있다가 일정 시간이 지난 후 다시 처리할 잡이 있는지 확인한다.

대기 상태의 지속 시간은 원하는 대로 설정할 수 있다.

큐 데몬이 멈추기 전까지 잡을 얼마나 오랫동안 실행할 수 있는지(--timeout),

잡이 없을 때 리스너가 얼마나 오랫동안 대기 상태로 있을지(--sleep),

잡을 지우기 전에 얼마나 여러 번 실행을 시도할지(--tries),

어떤 큐 커넥션을 사용할지(queue:work 이후 적어주는 첫 파라미터),

어떤 큐를 수신할지(--queue) 정의할 수 있다.

php artisan queue:work redis --timeout=60 --sleep=15 --tries=3 --queue=high,medium

# 실패한 잡 다루기

최대 재시도 횟수나 최대 예외 횟수를 초과하면 '실패한'잡이 된다. 

먼저 데이터베이스에 실패한 작업을 기록하기 위한 'failed_jobs' 테이블부터 만들어야 한다.

php artisan queue:failed-table

php artisan migrate

첫째, 잡이 실패할 때 클래스에 failed() 메서드가 존재한다면 이 메서드가 호출된다.

여기서는 시스템 관리자에게 알림을 보내는 등의 작업을 수행할 수 있다.
```
class CrunchReports implements ShouldQueue
{
    public function failed()
    {
        //관리자에게 알림을 보내는 등 원하는 모든 작업을 수행한다.
    }
}
```

둘째, 실패한 잡을 위한 글로벌 핸들러를 등록할 수 있다.

AppServiceProvider의 boot()메서드?

```
public function boot()
{
    Queue::failing(function (JobFailed $event) {
        //$event->connectionName
        //$event->job
        //$event->exception
    });
}
```

실패한 잡의 목록을 보여주는 아티즌 명령어

php artisan queue:failed

//특정 아이디 재시도

php artisan queue:retry (id)

php artisan queue:retry all

//특정 아이디 삭제

php artisan queue:forget (id)

//실패한 잡 모두 삭제

php artisan queue:flush

# 라라벨 호라이즌

호라이즌은 레디스 큐의 처리 현황을 보여준다.

어떤 잡이 실패했는지, 얼마나 많은 잡이 대기중이고 얼마나 빨리 처리되는지 볼 수 있다.

큐에 과부하가 걸리거나 실패하면 알림을 받을 수 있다.

https://laravel.kr/docs/horizon 설치, 설정, 배포

