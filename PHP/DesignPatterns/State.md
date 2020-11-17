# State

출처 : https://refactoring.guru/design-patterns/state

State는 내부 상태가 변경 될 때 개체가 동작을 변경할 수 있도록하는 동작 디자인 패턴입니다. 
객체가 클래스를 변경 한 것처럼 보입니다.

상태 패턴은 switch연산자를 기반으로하는 크고 번거로운 상태 머신 을 객체로 전환하기 위해 PHP에서 가끔 사용 됩니다.


![20201117165334](https://user-images.githubusercontent.com/6989005/99361466-729e2f00-28f5-11eb-92c1-2121b2cf3f59.png)

```
<?php

//context를 통해서 concreteStateA와 concreteStateB를 상태 변환한다.
//context에서 상태를 저장, 변환, 특정 행동 handler

class Context
{
    private $state;

    public function __construct(State $state)
    {
        $this->transitionTo($state);
    }

    public function transitionTo(State $state): void
    {
        echo "Context: Transition to :".get_class($state);
        $this->state = $state;
        $this->state->setContext($this);
    }

    public function request1(): void
    {
        $this->state->handle1();
    }

    public function request2(): void
    {
        $this->state->handle2();
    }
}

abstract class State
{
    protected $context;

    public function setContext(Context $context)
    {
        $this->context = $context;
    }

    abstract public function handle1(): void;

    abstract public function handle2(): void;
}

class ConcreteStateA extends State
{
    public function handle1(): void
    {
        echo "ConcreteStateA handles request1.\n";
        echo "ConcreteStateA wants to change the state of the context.\n";
        $this->context->transitionTo(new ConcreteStateB());
    }

    public function handle2(): void
    {
        echo "ConcreteStateA handles request2.\n";
    }
}

class ConcreteStateB extends State
{
    public function handle1(): void
    {
        echo "ConcreteStateB handles request1.\n";
    }

    public function handle2(): void
    {
        echo "ConcreteStateB handles request2.\n";
        echo "ConcreteStateB wants to change the state of the context.\n";
        $this->context->transitionTo(new ConcreteStateA());
    }
}

$context = new Context(new ConcreteStateA());
$context->request1(); //A->B로 변경
$context->request2(); //B->A로 변경



?>
```


