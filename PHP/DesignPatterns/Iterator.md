# Iterator

출처 : https://refactoring.guru/design-patterns/iterator

Iterator 는 기본 표현 (목록, 스택, 트리 등)을 노출하지 않고도 컬렉션의 요소를 탐색 할 수있는 동작 디자인 패턴입니다.

컬렉션은 프로그래밍에서 가장 많이 사용되는 데이터 유형 중 하나입니다. 
그럼에도 불구하고 컬렉션은 개체 그룹의 컨테이너 일뿐입니다.

DFS와 BFS

![20201117133638](https://user-images.githubusercontent.com/6989005/99347247-f2b69b80-28d9-11eb-9832-852905622887.png)

![20201117133744](https://user-images.githubusercontent.com/6989005/99347286-17127800-28da-11eb-95b9-00257ec24668.png)

```
<?php

//\Iterator를 선언하지 않아서 그런가.. 출력이 안된다
//SPL에서 다뤘던 iterator를 implements해서 사용하는 패턴
//그 구조랑 크게 다른 건 없는 것 같다.
//iterator를 사용해서 순회하는 방법을 알고 있으면 됐다.


class AlphabeticalOrderIterator implements \Iterator
{
    private $collection;

    private $position = 0;

    private $reverse = false;

    public function __construct($collection, $reverse = false)
    {
        $this->collection = $collection;
        $this->reverse = $reverse;
    }

    public function rewind()
    {
        $this->position = $this->reverse ? 
            count($this->collection->getItems()) -1 : 0;
    }

    public function current()
    {
        return $this->colleciton->getItems()[$this->position];
    }

    public function key()
    {
        return $this->position;
    }

    public function next()
    {
        $this->position = $this->position + ($this->reverse ? -1 : 1);
    }

    public function vaild()
    {
        return isset($this->collection->getItems()[$this->position]);
    }

}


class WordsCollection implements \IteratorAggregate
{
    private $items = [];

    public function getItems()
    {
        return $this->items;
    }

    public function addItem($item)
    {
        $this->items[] = $item;
    }

    public function getIterator(): Iterator
    {
        return new AlphabeticalOrderIterator($this);
    }

    public function getReverseIterator(): Iterator
    {
        return new AlphabeticalOrderIterator($this, true);
    }
}


$collection = new WordsCollection();
$collection->addItem("First");
$collection->addItem("Second");
$collection->addItem("Third");

echo "Straight traversal";
foreach ($collection->getIterator() as $item) {
    echo $item;
}


echo "Reverse traversal";
foreach ($collection->getReverseIterator() as $item) {
    echo $item;
}
?>
```