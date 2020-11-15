# Prototype

Prototype 은 코드를 클래스에 종속시키지 않고도 기존 객체를 복사 할 수있는 생성 디자인 패턴입니다.


구조
![structure (2)](https://user-images.githubusercontent.com/6989005/99027615-fcc25c80-25b0-11eb-9879-f6a72ecf74a7.png)

프로토 타입 레지스트리 구현

![structure-prototype-cache](https://user-images.githubusercontent.com/6989005/99027611-fb912f80-25b0-11eb-97cb-acf77c08f2b7.png)

```
<?php

// new로 새로운 객체를 생성하는 것보다 clone을 통해 객체를 복제함으로써
// 많은 수의 객체를 다룰 때 메모리 소모량을 줄이기 위해 사용하는 패턴이라고 생각된다.
// primitive의 값이 고정값이 삽입되어서 그런지
// primitive의 값을 clone에서 재정의하지 않아서 그런지
// primitive의 값을 new로 생성하지 않아서 그런지
// 복제 했을 때 primitive의 값을 제외하고는 다 같지 않았다.

class Prototype //복제하는 인터페이스
{
    public $primitive;
    public $component;
    public $circularReference;

    public function __clone()
    {
        $this->component = clone $this->component;
        $this->circularReference = clone $this->circularReference;
        $this->circularReference->prototype = $this;
    }
}

class ComponentWithBackReference //
{
    public $prototype;

    public function __construct(Prototype $prototype)
    {
        $this->prototype = $prototype;
    }
}

function clientCode()
{
    $p1 = new Prototype();
    $p1->primitive = 245;
    $p1->component = new \DateTime();
    $p1->circularReference = new ComponentWithBackReference($p1);

    $p2 = clone $p1;
    if ($p1->primitive === $p2->primitive) {
        echo "Primitive field values have been carried over to a clone. Yay!\n";
    } else {
        echo "Primitive field values have not been copied. Booo!\n";
    }

    if ($p1->component === $p2->component) {
        echo "Simple component has not been cloned. Booo!\n";
    } else {
        echo "Simple component has been cloned. Yay!\n";
    }

    if ($p1->circularReference === $p2->circularReference) {
        echo "Component with back reference has not been cloned. Booo!\n";
    } else {
        echo "Component with back reference has been cloned. Yay!\n";
    }

    if ($p1->circularReference->prototype === $p2->circularReference->prototype) {
        echo "Component with back reference is linked to original object. Booo!\n";
    } else {
        echo "Component with back reference is linked to the clone. Yay!\n";
    }
}

clientCode();
```