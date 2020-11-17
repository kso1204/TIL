# Template Method

출처 : https://refactoring.guru/design-patterns/template-method

템플릿 메서드는 슈퍼 클래스에서 알고리즘의 골격을 정의하지만 하위 클래스가 구조를 변경하지 않고
알고리즘의 특정 단계를 재정의 할 수 있도록하는 동작 디자인 패턴입니다.

![20201117175036](https://user-images.githubusercontent.com/6989005/99367568-746bf080-28fd-11eb-8a38-cb6f3e961196.png)

![20201117175043](https://user-images.githubusercontent.com/6989005/99367562-73d35a00-28fd-11eb-865f-0a9663ec13e6.png)


```
<?php

//그니까.. templateMethod에있는 function은
//기본적으로 해야하는 것, 구조에 따라 달라지는 것, 알고리즘 앞뒤에 혹시나 추가 될 수 있는 것으로 나뉘는데
//기본적->base
//구조에따라->required
//혹시나->hook

//templateMethod를 하면 선언한 function을 전부 호출하는데,
//A에서 호출할 때 B에서 호출할 때에 따라 기본적인 부분을 제외하고 변동이 생길 수 있어서
//이러한 부분을 전체 재정의하기 힘드니까 template을 만든 패턴이 templatepattern이다.
//final은 자식 클래스에서 상속하지 못하게 정의하는 키워드이다.


abstract class AbstractClass
{
    final public function templateMethod(): void
    {
        $this->baseOperation1();
        $this->requiredOperations1();
        $this->baseOperation2();
        $this->hook1();
        $this->requiredOperations2();
        $this->baseOperation3();
        $this->hook2();
    }

    protected function baseOperation1(): void
    {
        echo "AbstractClass says: I am doing the bulk of the work\n";
    }

    protected function baseOperation2(): void
    {
        echo "AbstractClass says: But I let subclasses override some operations\n";
    }

    protected function baseOperation3(): void
    {
        echo "AbstractClass says: But I am doing the bulk of the work anyway\n";
    }

    /**
     * These operations have to be implemented in subclasses.
     */
    abstract protected function requiredOperations1(): void;

    abstract protected function requiredOperations2(): void;

    /**
     * These are "hooks." Subclasses may override them, but it's not mandatory
     * since the hooks already have default (but empty) implementation. Hooks
     * provide additional extension points in some crucial places of the
     * algorithm.
     */

    protected function hook1(): void { }

    protected function hook2(): void { }
}

class ConcreteClass1 extends AbstractClass
{
    protected function requiredOperations1(): void
    {
        echo "ConcreteClass1 says: Implemented Operation1\n";
    }

    protected function requiredOperations2(): void
    {
        echo "ConcreteClass1 says: Implemented Operation2\n";
    }
}

class ConcreteClass2 extends AbstractClass
{
    protected function requiredOperations1(): void
    {
        echo "ConcreteClass2 says: Implemented Operation1\n";
    }

    protected function requiredOperations2(): void
    {
        echo "ConcreteClass2 says: Implemented Operation2\n";
    }

    protected function hook1(): void
    {
        echo "ConcreteClass2 says: Overridden Hook1\n";
    }
}


function clientCode(AbstractClass $class)
{
    // ...
    $class->templateMethod();
    // ...
}

echo "Same client code can work with different subclasses:\n";
clientCode(new ConcreteClass1());
echo "\n";

echo "Same client code can work with different subclasses:\n";
clientCode(new ConcreteClass2());


?>
```