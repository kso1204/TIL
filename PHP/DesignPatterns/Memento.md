# Memento

출처 : https://refactoring.guru/design-patterns/memento

Also known as: Snapshot

Memento 는 구현 세부 사항을 공개하지 않고 개체의 이전 상태를 저장하고 복원 할 수있는 동작 디자인 패턴입니다.

Memento 패턴은 상태 스냅 샷 생성을 해당 상태의 실제 소유자인 발신자 객체 에게 위임 합니다.
따라서 다른 개체가 "외부"에서 편집기의 상태를 복사하려고하는 대신
편집기 클래스 자체가 자체 상태에 대한 전체 액세스 권한이 있으므로 스냅 샷을 만들 수 있습니다.

![20201117150136](https://user-images.githubusercontent.com/6989005/99354174-47adde00-28e9-11eb-9db8-b7f416ebd822.png)


![20201117152444](https://user-images.githubusercontent.com/6989005/99354042-0a495080-28e9-11eb-835e-a776c51ef3da.png)


```
<?php

//php에서는 중요하지 않다고 설명한다.

// HP에서 Memento 패턴의 실제 적용 가능성은 매우 의심 스럽습니다.
// 대부분의 경우 직렬화를 사용하여 객체 상태의 복사본을 더 쉽게 만들 수 있습니다.
// 직렬화..?serialize?
// 정리하지 않는 게 좋았을 것 같다


class Originator
{
    private $state;

    public function __construct(string $state)
    {
        $this->state = $state;
        echo "Originator: My inital state {$this->state}";
    }

    public function doSomething(): void
    {
        echo "Originator: i'm doing smething";
        $this->state = $this->generateRandomString(30);
        echo "Originator: and my state has changed to:{$this->state}";
    }

    private function generateRandomString(int $length = 10): string
    {
        return substr(
            str_shuffle(
                str_repeat(
                    $x = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    ceil($length / strlen($x))
                )
            ),
            1,
            $length,
        );
    }

    public function save(): Memento
    {
        return new ConcreteMemento($this->state);
    }

    public function restore(Memento $memento): void
    {
        $this->state = $memento->getState();
        echo "Originator: My state has changed to: {$this->state}\n";
    }


}

interface Memento
{
    public function getName(): string;

    public function getDate(): string;
}

class ConcreteMemento implements Memento
{
    private $state;

    private $date;

    public function __construct(string $state)
    {
        $this->state = $state;
        $this->date = date('Y-m-d H:i:s');
    }

    /**
     * The Originator uses this method when restoring its state.
     */
    public function getState(): string
    {
        return $this->state;
    }

    /**
     * The rest of the methods are used by the Caretaker to display metadata.
     */
    public function getName(): string
    {
        return $this->date . " / (" . substr($this->state, 0, 9) . "...)";
    }

    public function getDate(): string
    {
        return $this->date;
    }
}

/**
 * The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
 * doesn't have access to the originator's state, stored inside the memento. It
 * works with all mementos via the base Memento interface.
 */
class Caretaker
{
    /**
     * @var Memento[]
     */
    private $mementos = [];

    /**
     * @var Originator
     */
    private $originator;

    public function __construct(Originator $originator)
    {
        $this->originator = $originator;
    }

    public function backup(): void
    {
        echo "\nCaretaker: Saving Originator's state...\n";
        $this->mementos[] = $this->originator->save();
    }

    public function undo(): void
    {
        if (!count($this->mementos)) {
            return;
        }
        $memento = array_pop($this->mementos);

        echo "Caretaker: Restoring state to: " . $memento->getName() . "\n";
        try {
            $this->originator->restore($memento);
        } catch (\Exception $e) {
            $this->undo();
        }
    }

    public function showHistory(): void
    {
        echo "Caretaker: Here's the list of mementos:\n";
        foreach ($this->mementos as $memento) {
            echo $memento->getName() . "\n";
        }
    }
}

/**
 * Client code.
 */
$originator = new Originator("Super-duper-super-puper-super.");
$caretaker = new Caretaker($originator);

$caretaker->backup();
$originator->doSomething();

$caretaker->backup();
$originator->doSomething();

$caretaker->backup();
$originator->doSomething();

echo "\n";
$caretaker->showHistory();

echo "\nClient: Now, let's rollback!\n\n";
$caretaker->undo();

echo "\nClient: Once more!\n\n";
$caretaker->undo();

?>
```

