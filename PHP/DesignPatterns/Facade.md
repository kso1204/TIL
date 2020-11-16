# Facade

출처 : https://refactoring.guru/design-patterns/facade

Facade 는 라이브러리, 프레임 워크 또는 기타 복잡한 클래스 집합에 대한 단순화 된 인터페이스를 제공하는 구조적 디자인 패턴입니다.

클라이언트가 서브시스템에 직접 접근하지 않고 시스템을 이용할 수 있도록 하는 패턴

facade는 라이프사이클을

![20201116132811](https://user-images.githubusercontent.com/6989005/99212896-96874500-280f-11eb-8242-a8ed41fcf3b0.png)

Facade(외관)

```
<?php

/**
 * The Facade class provides a simple interface to the complex logic of one or
 * several subsystems. The Facade delegates the client requests to the
 * appropriate objects within the subsystem. The Facade is also responsible for
 * managing their lifecycle. All of this shields the client from the undesired
 * complexity of the subsystem.
 */
//복잡한 로직에 대한 간단한 인터페이스 제공과 적절한 서브시스템 제공?
//생명주기를 관리하기도 하고 서브시스템의 복잡함으로부터 클라이언트를 보호한다..?

//작업이 1~n까지 있는 서브시스템 1
//작업이 1~m까지 있는 서브시스템 2
//파사드는 서브시스템1과 서브시스템2에 있는 작업을 관리하는 담당자

class Facade
{
    protected $subsystem1;

    protected $subsystem2;

    public function __construct(Subsystem1 $subsystem1 = null, Subsystem2 $subsystem2 = null)
    {
        $this->subsystem1 = $subsystem1 ?: new Subsystem1();
        $this->subsystem2 = $subsystem2 ?: new Subsystem2();
    }

    public function operation(): string
    {
        $result = "Facade initializes subsystems:\n";
        $result .= $this->subsystem1->operation1();
        $result .= $this->subsystem2->operation1();
        $result .= "Facade orders subsystems to perform the action:\n";
        $result .= $this->subsystem1->operationN();
        $result .= $this->subsystem2->operationZ();

        return $result;
    }
}

/**
 * The Subsystem can accept requests either from the facade or client directly.
 * In any case, to the Subsystem, the Facade is yet another client, and it's not
 * a part of the Subsystem.
 */

// 서브시스템은 파사드나, 클라이언트로부터 요청을 받을 수 있다.
// 파사드 = 클라이언트 != 서브시스템이다?

class Subsystem1
{
    public function operation1(): string
    {
        return "Subsystem1: ready";
    }

    public function operationN(): string
    {
        return "Subsystem1: go";
    }
}

class Subsystem2
{
    public function operation1(): string
    {
        return "Subsystem2: get ready";
    }

    public function operationZ(): string
    {
        return "Subsystem2: fire";
    }
}

function clientCode(Facade $facade)
{
    echo $facade->operation();
}

$subsystem1 = new Subsystem1();
$subsystem2 = new Subsystem2();
$facade = new Facade($subsystem1, $subsystem2);
clientCode($facade);


?>
```