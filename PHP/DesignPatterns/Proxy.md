# Proxy

출처 : https://refactoring.guru/design-patterns/proxy

프록시는 다른 객체에 대한 대체 또는 자리 표시자를 제공 할 수있는 구조 설계 패턴입니다. 
프록시는 원본 개체에 대한 액세스를 제어하므로 요청이 원본 개체에 전달되기 전이나 후에 작업을 수행 할 수 있습니다.


![20201116175847](https://user-images.githubusercontent.com/6989005/99235299-065df580-2839-11eb-8e55-9d4125209a08.png)


![20201116175915](https://user-images.githubusercontent.com/6989005/99235302-078f2280-2839-11eb-8ab6-bc6824385dd2.png)

```
<?php

//같은 request를 처리하는 데
//proxy 패턴은 request를 처리하기 전, 처리하고 나서의 상황에 대해 추가적인 제어가 가능하다.
//realSubject로 접근하나 proxy로 접근하나 결과값이 동일한데 why? Proxy 패턴을 써야할까?
//The most common applications of the Proxy pattern are lazy loading,
//caching, controlling the access, logging, etc.
//이런 부분을 어떻게 다루는지, 이 내용이 무엇인지에 대해서 정리해보면 좋을 것 같다. 


/**
 * The Subject interface declares common operations for both RealSubject and the
 * Proxy. As long as the client works with RealSubject using this interface,
 * you'll be able to pass it a proxy instead of a real subject.
 */

//realsubject 대신에 이용할 수 있는 proxy

interface Subject
{
    public function request(): void;
}

class RealSubject implements Subject
{
    public function request(): void
    {
        echo "RealSubject: Handling request.";
    }
}

class Proxy implements Subject
{
    private $realSubject;

      /**
     * The Proxy maintains a reference to an object of the RealSubject class. It
     * can be either lazy-loaded or passed to the Proxy by the client.
     */

     //lazy-loaded!! 
    

    public function __construct(RealSubject $realSubject)
    {
        $this->realSubject = $realSubject;
    }

    /**
     * The most common applications of the Proxy pattern are lazy loading,
     * caching, controlling the access, logging, etc. A Proxy can perform one of
     * these things and then, depending on the result, pass the execution to the
     * same method in a linked RealSubject object.
     */

     public function request(): void
     {
         if ($this->checkAccess()) {
             $this->realSubject->request();
             $this->logAccess();
         }
     }

     private function checkAccess(): bool
     {
         echo "proxy: checking access prior to firing a real request.";

         return true;
     }

     private function logAccess(): void
     {
         echo "proxy: loggin the time of request.\n";
     }
     


}

//In real life, however, clients mostly work with their real subjects
//directly. In this case, to implement the pattern more easily, you can extend
// your proxy from the real subject's class.

function clientCode(Subject $subject)
{
    $subject->request();
}

echo "Client: Executing the client code with a real subject";
$realSubject = new RealSubject();
clientCode($realSubject);

echo "Client: Executing the client code with a proxy";
$proxy = new Proxy($realSubject);
clientCode($proxy);

?>
```