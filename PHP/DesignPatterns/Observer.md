# Observer

출처 : https://refactoring.guru/design-patterns/observer

Also known as: Event-Subscriber, Listener

Observer 는 관찰중인 객체에 발생하는 이벤트에 대해 여러 객체에 알리는 구독 메커니즘을 정의 할 수있는 동작 디자인 패턴입니다.

흥미로운 상태를 가진 객체를 종종 subject 라고 부르지 만, 상태 변경에 대해 다른 객체에게 알릴 것이므로이를 publisher 라고합니다 . 게시자의 상태 변경을 추적하려는 다른 모든 개체를 구독자 라고 합니다.


![20201117153617](https://user-images.githubusercontent.com/6989005/99354908-a7f14f80-28ea-11eb-9295-5949a3721fea.png)

비즈니스 로직을 살펴보고 이를 두 부분으로 나누십시오.
다른 코드와 독립적인 핵심 기능이 게시자 역할을합니다.
나머지는 구독자 클래스 집합으로 바뀝니다.

PHP에는 Observer 패턴 구현을 나머지 PHP 코드와 호환되도록 만드는 데 사용할 수있는 여러 내장 인터페이스
 ( SplSubject , SplObserver )가 있습니다.

 ```
 <?php

//attach를 통해 ConcreteObject 1 or 2의 결과가 보여지는 패턴이다.
//attach -> 구독자 등록
//datach -> 구독자 삭제
//notify -> 구독자에게 발행 
//여기서는 state를 통해 특정 형태의 구독자에 대한 랜덤 제한을 걸고있다..?


 
class Subject implements \SplSubject
{
    /**
     * @var int For the sake of simplicity, the Subject's state, essential to
     * all subscribers, is stored in this variable.
     */
    public $state;

    /**
     * @var \SplObjectStorage List of subscribers. In real life, the list of
     * subscribers can be stored more comprehensively (categorized by event
     * type, etc.).
     */
    private $observers;

    public function __construct()
    {
        $this->observers = new \SplObjectStorage();
    }

    /**
     * The subscription management methods.
     */
    public function attach(\SplObserver $observer): void
    {
        echo "Subject: Attached an observer.\n";
        $this->observers->attach($observer);
    }

    public function detach(\SplObserver $observer): void
    {
        $this->observers->detach($observer);
        echo "Subject: Detached an observer.\n";
    }

    /**
     * Trigger an update in each subscriber.
     */
    public function notify(): void
    {
        echo "Subject: Notifying observers...\n";
        foreach ($this->observers as $observer) {
            $observer->update($this);
        }
    }

    /**
     * Usually, the subscription logic is only a fraction of what a Subject can
     * really do. Subjects commonly hold some important business logic, that
     * triggers a notification method whenever something important is about to
     * happen (or after it).
     */
    public function someBusinessLogic(): void
    {
        echo "\nSubject: I'm doing something important.\n";
        $this->state = rand(0, 10);

        echo "Subject: My state has just changed to: {$this->state}\n";
        $this->notify();
    }
}

/**
 * Concrete Observers react to the updates issued by the Subject they had been
 * attached to.
 */
class ConcreteObserverA implements \SplObserver
{
    public function update(\SplSubject $subject): void
    {
        if ($subject->state < 3) {
            echo "ConcreteObserverA: Reacted to the event.\n";
        }
    }
}

class ConcreteObserverB implements \SplObserver
{
    public function update(\SplSubject $subject): void
    {
        if ($subject->state == 0 || $subject->state >= 2) {
            echo "ConcreteObserverB: Reacted to the event.\n";
        }
    }
}

/**
 * The client code.
 */

$subject = new Subject();

$o1 = new ConcreteObserverA();
$subject->attach($o1);

$o2 = new ConcreteObserverB();
$subject->attach($o2);

$subject->someBusinessLogic();
$subject->someBusinessLogic();

$subject->detach($o2);

$subject->someBusinessLogic();
?>
```