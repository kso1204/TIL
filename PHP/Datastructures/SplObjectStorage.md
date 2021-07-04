# SplObjectStorage

SplObjectStorage 클래스는 객체에서 데이터로의 맵을 제공하거나 데이터를 무시하여 객체 세트를 제공합니다. 이 이중 목적은 개체를 고유하게 식별해야하는 많은 경우에 유용 할 수 있습니다.

프로그램을 작성하다보면 배열안에 객체가 들어있고, 그 객체안에 다시 배열이 들어있는 경우가 있는데..
이건 그 객체를 담는 일반적인 배열보다 기능을 가지고 있는 배열이라고 생각하면 될까?;

SplObjectStorage implements Countable , Iterator , Serializable , ArrayAccess {

    /* Methods */
    public addAll ( SplObjectStorage $storage ) : void
    public attach ( object $object [, mixed $data = NULL ] ) : void
    public contains ( object $object ) : bool
    public count ( ) : int
    public current ( ) : object
    public detach ( object $object ) : void
    public getHash ( object $object ) : string
    public getInfo ( ) : mixed
    public key ( ) : int
    public next ( ) : void
    public offsetExists ( object $object ) : bool
    public offsetGet ( object $object ) : mixed
    public offsetSet ( object $object [, mixed $data = NULL ] ) : void
    public offsetUnset ( object $object ) : void
    public removeAll ( SplObjectStorage $storage ) : void
    public removeAllExcept ( SplObjectStorage $storage ) : void
    public rewind ( ) : void
    public serialize ( ) : string
    public setInfo ( mixed $data ) : void
    public unserialize ( string $serialized ) : void
    public valid ( ) : bool

}
```
<?php
// As an object set
$s = new SplObjectStorage();

$o1 = new StdClass;
$o2 = new StdClass;
$o3 = new StdClass;

$s->attach($o1); //객체저장소에 객체를 추가하기
$s->attach($o2);

var_dump($s->contains($o1)); //객체저장소에 객체가 있는지 확인하기
var_dump($s->contains($o2));
var_dump($s->contains($o3));

$s->detach($o2);

var_dump($s->contains($o1));
var_dump($s->contains($o2));
var_dump($s->contains($o3));
?>

Stdclass는 빈 클래스보다 빈 객체..? 라고 설명하는 것 같다. json_decode를 했을 때 나오는 형태이기도 하고, stdClass형태면 각 프로퍼티? 데이터?에 애로우 형태로 접근할 수 있다.



```

> Quiz. Output ?    
```
<?php
// As a map from objects to data
$s = new SplObjectStorage();

$o1 = new StdClass;
$o2 = new StdClass;
$o3 = new StdClass;

$s[$o1] = "data for object 1";
$s[$o2] = array(1,2,3);

if (isset($s[$o2])) {
    var_dump($s[$o2]);
}
?>
```

> Quiz. Output ?

