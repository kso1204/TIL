# 레포지토리 디자인 패턴

1. 레포지토리 디자인 패턴이란?

레포지토리 디자인 패턴은 데이터 레이어의 추상화이며, 데이터와 액세스 로직 사이의 중간 또는 중간 레이어 역할을 한다.

2. 이점은?

코드를 재사용 가능하고 깨끗하며 유지 관리가 가능하다.

데이터 액세스를 변경할 수 있는 단일 위치이다.

추상화이므로 데이터가 데이터베이스에서 얼마나 정확하게 가져오고 지속되는지에 대한 세부 정보를 숨긴다.

코드를 쉽게 테스트 할 수 있다. (테스트를 위해 레포지토리를 가짜 구현으로 쉽게 교체? 할 수 있으므로 단위 테스트에 사용할 수 있는 데이터 베이스가 필요하지 않다?)

3. Laravel에서 저장소 디자인 패턴을 구현하는 방법은?

```

시나리오 - Post 모델과 PostController

게시물 목록을 가져오고 고유 ID로 단일 게시물을 가져온다.

<?php

namespace App\Http\Controllers;

use App\Http\Requests;
use App\Http\Controllers\Controller

class PostController extends Controller
{
    public function index()
    {
        $data = Post::all();
        return view('posts.index')->with('data',$data);
    }

    public function show($id)
    {
        $data = Post::findOrFail($id)
        return view('posts.show')->with('data',$data);
    }
}

문제

id 또는 post list로 단일 게시물이 필요한 컨트롤러가 몇 개 더있다면 거기에서 정확히 동일한 코드를 반복한다.(중복발생)

이예에서는 엘로퀀트모델을 사용하여 데이터베이스에 데이터를 가져옵니다.

향후 프로젝트에서 지원하지 않는 데이터 소스를 엘로퀀트를 사용해서 변경해야 한다면 애플리케이션을 깨지지 않도록 유지하기 매우 어렵다?

모델과 컨트롤러가 긴밀하게 결합되어 있기 때문에 단위 테스트도 불가능하다

해결책

Laravel 프로젝트의 레포지토리 패턴을 이용한다.

데이터에 액세스하기 위해 컨트롤러에 대해 레포지토리 인터페이스를 사용한다.

따라서 컨트롤러는 느슨하게 결합되고 독립적이며 데이터의 출처와 논리가 어떻게 구현되는지 알 필요가 없다.

따라서 향후 데이터 드라이버를 변경하면 변경 사항을 적용하기 위해 컨트롤러 코드를 변경할 필요가 없다.


>

```

1. 인터페이스 만들기

```

app\Repository 디렉토리에서 PostRepositoryInterface를 사용하여 인터페이스 이름을 만든다.

<?php

namespace App\Repositories

interface PostRepositoryInterface{

    public function getAll();
    
    public function getPost($id);
}

?>

```

2. 저장소 클래스 만들기

```
<?php

namespace App\Repositories

use App\Post;

class PostRepository implements PostRepositoryInterface
{
    public function getAll()
    {
        return Post::all();
    }

    public function getPost($id)
    {
        return Post::findOrFail($id);
    }
}

>
```

3. 컨트롤러 만들기


인터페이스 및 저장소 클래스가 완료되었습니다

이제 PostController 클래스에서 사용하겠습니다.

```
<?php

namesapce App\Http\Controllers;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use App\Repositories\PostRepositoryInterface;

class PostController extends Controller
{
    private $repository;

    public function __construct(PostRepositoryInterface $repository)
    {
        $this->repository = $repository;
    }

    public function index()
    {
        $data = $this->repository->getAll();
        return view('posts.index')->with('data',$data);
    }

    public function show($id)
    {
        $data = $this->repository->getPost($id)
        return view('posts.show')->with('data',$data);
    }
}

>
```

4. 저장소를 등록합니다.

우리는 방금 포스트 Repository를 만들었습니다.

우리의 포스트 컨트롤러는 그것을 사용했지만 라라벨에 어떤 구현이 사용되었는지 우리의 인터페이스를 모릅니다?

포스트 저장소 모듈을 등록하면 AppServiceProvider에 추가합니다.




```

<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    public function register()
    {
        $this->app->bind(
            'App\Repositories\PostRepositoryInterface',
            'App\Repositories\PostRepository'
        )
    }
}

>

```

구현이 완료 됐습니다.

오늘 또는 내일 Post에 대해 다른 데이터소스를 사용해야 하는 경우, 

PostController에 어떠한 변화 없이 PostInterface를 사용하면 됩니다. 사용하는 부분이 아무리 많아져도!

예를들어 엘로퀀트 모델 대신에 firebase 기반의 소스를 사용한다고 하면?

두 부분만 바꿔주면 됩니다.

첫째로 RepositoryInterface를 바인딩하는 새로운 소스를 추가하고 

ex)

```
<?php

namespace App\Repository;

class PostRepositoryInterface implements PostRepositoryInterface
{
    public function getAll()
    {
        // example: http request to get all the post data and return;
    }

    public function getPost()
    {
        // example: http request to get sepcific post data and return;
    }
}

```

그리고 서비스프로바이드에 바인딩 해줍니다.


```

<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    public function register()
    {
        $this->app->bind(
            'App\Repositories\PostRepositoryInterface',
            'App\Repositories\PostRepositoryFirebase'
        )
    }
}

>

```

# 저장소 디자인 패턴에 인터페이스가 필요한 이유는?

위에 작성한 것 처럼 인터페이스는 우리가 원하는대로 더 많은 구현을 할 수 있게 해주기 때문에 사용한다.

새로운 데이터 소스 구현을 위해 사용된 모든 위치를 수동으로 바꾸는 것이 아니라 두 위치에서 변경한다.

# 모든 프로젝트에서 리포지토리를 사용해야 하는가?

작은 프로젝트에서는 리포지토리 패턴을 사용할 필요가 없지만..

대규모 프로젝트의 경우 코드를 더 읽기 쉽고 관리하고 재사용할 수 있다.

