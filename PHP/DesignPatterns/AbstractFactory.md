# Abstract Factory

출처 : https://refactoring.guru/design-patterns/abstract-factory

Abstract Factory 는 구체적인 클래스를 지정하지 않고도 관련 객체의 패밀리를 생성 할 수있는 창조 디자인 패턴입니다.

![structure](https://user-images.githubusercontent.com/6989005/99019818-89b0ea00-25a0-11eb-9f51-3c578f5db291.png)

가구점 시뮬레이터를 만들고 있다고 상상해보십시오. 코드는 다음을 나타내는 클래스로 구성됩니다.

관련 제품군, 예 : Chair+ Sofa+ CoffeeTable.

이 제품군의 여러 변형. 

예를 들어, 제품 Chair+ Sofa+는 CoffeeTable이러한 변형에서 사용할 수 있습니다 : Modern, Victorian, ArtDeco.

![problem-en](https://user-images.githubusercontent.com/6989005/99019323-6afe2380-259f-11eb-8666-c38a52c6f129.png)

동일한 패밀리의 다른 오브젝트와 일치하도록 개별 가구 오브젝트를 작성하는 방법이 필요합니다. 고객은 일치하지 않는 가구를 받으면 매우 화가납니다.


```
<?php

//productA 

//가구공장에서 의자랑, 커피테이블이랑 소파를 만들 수 있는데.

//A가구공장은 모던하게 만들고 (뭐를? 의자랑, 커피테이블, 소파를)
//B가구공장은 화려하게 만들어

//가구공장은 interface(AbstractFactory고)

//A가구공장은 ConcreteFactory1 
//B가구공장은 ConcreteFactory2

//모던의자는 ConcreteProductA1()
//모던소파는 ConcreteProductB1()

//화려의자는 ConcreteProductA2()
//화려소파는 ConcreteProductB2() 

//콘크리트 팩토리는 구체적인 제품을 인스턴스화하지만 생성 방법의 서명은 해당 추상 제품을 반환해야합니다 .
//이렇게하면 공장을 사용하는 클라이언트 코드가 공장에서 가져온 특정 제품 변형에 결합되지 않습니다. 
//클라이언트 가 추상적 인 인터페이스를 통해 해당 개체와 통신하는 한, 어떤 콘크리트 공장 / 제품 변형 작업 할 수 있습니다.

interface AbstractFactory
{
    public function createProductA(): AbstractProductA; //의자

    public function createProductB(): AbstractProductB; //소파
}

class ConcreteFactory1 implements AbstractFactory
{
    public function createProductA(): AbstractProductA
    {
        return new ConcreteProductA1();
    }

    public function createProductB(): AbstractProductB
    {
        return new ConcreteProductB1();
    }
}
class ConcreteFactory2 implements AbstractFactory
{
    public function createProductA(): AbstractProductA
    {
        return new ConcreteProductA2();
    }

    public function createProductB(): AbstractProductB
    {
        return new ConcreteProductB2();
    }
}


interface AbstractProductA
{
    public function usefulFunctionA(): string;
}

class ConcreteProductA1 implements AbstractProductA
{
    public function usefulFunctionA():string
    {
        return "The result of the product A1.";
    }
}



class ConcreteProductA2 implements AbstractProductA
{
    public function usefulFunctionA():string
    {
        return "The result of the product A2.";
    }
}


interface AbstractProductB
{
    public function usefulFunctionB(): string;

    /**
     * ...but it also can collaborate with the ProductA.
     *
     * The Abstract Factory makes sure that all products it creates are of the
     * same variant and thus, compatible.
     */
    

    public function anotherUsefulFunctionB(AbstractProductA $collaborator): string;
}

class ConcreteProductB1 implements AbstractProductB
{
    public function usefulFunctionB(): string
    {
        return "The result of the product B1.";
    }
    /**
     * The variant, Product B1, is only able to work correctly with the variant,
     * Product A1. Nevertheless, it accepts any instance of AbstractProductA as
     * an argument.
     */
    public function anotherUsefulFunctionB(AbstractProductA $collaborator): string
    {
        $result = $collaborator->usefulFunctionA();

        return "The result of the B1 collaboration with the ({$result})";
    }

}

class ConcreteProductB2 implements AbstractProductB
{
    public function usefulFunctionB(): string
    {
        return "The result of the product B2.";
    }
    /**
     * The variant, Product B1, is only able to work correctly with the variant,
     * Product A1. Nevertheless, it accepts any instance of AbstractProductA as
     * an argument.
     */
    public function anotherUsefulFunctionB(AbstractProductA $collaborator): string
    {
        $result = $collaborator->usefulFunctionA();

        return "The result of the B2 collaboration with the ({$result})";
    }

}

function clientCode(AbstractFactory $factory)
{
    $productA = $factory->createProductA();
    $productB = $factory->createProductB();

    echo $productB->usefulFunctionB()."\n";
    echo $productB->anotherUsefulFunctionB($productA)."\n";
}

echo "Client: Testing Client code with the factory Type";
clientCode(new ConcreteFactory1());

echo "Client: Testing the same client code with the second factory type:\n";
clientCode(new ConcreteFactory2());

?>
```