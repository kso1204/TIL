# Repository

https://dev.to/safventure/implement-crud-with-laravel-service-repository-pattern-1dkl

https://asperbrothers.com/blog/implement-repository-pattern-in-laravel/

리포지포리 패턴의 많은 이점

데이터 액세스 로직의 중앙 집중화로 코드 유지 관리 용이

비즈니스 및 데이터 액세스 로직은 별도로 테스트

코드 중복 감소

프로그래밍 오류 발생 가능성 감소

Request-> Controller -> Service -> Repository -> Model

요청받은 데이터 가공.. Request

데이터 전달 Controller

서비스 로직 Service

DB 사용 Repository

모델 데이터 사용.. Model

서비스로직.. heal?

DB사용 userRepository?

API 형태로 제작한다고 하면 이럴 때 사실상.. 6개의 컨트롤러가 필요한 것일까?



```
class UsersController extends Controller
{
   public function index()
   {
       $users = User::all();

       return view('users.index', [
           'users' => $users
       ]);
   }
} 
```

Repository의 사용

```
class UsersController extends Controller
{
   private $userRepository;
  
   public function __construct(UserRepositoryInterface $userRepository)
   {
       $this->userRepository = $userRepository;
   }

   public function index()
   {
       $users = $this->userRepository->all();

       return view('users.index', [
           'users' => $users
       ]);
   }
}
```

폴더 구조

```
-- app
---- Repository
------ Eloquent
-------- UserRepository.php
-------- BaseRepository.php
------ UserRepositoryInterface.php
------ EloquentRepositoryInterface.php
```
