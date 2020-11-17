# Chain of Responsibility

출처 : https://refactoring.guru/design-patterns/chain-of-responsibility

Chain of Responsibility 는 핸들러 체인을 따라 요청을 전달할 수있는 동작 디자인 패턴입니다. 
요청을 수신하면 각 핸들러는 요청을 처리하거나 체인의 다음 핸들러로 전달할지 결정합니다.

![chain-of-responsibility](https://user-images.githubusercontent.com/6989005/99325161-12899780-28b9-11eb-996a-3e8fe1399191.png)


![solution1-en (1)](https://user-images.githubusercontent.com/6989005/99325299-61cfc800-28b9-11eb-8c37-c80d1072e037.png)

![20201117094333](https://user-images.githubusercontent.com/6989005/99325296-609e9b00-28b9-11eb-846d-100d55f73678.png)

책임 체인 패턴은 프로그램에 객체 체인이 있어야하기 때문에 PHP에서 그리 일반적이지 않습니다.
PHP에서이 패턴을 사용하는 가장 유명한 예 중 하나는 PSR-15에 설명 된 HTTP 요청 미들웨어 입니다.

```
<?php

//결과도 당연하고 이해하기도 쉬운데,
//코드를 짜기에는 어려운 패턴같다.
//baseinterface에는 연결과 처리
//A->B->C를 연결하고 확인
//Output을 도출할 때 subhandler를 확인하는 데 사실 이 패턴은 A~C까지 전체가 다 true여야 하는 것 아닌가..?

//abstractHandler의 네이밍이 좀 헷갈리게 하는데 일조한 것 같기도 하다..
//setNext(Handler $nextHandler){
//    $this->handler = $nextHandler;
//} 로 하면 좀 덜 헷갈렸을려나

//monkey에서 setNext로 연결을 했는데
//monkey에서 handle(string)을 호출하면"banana"가 아니면
//parent::handle(string)을 호출하게 되는데
//this->nextHandler가 없으면 null을 호출하게 된다
//this->nextHandler가 있는지 없는지 저기서 어떻게 알지? 연결 했으면 그 데이터가 따로 보여지는건가..?
//지금 링크된 상황을 볼 수 있나..?
//이 부분에 대한 코드가 이해가 안 돼서 헷갈리는듯..

interface Handler
{
    public function setNext(Handler $handler): Handler;

    public function handle(string $request): ?string;
}

abstract class AbstractHandler implements Handler
{
    private $nextHandler;

    public function setNext(Handler $handler): Handler
    {
        $this->nextHandler = $handler;

        return $handler;
    }

    public function handle(string $request): ?string
    {
        if ($this->nextHandler) {
            return $this->nextHandler->handle($request);
        }

        return null;
    }
}

class MonkeyHandler extends AbstractHandler
{
    public function handle(string $request): ?string
    {
        if ($request === "Banana") {
            return "Monkey: I'll eat the ". $request .".\n";
        } else {
            return parent::handle($request);
        }
    }
}
class SquirrelHandler extends AbstractHandler
{
    public function handle(string $request): ?string
    {
        if ($request === "Nut") {
            return "Squirrel: I'll eat the " . $request . ".\n";
        } else {
            return parent::handle($request);
        }
    }
}
class DogHandler extends AbstractHandler
{
    public function handle(string $request): ?string
    {
        if ($request === "MeatBall") {
            return "Dog: I'll eat the " . $request . ".\n";
        } else {
            return parent::handle($request);
        }
    }
}

function clientCode(Handler $handler)
{
    foreach (["Nut", "Banana", "Cup of coffee"] as $food) {
        echo "Client: Who wants a " . $food . "?\n";
        $result = $handler->handle($food);
        if ($result) {
            echo "  " . $result;
        } else {
            echo "  " . $food . " was left untouched.\n";
        }
    }
}

$monkey = new MonkeyHandler();
$squirrel = new SquirrelHandler();
$dog = new DogHandler();
$monkey->setNext($squirrel)->setNext($dog);

echo "Chain: Monkey > Squirrel > Dog\n\n";
clientCode($monkey);
echo "\n";

echo "Subchain: Squirrel > Dog\n\n";
clientCode($squirrel);

?>
```