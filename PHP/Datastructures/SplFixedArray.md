# SplFixedArray

배열의 크기가 클수록 읽고 쓰는 속도가 일반 배열보다 빠르고, 메모리 소모가 적은 장점이있다.

The SplFixedArray class provides the main functionalities of array. The main differences between a SplFixedArray and a normal PHP array is that the SplFixedArray is of fixed length and allows only integers within the range as indexes. The advantage is that it uses less memory than a standard array.

As the documentation says, SplFixedArray is meant to be *faster* than array. Do not blindly believe other people's benchmarks, and beextra careful with the user comments on php.net. For instance, nairbv's benchmark code is completely wrong. Among other errors, it intends to increase the size of the arrays, but always initialize a 20 elements SplFixedArray.

On a PHP 5.4 64 bits linux server, I found SplFixedArray to be always faster than array().
* small data (1,000):
    * write: SplFixedArray is 15 % faster
    * read:  SplFixedArray is  5 % faster
* larger data (512,000):
    * write: SplFixedArray is 33 % faster
    * read:  SplFixedArray is 10 % faster

SplFixedArray implements Iterator , ArrayAccess , Countable {

    /* Methods */
    public __construct ([ int $size = 0 ] )
    public count ( ) : int
    public current ( ) : mixed
    public static fromArray ( array $array [, bool $save_indexes = TRUE ] ) : SplFixedArray
    public getSize ( ) : int
    public key ( ) : int
    public next ( ) : void
    public offsetExists ( int $index ) : bool
    public offsetGet ( int $index ) : mixed
    public offsetSet ( int $index , mixed $newval ) : void
    public offsetUnset ( int $index ) : void
    public rewind ( ) : void
    public setSize ( int $size ) : bool
    public toArray ( ) : array
    public valid ( ) : bool
    public __wakeup ( ) : void
}

<?php
// Initialize the array with a fixed length
$array = new SplFixedArray(5);

$array[1] = 2;
$array[4] = "foo";

var_dump($array[0]); // NULL
var_dump($array[1]); // int(2)

var_dump($array["4"]); // string(3) "foo"

// Increase the size of the array to 10
$array->setSize(10);

$array[5] = "asdf";

// Shrink the array to a size of 2
$array->setSize(2);

// The following lines throw a RuntimeException: Index invalid or out of range

try {
    var_dump($array[-1]);
} catch(RuntimeException $re) {
    echo "RuntimeException: ".$re->getMessage()."\n";
}

try {
    var_dump($array[5]);
} catch(RuntimeException $re) {
    echo "RuntimeException: ".$re->getMessage()."\n";
}
?>

> Quiz. Output ? 