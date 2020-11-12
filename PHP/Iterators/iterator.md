# Iterators

내부적으로 자체적으로 반복 될 수있는 개체에 대한 인터페이스..
자체적으로 반복 된다..? Key와 Value

```
Iterator extends Traversable {

    /* Methods */
    abstract public current ( ) : mixed
    abstract public key ( ) : scalar
    abstract public next ( ) : void
    abstract public rewind ( ) : void
    abstract public valid ( ) : bool

}

Iterator::current — Return the current element //현재위치 값
Iterator::key — Return the key of the current element //현재 키값
Iterator::next — Move forward to next element //다음위치
Iterator::rewind — Rewind the Iterator to the first element //처음 위치
Iterator::valid — Checks if current position is valid //현재 키값이 있는지 확인

<?php
class myIterator implements Iterator {
    private $position = 0;
    private $array = array(
        "firstelement",
        "secondelement",
        "lastelement",
    );  

    public function __construct() {
        $this->position = 0;
    }

    public function rewind() {
        var_dump(__METHOD__);
        $this->position = 0;
    }

    public function current() {
        var_dump(__METHOD__);
        return $this->array[$this->position];
    }

    public function key() {
        var_dump(__METHOD__);
        return $this->position;
    }

    public function next() {
        var_dump(__METHOD__);
        ++$this->position;
    }

    public function valid() {
        var_dump(__METHOD__);
        return isset($this->array[$this->position]);
    }
}

$it = new myIterator;

foreach($it as $key => $value) {
    var_dump($key, $value);
    echo "\n";
} //1


foreach($it as $key => $value) {

} //2


foreach($it as $value) {
    
} //3
?>

```

> Quiz 1. Output ?   
> Quiz 2. Output ?    
> Quiz 3. Output ?    
