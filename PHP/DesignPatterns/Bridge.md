# Bridge

Bridge 는 큰 클래스 또는 밀접하게 관련된 클래스 집합을 서로 독립적으로 개발할 수 있는 두 개의 개별 계층 (추상 및 구현)으로 분할 할 수있는 구조적 디자인 패턴입니다.

Abstraction? Implementation? Sound scary? Stay calm and let’s consider a simple example.

Say you have a geometric Shape class with a pair of subclasses: Circle and Square. You want to extend this class hierarchy to incorporate colors, so you plan to create Red and Blue shape subclasses. However, since you already have two subclasses, you’ll need to create four class combinations such as BlueCircle and RedSquare.

![problem-en (2)](https://user-images.githubusercontent.com/6989005/99202928-33d48000-27f4-11eb-86bc-6b0c894d4965.png)

클래스 조합을 할 때 기하급수적으로 늘어나는 경우의 수

![solution-en (1)](https://user-images.githubusercontent.com/6989005/99203297-7054ab80-27f5-11eb-8b6a-90a859383770.png)

독립적인 것을 그대로 유지한다.

Making even a simple change to a monolithic codebase is pretty hard because you must understand the entire thing very well. Making changes to smaller, well-defined modules is much easier.

//monolithic과 MSA.. 큰 규모를 잘게 쪼개는 형태

![bridge-2-en](https://user-images.githubusercontent.com/6989005/99203420-e0fbc800-27f5-11eb-9e32-74f6f7644d6a.png)

![20201116102509](https://user-images.githubusercontent.com/6989005/99203497-1e605580-27f6-11eb-90e8-8aff08a41bda.png)

```
<?php

// implements와 abstraction을 사용해서
// 클라이언트가 원하는 내용을 조합해서 사용할 수 있도록 구현하는 방법..?
// abstract와 extendedAbstract 그리고 implements 를 분류하고 이 내용으로 조합하는 방법으로 이해했다.
// 조금 더 어려운 상황을 봐야 이해하는 데 더 도움이 될 것 같다.

//hierarchies <- 계층

// Abstraction은 두 클래스 계층 의 "제어" 부분에 대한 인터페이스를 정의합니다 .
// Implementation 계층 의 개체에 대한 참조를 유지하고 모든 실제 작업을 이 개체에 위임합니다.

class Abstraction
{
    protected $implementation;

    public function __construct(Implementation $implementation)
    {
        $this->implementation = $implementation;
    }

    public function operation(): string
    {
        return "Abstraction: Base operation with:\n".
            $this->implementation->operationImplementation();
    }
}

/* 
implementation은 모든 implementation 클래스에 대한 인터페이스를 정의합니다.
그것은 Abstraction의 인터페이스와 일치 할 필요는 없습니다.
실제로 두 인터페이스는 완전히 다를 수 있습니다.
일반적으로 implementation 인터페이스 는 기본 작업 만 제공하는 반면, 
Abstraction는 이러한 기본 작업을 기반으로 더 높은 수준의 작업을 정의합니다 .  */

class ExtendedAbstraction extends Abstraction
{
    public function operation(): string
    {
        return "ExtendedAbstraction: Extended opertation with:\n".
            $this->implementation->operationImplementation();
    }
}

interface Implementation
{
    public function opertationImplementation(): string;
}

class ConcreteImplementationA implements Implementation
{
    public function operationImplementation(): string
    {
        return "ConcreteImplementationA: Here's the result on the platform A.";
    }

}

class ConcreteImplementationB implements Implementation
{
    public function operationImplementation(): string
    {
        return "ConcreteImplementationB: Here's the result on the platform B.\n";
    }
}

/**
 * Except for the initialization phase, where an Abstraction object gets linked
 * with a specific Implementation object, the client code should only depend on
 * the Abstraction class. This way the client code can support any abstraction-
 * implementation combination.
 */


function clientCode(Abstraction $abstraction)
{
    // ...

    echo $abstraction->operation();

    // ...
}

/**
 * The client code should be able to work with any pre-configured abstraction-
 * implementation combination.
 */

$implementation = new ConcreteImplementationA();
$abstraction = new Abstraction($implementation);
clientCode($abstraction);

echo "\n";

$implementation = new ConcreteImplementationB();
$abstraction = new ExtendedAbstraction($implementation);
clientCode($abstraction);




?>
```