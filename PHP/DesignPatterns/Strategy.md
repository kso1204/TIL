# Strategy

출처 : https://refactoring.guru/design-patterns/strategy

Strategy는 알고리즘 패밀리를 정의하고 각 알고리즘을 별도의 클래스에 배치하고 객체를 상호 교환 할 수 있도록하는 행동 설계 패턴입니다.

컨텍스트 클래스에서 자주 변경되는 알고리즘을 식별합니다.

런타임에 동일한 알고리즘의 변형을 선택하고 실행하는 대규모 조건 일 수도 있습니다.

알고리즘의 모든 변형에 공통적인 전략 인터페이스를 선언합니다.

하나씩 모든 알고리즘을 자체 클래스로 추출하십시오. 

그들은 모두 전략 인터페이스를 구현해야합니다.

전략 패턴은 특히 런타임에 알고리즘을 전환해야하는 경우 PHP 코드에서 자주 사용됩니다.

그러나 이 패턴에는 2009 년 PHP 5.3에 도입 된 익명 함수로 대표되는 강력한 경쟁자가 있습니다.


![20201117172724](https://user-images.githubusercontent.com/6989005/99366609-302c2080-28fc-11eb-9050-3d91384cc9dd.png)

![20201117172730](https://user-images.githubusercontent.com/6989005/99366605-2efaf380-28fc-11eb-8b5c-049324d11931.png)


```
<?php

//context에서 dosomebusinesslogic을 설정하면
//strategy에서 생성하는 doalgorithm을 실행한다.
//doalgorithm은 concreteStrategyA인지 B인지에 따라 달라지는데,
//이 A와 B가 strategy 패턴이라고 볼 수 있다.

class Context
{
    private $strategy;

    public function __construct(Strategy $strategy)
    {
        $this->strategy = $strategy;
    }

    public function setStrategy(Strategy $strategy)
    {
        $this->strategy = $strategy;
    }

    public function doSomeBusinessLogic(): void
    {
        echo "Context: Sorting data using the strategy";
        $result = $this->strategy->doAlgorithm(["a","b","c","d","e"]);
        echo implode(", ", $result);
    }
}

/**
 * The Strategy interface declares operations common to all supported versions
 * of some algorithm.
 *
 * The Context uses this interface to call the algorithm defined by Concrete
 * Strategies.
 */

 interface Strategy
 {
     public function doAlgorithm(array $data): array;
 }

 class ConcreteStrategyA implements Strategy
 {
    public function doAlgorithm(array $data): array
    {
        sort($data);

        return $data;
    }
 }

 class ConcreteStrategyB implements Strategy
 {
    public function doAlgorithm(array $data): array
    {
        rsort($data);

        return $data;
    }
 }


 $context = new Context(new ConcreteStrategyA());
 echo "Client: Strategy is set to normal sorting.\n";
 $context->doSomeBusinessLogic();
 
 echo "\n";
 
 echo "Client: Strategy is set to reverse sorting.\n";
 $context->setStrategy(new ConcreteStrategyB());
 $context->doSomeBusinessLogic();



?>
```