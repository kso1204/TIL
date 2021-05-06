# 개선? 업그레이드?

# DB::transaction

```

1:N 관계로 정의되어 있는 테이블에서 create하고 해당 data를 get 했더니 정상적으로 데이터를 가져오지 못했다.

refresh를 이용하거나 load를 이용하라는 내용들이 검색 됐는데, Laravel5.2 버전에서는 사용되지 않았다.

insert 하는 부분은 그대로 사용하고, get하는 부분을 transaction으로 감싸서 return 받으니 정상적으로 처리 되었다.

Transaction을 통해 새로운 인스턴스? DB?를 호출하게 되어서 그런 것 같다.

```

