# 개선? 업그레이드?

# DB::transaction

```

1:N 관계로 정의되어 있는 테이블에서 create하고 해당 data를 get 했더니 정상적으로 데이터를 가져오지 못했다.

refresh를 이용하거나 load를 이용하라는 내용들이 검색 됐는데, Laravel5.2 버전에서는 사용되지 않았다.

insert 하는 부분은 그대로 사용하고, get하는 부분을 transaction으로 감싸서 return 받으니 정상적으로 처리 되었다.

Transaction을 통해 새로운 인스턴스? DB?를 호출하게 되어서 그런 것 같다.

```

# Relation $model->relation() Vs $model->relation

```

$model->relation()은 Object를 반환하는 데 해당 오브젝트는 hasMany, BelongsTo 등 여러가지가 있지만 일단 Eloquent를 상속 받은 object를 반환한다.

$model->relation은 $model->relation()->first()와 같다.

```

# updateOrCreate

```

$model->relation()->updateOrCreate([조건],[내용]);

어느 데이터까지 일치하고 나머지 데이터가 달라지면 업데이트 하던지 생성할 것이냐..

조건에 일치하는데 내용이 다르면 update 하라는 내용

조건에 일치하지 않으면 내용을 create

```