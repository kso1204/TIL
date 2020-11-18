# Visitor

출처 : https://refactoring.guru/design-patterns/visitor

Visitor는 알고리즘이 작동하는 객체에서 알고리즘을 분리 할 수있는 행동 디자인 패턴입니다.

![20201117182340](https://user-images.githubusercontent.com/6989005/99371523-5e146380-2902-11eb-994e-631117fd0585.png)

![20201117182402](https://user-images.githubusercontent.com/6989005/99371526-5f459080-2902-11eb-8741-8c902ed80077.png)

```
<?php

//Component, ConcreteComponent A,B
//Visitor, ConcnreteVisitor A,B

//concreteComponent와 ConcreteVisitor의 조합으로
//같은 함수를 사용해서 결과값을 다르게 도출하는 것
//이런 비슷한 패턴이 있었던 것 같은데..


interface Component
{
    public function accept(Visitor $visitor): void;
}

class ConcreteComponentA implements Component
{
    public function accept(Visitor $visitor): void
    {
        $visitor->visitConcreteComponentA($this);
    }

    public function exclusiveMethodOfConcreteComponentA(): string
    {
        return "A";
    }
}

class ConcreteComponentB implements Component
{
    public function accept(Visitor $visitor): void
    {
        $visitor->visitConcreteComponentB($this);
    }

    public function specialMethodOfConcreteComponentB(): string
    {
        return "B";
    }
}

interface Visitor
{
    public function visitConcreteComponentA(ConcreteComponentA $element): void;
    
    public function visitConcreteComponentB(ConcreteComponentB $element): void;
    
}

class ConcreteVisitor1 implements Visitor
{
    public function visitConcreteComponentA(ConcreteComponentA $element): void
    {
        echo $element->exclusiveMethodOfConcreteComponentA() . " + ConcreteVisitor1\n";
    }

    public function visitConcreteComponentB(ConcreteComponentB $element): void
    {
        echo $element->specialMethodOfConcreteComponentB() . " + ConcreteVisitor1\n";
    }
}

class ConcreteVisitor2 implements Visitor
{
    public function visitConcreteComponentA(ConcreteComponentA $element): void
    {
        echo $element->exclusiveMethodOfConcreteComponentA() . " + ConcreteVisitor2\n";
    }

    public function visitConcreteComponentB(ConcreteComponentB $element): void
    {
        echo $element->specialMethodOfConcreteComponentB() . " + ConcreteVisitor2\n";
    }
}

function clientCode(array $components, Visitor $visitor)
{

    foreach ($components as $component) {
        $component->accept($visitor);
    }

}

$components = [
    new ConcreteComponentA(),
    new ConcreteComponentB(),
];

echo "The client code works with all visitors via the base Visitor interface:\n";
$visitor1 = new ConcreteVisitor1();
clientCode($components, $visitor1);
echo "\n";

echo "It allows the same client code to work with different types of visitors:\n";
$visitor2 = new ConcreteVisitor2();
clientCode($components, $visitor2);

?>
```