# Adapter

출처 : https://refactoring.guru/design-patterns/adapter

어댑터 는 호환되지 않는 인터페이스를 가진 객체가 협업 할 수 있도록하는 구조적 디자인 패턴입니다.

주식 시장 모니터링 앱을 만들고 있다고 상상해보십시오. 이 앱은 XML 형식의 여러 소스에서 주식 데이터를 다운로드 한 다음 사용자에게 멋진 차트와 다이어그램을 표시합니다.

어느 시점에서 스마트 타사 분석 라이브러리를 통합하여 앱을 개선하기로 결정합니다. 하지만 한 가지 문제가 있습니다. 분석 라이브러리는 JSON 형식의 데이터로만 작동합니다.

![problem-en (1)](https://user-images.githubusercontent.com/6989005/99201738-caeb0900-27ef-11eb-8731-4a0d39b2ea04.png)

![solution-en](https://user-images.githubusercontent.com/6989005/99201735-c9b9dc00-27ef-11eb-9dc4-6c592f3ac7ee.png)

![structure-object-adapter](https://user-images.githubusercontent.com/6989005/99201790-0ab1f080-27f0-11eb-817e-d352f9857c07.png)

```
<?php

//작동방법이 달라서 직접적으로 실행하기 어려울 때
//Adpater에서 변환을 해줌


class Target
{
    public function request(): string
    {
        return "Target: The default target's behavior.";
    }
}

/**
 * The Adaptee contains some useful behavior, but its interface is incompatible
 * with the existing client code. The Adaptee needs some adaptation before the
 * client code can use it.
 */

//Adaptee가 실제로 행하는 것이고 클라이언트와 독립적이다?

class Adaptee
{
    public function specificRequest(): string
    {
        return ".eetpadA eht roivaheb laicepS";
    }
}

class Adapter extends Target
{
    private $adaptee;

    public function __construct(Adaptee $adaptee)
    {
        $this->adaptee = $adaptee;
    }

    public function request(): string
    {
        return "Adapter: (TRANSLATED)".strrev($this->adaptee->specificRequest()); 
    }
}

//strrev? -> 문자열 뒤집기

function clientCode(Target $target)
{
    echo $target->request();
}

echo "Client: I can work just fine with the Target objects:\n";
$target = new Target();
clientCode($target);
echo "\n\n";

//weird 기묘한, 이상한
$adaptee = new Adaptee();
echo "Client: The Adaptee class has a weird interface. See, I don't understand it:\n ";
echo "Adaptee: ".$adaptee->specificRequest();

echo "Client: But i can work with it via Adapter:\n";
$adapter = new Adapter($adaptee);
clientCode($adapter);

?>
```