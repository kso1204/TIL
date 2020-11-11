# SplDoublyLinkedList

* 이중 연결 목록 (DLL)은 양방향으로 서로 연결된 노드 목록입니다. 반복자의 작업, 양쪽 끝에 대한 액세스, 노드 추가 또는 제거는 기본 구조가 DLL 인 경우 O (1)의 비용이 듭니다. 따라서 스택 및 큐에 대한 적절한 구현을 제공합니다.

> [SplStack](#SplStack)   
> [SplQueue](#SplQueue)  

```
SplDoublyLinkedList implements Iterator , ArrayAccess , Countable , Serializable {

    /* Constants */
    const int IT_MODE_LIFO = 2 ;
    const int IT_MODE_FIFO = 0 ;
    const int IT_MODE_DELETE = 1 ;
    const int IT_MODE_KEEP = 0 ;

    /* Methods */
    public __construct ( )
    public add ( mixed $index , mixed $newval ) : void
    public bottom ( ) : mixed
    public count ( ) : int
    public current ( ) : mixed
    public getIteratorMode ( ) : int
    public isEmpty ( ) : bool
    public key ( ) : mixed
    public next ( ) : void
    public offsetExists ( mixed $index ) : bool
    public offsetGet ( mixed $index ) : mixed
    public offsetSet ( mixed $index , mixed $newval ) : void
    public offsetUnset ( mixed $index ) : void
    public pop ( ) : mixed
    public prev ( ) : void
    public push ( mixed $value ) : void
    public rewind ( ) : void
    public serialize ( ) : string
    public setIteratorMode ( int $mode ) : void
    public shift ( ) : mixed
    public top ( ) : mixed
    public unserialize ( string $serialized ) : void
    public unshift ( mixed $value ) : void
    public valid ( ) : bool
}
```

* SplDoublyLinkedList::IT_MODE_LIFO
* The list will be iterated in a last in, first out order, like a stack. //점점 쌓이는 구조

* SplDoublyLinkedList::IT_MODE_FIFO
* The list will be iterated in a first in, first out order, like a queue. //선입선출

```
SplDoublyLinkedList::add — Add/insert a new value at the specified index (지정한 인덱스에 새로운 값 삽입)
SplDoublyLinkedList::bottom — Peeks at the node from the beginning of the doubly linked list (시작 값)
SplDoublyLinkedList::__construct — Constructs a new doubly linked list 
SplDoublyLinkedList::count — Counts the number of elements in the doubly linked list
SplDoublyLinkedList::current — Return current array entry (현재위치의 값 반환)
SplDoublyLinkedList::getIteratorMode — Returns the mode of iteration (현재 LIFO인지 FIFO인지)
SplDoublyLinkedList::isEmpty — Checks whether the doubly linked list is empty
SplDoublyLinkedList::key — Return current node index (현재위치의 인덱스 반환)
SplDoublyLinkedList::next — Move to next entry (다음으로 이동)
SplDoublyLinkedList::offsetExists — Returns whether the requested $index exists
SplDoublyLinkedList::offsetGet — Returns the value at the specified $index
SplDoublyLinkedList::offsetSet — Sets the value at the specified $index to $newval
SplDoublyLinkedList::offsetUnset — Unsets the value at the specified $index
SplDoublyLinkedList::pop — Pops a node from the end of the doubly linked list(마지막 값 삭제)
SplDoublyLinkedList::prev — Move to previous entry (이전으로 이동)
SplDoublyLinkedList::push — Pushes an element at the end of the doubly linked list (마지막에 값 추가)
SplDoublyLinkedList::rewind — Rewind iterator back to the start (위치를 맨 처음으로 되감기?)
SplDoublyLinkedList::serialize — Serializes the storage
SplDoublyLinkedList::setIteratorMode — Sets the mode of iteration
SplDoublyLinkedList::shift — Shifts a node from the beginning of the doubly linked list
SplDoublyLinkedList::top — Peeks at the node from the end of the doubly linked list (마지막 값)
SplDoublyLinkedList::unserialize — Unserializes the storage
SplDoublyLinkedList::unshift — Prepends the doubly linked list with an element
SplDoublyLinkedList::valid — Check whether the doubly linked list contains more nodes

$a = new SplDoublyLinkedList;
$arr=[1,2,3,4,5,6,7,8,9];
for($i=0;$i<count($arr);$i++){
    $a->add($i,$arr[$i]);
}

$a->push(11); //push method
$a->add(10,12); //add method must with index
$a->shift(); //remove array first value
$a->unshift(1); //add first value

$a->rewind(); //initial from first

echo "SplDoublyLinkedList array last/top value " .  $a->top() ." \n";
echo "SplDoublyLinkedList array count value " .  $a->count() ." \n";
echo "SplDoublyLinkedList array first/top value " . $a->bottom() . " \n\n";

while($a->valid()){ //check with valid method
    echo 'key ', $a->key(), ' value ', $a->current(),"\n"; //key and current method use here
    $a->next(); //next method use here
}

$a->pop(); //remove array last value
print_r($a);
$s=$a->serialize();
echo $s;

//Output
SplDoublyLinkedList array last/top value 12
SplDoublyLinkedList array count value 11
SplDoublyLinkedList array first/top value 1

key 0 value 1
key 1 value 2
key 2 value 3
key 3 value 4
key 4 value 5
key 5 value 6
key 6 value 7
key 7 value 8
key 8 value 9
key 9 value 11
key 10 value 12
SplDoublyLinkedList Object
(
    [flags:SplDoublyLinkedList:private] => 0
    [dllist:SplDoublyLinkedList:private] => Array
        (
            [0] => 1
            [1] => 2
            [2] => 3
            [3] => 4
            [4] => 5
            [5] => 6
            [6] => 7
            [7] => 8
            [8] => 9
            [9] => 11
        )

)
i:0;:i:1;:i:2;:i:3;:i:4;:i:5;:i:6;:i:7;:i:8;:i:9;:i:11;
```

# SplStack

> the SplStack is  simply a SplDoublyLinkedList with  an iteration mode IT_MODE_LIFO and IT_MODE_KEEP

# SplQueue

> 이중연결리스트에서 FIFO방식으로 하더라도 기존 queue와 다르다는 것을 확인할 수 있다.   
> 모드를 FIFO로 하면 queue와 같은 방식으로 탐색은 가능하지만 push와 pop이 하는일은 queue와 다르다.

```
SplQueue extends SplDoublyLinkedList implements Iterator , ArrayAccess , Countable {

/* Methods */

__construct ( )
dequeue ( ) : mixed
enqueue ( mixed $value ) : void
setIteratorMode ( int $mode ) : void

/* Inherited methods */
public SplDoublyLinkedList::add ( mixed $index , mixed $newval ) : void
...

}

SplQueue::dequeue — Dequeues a node from the queue
SplQueue::enqueue — Adds an element to the queue


 
$queue = new SplQueue();
$queue->enqueue('A');
$queue->enqueue('B');
$queue->enqueue('C');

$queue->rewind();
while($queue->valid()){
    echo $queue->current(),"\n";
    $queue->next();
}

print_r($queue);
$queue->dequeue(); //remove first one
print_r($queue);


$queue->push(1);
$queue->push(2);
$queue->push(3);
$queue->pop();

print_r($queue); //Queue에서 Push로 삽입했을 때와 enqueue로 삽입했을 때, pop과 dequeue의 차이점을 이해하는가?

```

> Quiz. Output ? 


