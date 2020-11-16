# FactoryMethod

출처 : https://refactoring.guru/design-patterns/factory-method

Factory method 는 구체적인 클래스를 지정하지 않고 제품 객체를 생성하는 문제를 해결하는 창작 디자인 패턴입니다.




```
abstract class Department {
    public abstract function createEmployee($id);

    public function fire($id) {
        $employee = $this->createEmployee($id);
        $employee->paySalary();
        $employee->dismiss();
    }
}

class ITDepartment extends Department {
    public function createEmployee($id) {
        return new Programmer($id);
    }
}

class AccountingDepartment extends Department {
    public function createEmployee($id) {
        return new Accountant($id);
    }
}
```

```
<?php

//샘플 1

//물류를 배송한다고 생각해보자 (클래스)
//육지 배송과 바다 배송이 있다
//배송을 한다고 생각해보자 (인터페이스)
//배송은 트럭으로도 하고 배로도 한다.

//샘플 2

//제품을 창조(factoryMethod)한다고 생각해보자
//제품 A를 창조하는 방법(factoryMethod)과 제품B를 창조하는 방법(factoryMethod)이 있다.
//제품을 만든다고(Operation) 생각해보자
//제품 A를 만들거나(Operation) 제품 B를(Operation) 만든다. 

//샘플 1이랑 샘플2 설명이 달라서 좀 난해하다.. 쉽게 설명하고 싶은데

abstract class Creator
{
    abstract public function factoryMethod(): Product;

    public function someOperation(): string
    {
        //factoryMethod를 호출하여 product객체를 만든다.
        $product = $this->factoryMethod();
        //product 객체를 사용한다.
        $result = "Creator: 동일한 제작자의 코드로 ". $product->operation();

        return $result;
    }
}

class ConcreteCreator1 extends Creator
{
    public function factoryMethod(): Product
     //abstract product를 사용하면서 Creator가 ConcreteProduct로부터 독립할 수 있다는 부분이 핵심인데
     //완벽하게 이해가 되지 않는다.
    {
        return new ConcreteProduct1();
    }
}

class ConcreteCreator2 extends Creator
{
    public function factoryMethod(): Product
    {
        return new ConcreteProduct2();
    }
}

interface Product
{
    public function operation(): string;
}

class ConcreteProduct1 implements Product
{
    public function operation(): string
    {
        return "{ConcreteProduct1의 결과입니다.}";
    }
}

class ConcreteProduct2 implements Product
{
    public function operation(): string
    {
        return "{ConcreteProduct2의 결과입니다.}";
    }
}

/**
 * The client code works with an instance of a concrete creator, albeit through
 * its base interface. As long as the client keeps working with the creator via
 * the base interface, you can pass it any creator's subclass.
 */

function clientCode(Creator $creator)
{
    echo "Client: 나는 creator클래스를 몰라도 여전히 작동합니다.".$creator->someOperation();
}

/**
 * The Application picks a creator's type depending on the configuration or
 * environment.
 */
echo "App: Launched with the ConcreteCreator1.\n";
clientCode(new ConcreteCreator1());
echo "\n\n";

echo "App: Launched with the ConcreteCreator2.\n";
clientCode(new ConcreteCreator2());

?>
```