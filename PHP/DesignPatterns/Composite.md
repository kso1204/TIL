# Composite

출처 : https://refactoring.guru/design-patterns/composite

Composite 는 개체를 트리 구조로 구성한 다음 개별 개체 인 것처럼 이러한 구조로 작업 할 수있는 구조적 디자인 패턴입니다.

복합 패턴을 사용하는 것은 앱의 핵심 모델을 트리로 나타낼 수있는 경우에만 의미가 있습니다.

예를 들어, 두 가지 유형의 객체가 있다고 가정합니다. Products및 Boxes. A Box에는 여러 개의 Products작은 Boxes. 이 작은 것들은 Boxes또한 일부 Products또는 더 작은 것을 보유 할 수 있습니다 Boxes.

이러한 클래스를 사용하는 주문 시스템을 만들기로 결정했다고 가정 해 보겠습니다. 주문에는 포장이없는 단순한 제품과 제품으로 채워진 상자 및 기타 상자가 포함될 수 있습니다. 그러한 주문의 총 가격을 어떻게 결정 하시겠습니까?

![20201116105039](https://user-images.githubusercontent.com/6989005/99204619-97ad7780-27f9-11eb-80b0-4d9db97e2ea2.png)

![20201116105137](https://user-images.githubusercontent.com/6989005/99204662-b6ac0980-27f9-11eb-8e91-6f8b01a72374.png)

```
<?php

//clientCode와 clientCode2를 통해서
//기존에 사용하고 있던 트리구조에 새로운 component를 등록시킬 때
//다른 클래스를 생성하지 않고도 손쉽게 트리 구조로 추가되는 것을 알 수 있다.
//Component 자체의 isComposite는 false이기 때문에, 이 구조상에서 leaf는 부모가 될 수 없다.


abstract class Component
{
    protected $parent;

    public function setParent(Component $parent)
    {
        $this->parent = $parent;
    }

    public function getParent(): Component
    {
        return $this->parent;
    }

    public function add(Component $component): void {}
    public function remove(Component $component): void {}

    /**
     * You can provide a method that lets the client code figure out whether a
     * component can bear children. 자식을 가질 수 있는지 확인? bear..
     */

     public function isComposite(): bool
     {
         return false;
     }

     abstract public function operation(): string;

}

class Leaf extends Component
{
    public function operation(): string
    {
        return "Leaf";
    }
}

class Composite extends Component
{
    protected $children;

    public function __construct()
    {
        $this->children = new \SplObjectStorage();
    }

    public function add(Component $component): void
    {
        $this->children->attach($component);
        $component->setParent($this);
    }

    public function remove(Component $component): void
    {
        $this->children->detach($component);
        $component->setParent(null);
    }

    public function isComposite(): bool
    {
        return true;
    }

    //재귀적으로 순환하면서 그들 자식의 결과를 더한다.
    public function operation(): string
    {
        $results = [];
        foreach ($this->children as $child) {
            $results[] = $child->operation();
        }
        
        return "Branch (".implode("+", $results).")";
    }
}

function clientCode(Component $component)
{
    echo "RESULT : ". $component->operation();
}


$simple = new Leaf();
echo "Client: I've got a simple component";
clientCode($simple);

$tree = new Composite();
$branch1 = new Composite();
$branch1->add(new Leaf());
$branch1->add(new Leaf());
$branch2 = new Composite();
$branch2->add(new Leaf());
$tree->add($branch1);
$tree->add($branch2);

echo "Client: I've got a composite tree";
clientCode($tree);

function clientCode2(Component $component1, Component $component2)
{
    if ($component1->isComposite()) {
        $component1->add($component2);
    }
    echo "RESULT: ".$component1->operation();
}

echo "Client: I don't need to check the components classes even when managing the tree:\n";
clientCode2($tree, $simple);

?>
```