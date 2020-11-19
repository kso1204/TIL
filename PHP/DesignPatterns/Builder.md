# Builder

출처 : https://refactoring.guru/design-patterns/builder

Builder 는 복잡한 개체를 단계별로 구성 할 수있는 창의적인 디자인 패턴입니다.
패턴을 사용하면 동일한 구성 코드를 사용하여 객체의 다른 유형과 표현을 생성 할 수 있습니다.

- SRP

Single Responsibility Principle.

You can isolate complex construction code from the business logic of the product.

빌더란?
![builder-en](https://user-images.githubusercontent.com/6989005/99023173-60478c80-25a7-11eb-8bd9-5d3ec51a285d.png)

문제
![problem1 (1)](https://user-images.githubusercontent.com/6989005/99023211-72c1c600-25a7-11eb-9ff8-8d87a7f6ac50.png)

해결책
![solution1 (1)](https://user-images.githubusercontent.com/6989005/99023145-56258e00-25a7-11eb-8a81-764b86879482.png)

구조
![structure (1)](https://user-images.githubusercontent.com/6989005/99023309-a3096480-25a7-11eb-9e7b-bd341ecc4ee2.png)

제품을 구성하는 데 사용하는 빌더 단계에 대한 일련의 호출을 director 라는 별도의 클래스로 추출 할 수 있습니다.
director 클래스는 빌드 단계를 실행하는 순서를 정의하고 빌더는 해당 단계에 대한 구현을 제공합니다.

```
<?php

//유용하게 사용할 수 있을 것 같고, 직관적이라서 좋다.

//집을 짓는다. (Builder)
//문이 있는 오두막집을 A라고 하면 (produce1)
//창문이 있는 것은 B (produce2)
//울타리가 있는 것을 C라고 하면 (produce3)

//짓는일(목수?) builder1

//감독이 하는일?
//A집을 지으시오
//A+B+C가 다되어 있는 집을 지으시오

interface Builder
{
    public function producePartA(): void; //문

    public function producePartB(): void; //창문

    public function producePartC(): void; //울타리
}

class ConcreteBuilder1 implements Builder
{
    private $product;

    public function __construct()
    {
        $this->reset();
    } 

    public function reset(): void
    {
        $this->product = new Product1();
    }

    public function productPartA(): void
    {
        $this->product->parts[] = "PartA1";
    }

    public function productPartB(): void
    {
        $this->product->parts[] = "PartB1";
    }

    public function productPartC(): void
    {
        $this->product->parts[] = "PartC1";
    }

    public function getProduct(): Product1
    {
        $result = $this->product;
        $this->reset();

        return $result;
    }
}

class Product1
{
    public $parts = [];

    public function listParts(): void
    {
        echo "Product Parts: ".implode(', ', $This->parts). "\n";
    }
}

class Director
{
    private $builder;

    public function setBuilder(Builder $builder): void
    {
        $this->builder = $builder;
    }

    public function buildMinimalViableProduct(): void
    {
        $this->builder->producePartA();
    }

    public function buildFullFeaturedProduct(): void
    {
        $this->builder->producePartA();
        $this->builder->producePartB();
        $this->builder->producePartC();
    }
}

function clientCode(Director $director)
{
    $builder = new ConcreteBuilder1();
    $director->setBuilder($builder);

    echo "Basic";
    $director->buildMinimalViableProduct(); //문
    $builder->getProduct()->listParts();

    echo "Full";
    $director->buildFullFeaturedProduct(); //문, 창문, 울타리
    $builder->getProduct()->listParts();

    echo "Custom";
    $builder->producePartA(); //문
    $builder->producePartC(); //울타리
    $builder->getProduct()->listParts();
}

$director = new Director();
clientCode($director);


?>
```