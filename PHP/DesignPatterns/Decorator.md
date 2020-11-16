# Decorator

출처 : https://refactoring.guru/design-patterns/decorator

데코레이터 는 이러한 개체를 동작을 포함하는 특수 래퍼 개체 내에 배치하여 개체에 새로운 동작을 연결할 수있는 구조적 디자인 패턴입니다. (Wrapper!)

![decorator](https://user-images.githubusercontent.com/6989005/99207497-7486c600-2801-11eb-92c6-7ff17d2afba8.png)

설명이 직관적으로 되어 있어서 이해하기가 쉽다.

같은 일을 하는 동작에 대해서, 쉽게 확장성을 가지게 한다?

클래스를 확장할 때 상속대신 사용할 수 있는 방법 (why? 상속은 일반적으로 다중 상속을 지원하지 않기 때문에)

One of the ways to overcome these caveats is by using Aggregation or Composition  instead of Inheritance. 

Aggregation/composition is the key principle behind many design patterns, including Decorator.

On that note, let’s return to the pattern discussion.

![solution1-en](https://user-images.githubusercontent.com/6989005/99207815-45bd1f80-2802-11eb-8f6d-1414c39497ac.png)

“Wrapper” is the alternative nickname for the Decorator pattern that clearly expresses the main idea of the pattern. 

Decoration의 핵심

![solution2](https://user-images.githubusercontent.com/6989005/99207861-6d13ec80-2802-11eb-94b9-dd84ae4d39f1.png)

데코레이션은 스택으로 구성된다.

![20201116115508](https://user-images.githubusercontent.com/6989005/99207936-97fe4080-2802-11eb-9fb6-1aa86ea80d03.png)

```
<?php

// 결합되면서 쉽게 확장할 수 있는 방법을 가진 패턴으로
// 필요한 기능들을 추가하여 확장시킬 수 있는 방법이다.
// 옷을 껴입는 상황을 생각

interface Component
{
    public function operation(): string;
}

class ConcreteComponent implements Component
{
    public function operation(): string
    {
        return "ConcreteComponent";
    }
}


/**
 * The base Decorator class follows the same interface as the other components.
 * The primary purpose of this class is to define the wrapping interface for all
 * concrete decorators. The default implementation of the wrapping code might
 * include a field for storing a wrapped component and the means to initialize
 * it.
 */

class Decorator implements Component
{
    protected $component;

    public function __construct(Component $component)
    {
        $this->component = $component;
    }

    public function operation(): string
    {
        return $this->component->operation();
    }
}

class ConcreteDecoratorA extends Decorator
{
    
    /**
     * Decorators may call parent implementation of the operation, instead of
     * calling the wrapped object directly. This approach simplifies extension
     * of decorator classes.
     */
    //Decorator 패턴을 사용하면 간단하게 확장 할 수 있는 이유 

    public function operation(): string
    {
        return "ConcreteDecoratorA(" . parent::operation() . ")";
    }
}

class ConcreteDecoratorB extends Decorator
{
    public function operation(): string
    {
        return "ConcreteDecoratorB(" . parent::operation() . ")";
    }
}

function clientCode(Component $component)
{
    echo "Result: ".$component->operation();
}

$simple = new ConcreteComponent();
echo "Client: I've got a simple component";
clientCode($simple);

$decorator1 = new ConcreteDecoratorA($simple);
$decorator2 = new ConcreteDecoratorB($decorator1);
echo "Client: Now I've got a decorated component:\n";
clientCode($decorator2);

?>
```