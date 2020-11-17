# Mediator

출처 : https://refactoring.guru/design-patterns/mediator

Also known as: Intermediary, Controller

Mediator는 개체 간의 혼란스러운 종속성을 줄일 수있는 행동 설계 패턴입니다. 
이 패턴은 개체 간의 직접 통신을 제한하고 중재자 개체를 통해서만 공동 작업하도록합니다.

![20201117141600](https://user-images.githubusercontent.com/6989005/99349477-745cf800-28df-11eb-9f70-489ca18390e4.png)

```
<?php

//mediator, ConcreteMediator..
//BaseComponent, Component.. 

//컴포넌트의 명령을 수행하면서 mediator의 event수행
//흠.. concreteMediator에서 setmediator 해주는 부분이 좀 신기한건가?
//이거는 다른 예제를 봐야할 것 같다.

interface Mediator
{
    public function notify(object $sender, string $event): void;
}


/**
 * Concrete Mediators implement cooperative behavior by coordinating several
 * components.
 */

class ConcreteMediator implements Mediator
{
    private $component1;

    private $component2;

    public function __construct(Component1 $c1, Component2 $c2)
    {
        $this->component1 = $c1;
        $this->component1->setMediator($this);
        $this->component2 = $c2;
        $this->component2->setMediator($this);
    }

    public function notify(object $sender, string $event): void
    {
        if ($event == "A") {
            echo "Mediator reacts on A and triggers following operations:";
            $this->component2->doC();
        }

        if ($event == "D") {
            echo "Mediator reacts on D and triggers follwing operations:";
            $this->component1->doB();
            $this->component2->doC();
        }
    }
}

/**
 * The Base Component provides the basic functionality of storing a mediator's
 * instance inside component objects.
 */

 class BaseComponent
 {
     protected $mediator;

     public function __construct(Mediator $mediator = null)
     {
         $this->mediator = $mediator;
     }

     public function setMediator(Mediator $mediator): void
     {
         $this->mediator = $mediator;
     }
 }

 class Component1 extends BaseComponent
 {
     public function doA(): void
     {
         echo "Comp1 does A";
         $this->mediator->notify($this, "A");
     }

     public function doB(): void
     {
        echo "Comp1 does B";
        $this->mediator->notify($this, "B");

     }
 }
 

 class Component2 extends BaseComponent
 {
     public function doC(): void
     {
         echo "Comp2 does C";
         $this->mediator->notify($this, "C");
     }

     public function doD(): void
     {
        echo "Comp2 does D";
        $this->mediator->notify($this, "D");

     }
 }

 $c1 = new Component1();
 $c2 = new Component2();

$mediator = new ConcreteMediator($c1, $c2);

echo "Client triggers operation A";
$c1->doA();
echo "Client triggers operation D";
$c2->doD();
?>
```