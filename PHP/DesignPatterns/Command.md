# Command

출처 : https://refactoring.guru/design-patterns/command

Command는 요청을 요청에 대한 모든 정보를 포함하는 독립형 개체로 변환하는 동작 디자인 패턴입니다.
이 변환을 통해 서로 다른 요청으로 메서드를 매개 변수화하고, 요청 실행을 지연 또는 대기열에 추가하고,
실행 취소 가능한 작업을 지원할 수 있습니다.

Good software design is often based on the principle of separation of concerns,
which usually results in breaking an app into layers. 

The most common example: a layer for the graphical user interface and another layer for the business logic. 

![20201117111550](https://user-images.githubusercontent.com/6989005/99337773-4323fe00-28c6-11eb-8f19-01dcfa7a6b8c.png)

![20201117111829](https://user-images.githubusercontent.com/6989005/99337933-a2820e00-28c6-11eb-98c8-a72bdbab1db9.png)

![20201117112139](https://user-images.githubusercontent.com/6989005/99338199-13292a80-28c7-11eb-92ba-1e1a06f42b8e.png)

![20201117112205](https://user-images.githubusercontent.com/6989005/99338225-220fdd00-28c7-11eb-97ad-5d52bdfe95d3.png)

```
<?php

//cleancode에 보면 함수에 세 개 이상의 파라미터를 넘기지 말라고 했었던 것 같은데..
//receiver에서 처리해야 할 일들이 많아지면 파라미터가 많아질 것 같아서 생각을 해봤더니,
//너무 많은 일들을 receiver가 처리할 경우엔 객체형태로 넘길 것 같다.
//command객체인지 확인해서 execute를 실행하는 부분이나
//어떤 액션을 처리할 때 처리하기 전, 처리하고 나서에 대한 동작을 지정하는 부분이나
//복잡한 커맨드나 단순한 커맨드를 처리할 수 있는 범용성까지 갖춘 좋은 패턴인 것 같다.
//유용할 것 같은데, 실제로 어떻게 써야 할지 궁금하다

interface Command
{
    public function execute(): void;
}

class SimpleCommand implements Command
{
    private $payload;

    public function __construct(string $payload)
    {
        $this->payload = $payload;
    }

    public function execute(): void
    {
        echo "SimpleCommand: I can do". $this->payload;
    }
}

class ComplexCommand implements Command
{
    private $receiver;

    private $a;

    private $b;

    public function __construct(Receiver $receiver, string $a, string $b)
    {
        $this->receiver = $receiver;
        $this->a = $a;
        $this->b = $b;
    }

    public function execute(): void
    {
        echo "ComplexCommand: Complex stuff should be done by a receiver object.";
        $this->receiver->doSomething($this->a);
        $this->receiver->doSomethingElse($this->b);
    }
}

class Receiver
{
    public function doSomething(string $a): void
    {
        echo "Receiver: Working on".$a;
    }

    public function doSomethingElse(string $b): void
    {
        echo "Receiver: Also working on".$b;
    }
}

class Invoker
{
    private $onStart;

    private $onFinish;

    public function setOnstart(Command $command): void
    {
        $this->onStart = $command;
    }

    public function setOnFinish(Command $command): void
    {
        $this->onFinish = $command;
    }

    public function doSomethingImportant(): void
    {
        echo "Invoker: Dose anybody want something done before I begin";
        if ($this->onStart instanceof Command) //instanceof는 객체인지 확인하는 것 command객체여야 execute를 사용할 수 있어서 그런듯?
        {
            $this->onStart->execute();
        }

        echo "Invoker: ... doing someting really important..? 뭐하는데?";

        echo "Invoker: Does anybody want something done after I finish";
        if ($this->onFinish instanceof Command) {
            $this->onFinish->execute();
        }
    }
}

$invoker = new Invoker();
$invoker->setOnstart(new SimpleCommand("say hi"));
$receiver = new Receiver();
$invoker->setOnFinish(new ComplexCommand($receiver, "Send email", "save report"));

$invoker->doSomethingImportant();




?>
```