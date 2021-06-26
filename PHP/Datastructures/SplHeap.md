# SplHeap

힙이란? https://blog.naver.com/dusdkfla/222132620820

힙은 힙 속성을 따르는 트리와 같은 구조입니다. 각 노드는 자식보다 크거나 같습니다.
```
abstract SplHeap implements Iterator , Countable {

    /* Methods */
    public __construct ( )
    abstract protected compare ( mixed $value1 , mixed $value2 ) : int
    public count ( ) : int
    public current ( ) : mixed
    public extract ( ) : mixed
    public insert ( mixed $value ) : void
    public isCorrupted ( ) : bool
    public isEmpty ( ) : bool
    public key ( ) : mixed
    public next ( ) : void
    public recoverFromCorruption ( ) : void
    public rewind ( ) : void
    public top ( ) : mixed
    public valid ( ) : bool

}

SplHeap::compare — Compare elements in order to place them correctly in the heap while sifting up //우선순위를 설정하는 compare Max와 Min은 부등호를 변경하면 된다.
SplHeap::__construct — Constructs a new empty heap
SplHeap::count — Counts the number of elements in the heap
SplHeap::current — Return current node pointed by the iterator
SplHeap::extract — Extracts a node from top of the heap and sift up
SplHeap::insert — Inserts an element in the heap by sifting it up
SplHeap::isCorrupted — Tells if the heap is in a corrupted state
SplHeap::isEmpty — Checks whether the heap is empty
SplHeap::key — Return current node index
SplHeap::next — Move to the next node
SplHeap::recoverFromCorruption — Recover from the corrupted state and allow further actions on the heap
SplHeap::rewind — Rewind iterator back to the start (no-op)
SplHeap::top — Peeks at the node from the top of the heap
SplHeap::valid — Check whether the heap contains more nodes


<?php
/**
* A class that extends SplHeap for showing rankings in the Belgian
* soccer tournament JupilerLeague
*/
class JupilerLeague extends SplHeap
{
    /**
     * We modify the abstract method compare so we can sort our
     * rankings using the values of a given array
     */
    public function compare($array1, $array2)
    {
        $values1 = array_values($array1);
        $values2 = array_values($array2);
        if ($values1[0] === $values2[0]) return 0;
        return $values1[0] < $values2[0] ? -1 : 1;
    }
}

// Let's populate our heap here (data of 2009)
$heap = new JupilerLeague();
$heap->insert(array ('AA Gent' => 15));
$heap->insert(array ('Anderlecht' => 20));
$heap->insert(array ('Cercle Brugge' => 11));
$heap->insert(array ('Charleroi' => 12));
$heap->insert(array ('Club Brugge' => 21));
$heap->insert(array ('G. Beerschot' => 15));
$heap->insert(array ('Kortrijk' => 10));
$heap->insert(array ('KV Mechelen' => 18));
$heap->insert(array ('Lokeren' => 10));
$heap->insert(array ('Moeskroen' => 7));
$heap->insert(array ('Racing Genk' => 11));
$heap->insert(array ('Roeselare' => 6));
$heap->insert(array ('Standard' => 20));
$heap->insert(array ('STVV' => 17));
$heap->insert(array ('Westerlo' => 10));
$heap->insert(array ('Zulte Waregem' => 15));

// For displaying the ranking we move up to the first node
$heap->top();

// Then we iterate through each node for displaying the result
while ($heap->valid()) {
  list ($team, $score) = each ($heap->current()); //php에서 두 개의 변수에 동시에 값을 넣는 방법이라고 해야하나..?
  echo $team . ': ' . $score . PHP_EOL;
  $heap->next();
}
?>

This results in the following output:
Club Brugge: 21
Anderlecht: 20
Standard: 20
KV Mechelen: 18
STVV: 17
Zulte Waregem: 15
AA Gent: 15
G. Beerschot: 15
Charleroi: 12
Racing Genk: 11
Cercle Brugge: 11
Kortrijk: 10
Lokeren: 10
Westerlo: 10
Moeskroen: 7
Roeselare: 6

?>

> Splheap에서 우선순위힙, 맥스힙 정렬을 compare로 정의해서 사용한다.
> 우선순위 힙과 splheap의 차이는.. 우선 값(array형식 or 그냥 값) 으로 넣는지 키, 값형태로 넣는지에 차이가 있는 것 같고.. 아닌가?   
> 우선순위 힙에서 data와 priority 형태로 보여주려면 $heap->setExtractFlags(JupilerLeague::EXTR_BOTH); 이 부분을 설정해야 한다.   
> 저 flag를 설정하지 않을 경우에는 data만 보여줌


