# Test

출처 : https://modernpug.github.io/php-the-right-way/

테스트 주도 개발 (TDD)

테스트 주도 개발(test-driven development, TDD)은 매우 짧은 개발 사이클을 반복하는 소프트웨어 개발 프로세스 중 하나이다. 우선 개발자는 바라는 향상 또는 새로운 함수를 정의하는 (초기적 결함을 점검하는) 자동화된 테스트 케이스를 작성한다. 그런 후에, 그 케이스를 통과하기 위한 최소한의 양의 코드를 생성한다. 그리고 마지막으로 그 새 코드를 표준에 맞도록 리팩토링한다. 이 기법을 개발했거나 ‘재발견’ 한 것으로 인정되는 Kent Beck은 2003년에 TDD가 단순한 설계를 장려하고 자신감을 불어넣어준다고 말하였다.

유닛 테스트

유닛 테스트(Unit Testing)는 함수, 클래스, 메소드가 기대한 대로 동작하는지를 검증하는 프래그래밍 측면의 접근 방법으로서, 개발을 시작하는 시점부터 계속해서 유닛 테스트를 만들어 나가게 됩니다. 함수나 메소드의 입출력을 검사함으로써 내부 로직이 올바르게 동작하는지를 테스트하는 방식입니다. 의존성 주입(Dependency Injection) 기법을 활용하면서 “모의(mock)” 객체와 스텁(stub)들을 사용하여 서로 의존 관계에 있는 클래스들이 올바르게 연동되어 있는지 테스트함으로써 테스트 커버리지를 더 높일 수 있습니다.

PHPUnit이라는 테스트 프레임워크가 PHP 에서는 거의 업계 표준적인 위치에 있지만 다른 유닛 테스트 프레임워크들도 상당수 존재합니다.

TDD라는 부분에 대해서 개념이 너무 안잡혀서 TDD가 포함된 강의를 하나 들었더니 조금 이해가 됐습니다.

이 부분은 포스트를 보여줄 때 comments를 같이 보여주는 부분에 대한 unittest입니다.

phpunit/vendor/bin --filter test_a_posts_are_returned_with_comments명령어로 실행했습니다.

가장 복잡한 부분을 가져온 것 같은데..

$this->post(~) 이 부분을 설정하면 해당 route를 등록하면서 controller를 등록해야하고

$response->assertStatus(200)->assertJson([
    data ~ 
])

data에 해당하는 내용은 각 클래스의 model + relation, resource, collection 으로 이용되는 집약체입니다.

posts에서 comments데이터를 가져오고 comments에서 어떤 유저가 comments를 남겼는지에 대한 user정보를 가져옵니다.

이정보를 바탕으로 클래스들을 생성하고 테스트가 통과하면 frontend에서 이 데이터를 가져옵니다.

이 강의에서는 각 resource를 생성할 때 data에 type과 해당 id를 넣고

그 내용에 대한 직접적인 data는 attributes로 나누어서 작업했습니다. 

꼭 이렇게 할 필요는 없을 것 같은데,

소스가 길긴해도 알아보기는 쉬울 것 같아 편한데로 이용하면 될 것 같습니다.

근데 이 frontend를 가져올 때 결국 데이터를 가공하게 되는 부분이 들어가는데

이 부분을 frontend에서 담당하는건지에 대한 의문이.. 



```
public function test_a_posts_are_returned_with_comments()
    {
        $user = User::factory()->create();
        $this->actingAs($user, 'api');

        $post= Post::factory()->create(['id'=>123, 'user_id' =>$user->id]);

        $this->post('/api/posts/'.$post->id.'/comment', [
            'body' => 'A great comment here.',
        ]);

        $response = $this->get('/api/posts');

        $comment = Comment::first();
        $response->assertStatus(200)
            ->assertJson([
                'data' => [
                    [
                        'data' => [
                            'type' => 'posts',
                            'attributes' => [
                                'comments' => [
                                    'data' => [
                                        [
                                            
                                            'data' => [
                                                'type' => 'comments',
                                                'comment_id' => 1,
                                                'attributes' => [
                                                    'commented_by' => [
                                                        'data' => [
                                                            'user_id' => $user->id,
                                                            'attributes' => [
                                                                'name' => $user->name,
                                                            ]
                                                        ]
                                                            ],
                                                            
                                                'body' => 'A great comment here.',
                                                'commented_at' => $comment->created_at->diffForHumans(),
                                                ],
                                            ],
                                            'links' => [
                                                'self' => url('/posts/123'),
                                            ]
                                        ]
                                    ]
                                        ,
                                    'comment_count' => 1,
                                ]
                            ]
                        ]
                    ]
                ]
            ]);
    }
    ```