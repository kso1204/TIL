# API

RESTful JSON API 기초

REST(REpresentational State Transfer)는 API를 만들 때 사용하는 설계 스타일이다.

고유한 URI로 표현할 수 있는 자원을 중심으로 API 구조를 갖춘다. URI를 예로 들면 고양이를 조회하는 URI는 /cats, 15번 아이디를 가진 고양이 한 마리를 조회하는 URI는 /cats/15

상태를 갖지 않는다. 요청과 요청 사이에 유지되는 인증 세션이 없고 모든 요청은 인증 정보를 가지고 있어야 한다.

캐시할 수 있고 일관되게 작동한다.

JSON으로 응답한다.

Laravel 8 - php artisan make:controller Api/DogsController --api 

Laravel 5 - php artisan make:controller Api/DogsController --resource

5와 8의 차이는 8에서 create와 edit 메소드가 제외되었다.

index - 리소스 목록을 보여준다.

store - 새로 생성된 리소스를 스토리지에 저장한다.

show - 특정 리소스를 보여준다.

update - 스토리지에 있는 특정 리소스를 업데이트한다.

destroy - 스토리지에서 특정 리소스를 제거한다.

여기에서 엘로퀀트의 기능을 사용하면 편리하다. 조회 결과로 엘로퀀트 컬렉션을 출력하면 자동으로 JSON으로 변환된다.
```
class DogController extends Controller
{
    public function index()
    {
        return Dog::all();
    }

    public function store(Request $request)
    {
        return Dog::create($request->only(['name', 'bread']));
    }

    public function show($id)
    {
        return Dog::findOrFail($id);
    }

    public function update(Request $request, $id)
    {
        $dog = Dog::findOrFail($id);
        $dog->update($request->only(['name', 'bread']));
        return $dog;
    }

    public function destroy($id)
    {
        Dog::findOrFail($id)->delete();
    }
}
```
Laravel8 -> Route::apiResource를 사용하면 API 리소스 컨트롤러의 메서드를 적절한 라우트와 HTTP 메서드에 자동으로 연결할 수 있다.

Laravel5 -> Route::resource

APIResource를 가공해서 전달하기 위해 리소스 클래스를 만드는데, 5.2에서는 이 부분을 지원하지 않는다.

# 리소스 클래스 만들기

php artisan make:resource Dog

이러면 toArray() 메서드를 가진 app/Http/Resources/Dog.php 클래스가 새로 만들어진다.
```
namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\JsonResource;

class Dog extends JsonResource
{
    public function toArray($request)
    {
        return parent::toArray($request);
    }
}
```
여기서 다루는 toArray() 메서드는 두 가지 중요한 데이터에 접근한다. 

첫째, 일루미네이트 요청 객체에 접근한다. 따라서 쿼리 파라미터나 헤더를 비롯해 요청에 있는 중요한 정보에 기반해서 응답을 변경할 수 있다.

둘째, $this에 속성이나 메서드를 호출해서 변환 중인 엘로퀀트 객체에 접근할 수 있다.
```
class Dog extends JsonResource
{
    public function toArray($request)
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'breed' => $this->breed,
        ];
    }
}
```
새롭게 생성한 리소스를 사용하려면

use App\Http\Resources\Dog as DogResources;

return new DogResource(Dog::find($dogId));

# 리소스 컬렉션

만약 주어진 API 엔드포인트에 반환해야 할 엔티티가 여러 개일 때는 어떻게 하는지 살펴보자.

API 리소스 클래스의 collection() 메서드를 사용하면 된다.

return DogResource::collection(Dog::all());

이 메서드는 전달받은 모든 엔티티를 순회하며 DogResource로 변환하고 컬렉션을 반환한다.

경우에 따라 컬렉션 응답의 구조를 조금이라도 변경하고 싶거나, 메타데이터를 추가하려면 커스텀 API 리소스 컬렉션을 만들어서 해결한다.

php artisna make:resource DogCollection

이 명령어를 실행하면 app/Http/Resources/DogCollection.php에 API 리소스 클래스와 아주 흡사한 toArray() 메서드 하나를 갖고 있는 파일이 하나 생성된다.
```
namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\ResourceCollection;

class DogCollection extends ResourceCollection
{
    public function toArray($request)
    {
        return parent::toArray($request);
    }
}
```
API 리소스 클래스와 마찬가지로 요청과 처리할 데이터에 접근한다. 하지만 API 리소스 클래스와는 달리 단일 항목을 다루지 않고 컬렉션을 다룬다.
따라서 컬렉션을 $this->collection으로 접근한다.
```
class DogCollection extends ResourceCollection
{
    public function toArray($request)
    {
        'data' => $this->collection,
        'links => [
            'self' => route('dogs.index'),
        ],
    };
}
```
# 중첩된 연관관계 표현하기

API의 복잡한 점 중 하나가 연관관계를 표현하는 방법이다.

API 리소스를 사용하여 연관관계를 처리할 수 있는 가장 간단한 방법은 반환하는 배열에 API 리소스 컬렉션을 설정한 키를 추가하는 것이다.
```
class DogCollection extends ResourceCollection
{
    public function toArray()
    {
        return [
            'name' => $this->name,
            'breed' => $this->breed,
            'friends' => DogResource::collection($this->friends),
        ];
    }
}
```
조건에 따라 연관관계가 중첩되게 하는 방법
```
public function toArray()
{
    return [
        'name' => $this->name,
        'breed' => $this->breed,
        //이미 관계를 가지고 잇는 경우에만 연관관계를 추가
        'bones' => BoneResource::collection($this->whenLoaded('bones')),
        //또는 URL이 요청하는 경우에만 연관관계를 추가
        'bones' => $this->when(
            $request->get('include') === 'bones',
            BoneResource::collection($this->bones)
        ),
    ];
}
```
# API 리소스에 페이지네이션 적용하기

return new DogCollection(Dog::paginate(20));

페이지네이터 객체를 전달하면, 변환된 결과에 페이지네이션 정보(첫 페이지, 마지막 페이지, 이전 페이지, 다음 페이지)를 담은 링크와 전체 컬렉션에 대한 메타데이터가 추가된다.

# 조건에 따라 속성 적용하기
```
public function toArray($request)
{
    return [
        'name' => $this->name,
        'breed' => $this->breed,
        'rating' => $this->when(Auth::user()->canSeeRatings(), 12),
    ];
}
```