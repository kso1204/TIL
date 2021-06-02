# Relation

# has는 상대방꺼 내꺼

# belongs은 내꺼 상대방꺼 그래서 결국 순서가 동일하다.

# hasOne

```

class User {

    public function phone() {
        
        return $this->hasOne(Phone::class);

    }

}

Eloquent는 모델 이름을 기반으로 relationship의 외래 키(foreign key)를 결정합니다

지금 저렇게만 설정하면 Phone모델이 User_id를 가지고 있을거라고 추측한다.

근데 phone 모델이 uidx를 가지고 있다면??


class User {
    public function phone() {
        return $this->hasOne(Phone::class, 'uidx');
    }
}

Eloquent는 또한 외래 키가 부모의 id 컬럼(또는 사용자가 정의한 $primaryKey)에 상응하는 값을 가지고 있다고 추정합니다.

즉 phone레코드의 user_id 컬럼에서 사용자 id 컬럼의 이름을 찾는다. 다른 이름을 사용할것이라면

ex)uidx

class User {
    public function phone() {
        return $this->hasOne(Phone::class, 'uidx'//phone꺼, 'uidx' //user꺼);
    }
}


```

# belongsTo


```

User Class

role_id 유저꺼

public function role()
{
    return $this->belongsTo(Role::class,'role_id');
}

```

```

class Phone {

    public function user()
    {
        return $this->belongsTo(User::class);
    }
}

위 예에서 Eloquent는 Phone 모델의 user_id와 User 모델의 id를 비교해볼 것입니다.

Eloquent는 relationship 메소드의 이름을 검사하고 메소드 이름에 _id를 붙여서 외래 키의 기본 이름으로 결정합니다. 

만약 phone 모델의 외래키가 User_id가 아니라면?

커스텀 키 이름을 두번째 인자로 belongsTo에 전달하면 됩니다.

class Phone {
    public function user() 
    {
        return $this->belongsTo(User::class, 'uidx' //phone꺼);
    }
}


부모 모델이 id를 프라이머리 키로 사용하지 않거나 자식 모델을 다른 컬럼에 조인시키고 싶다면 부모 테이블의 커스텀 키를 지정하는 세번째 인자를 belongsTo 메소드로 전달하면 됩니다.

class Phone {
    public function user() 
    {
        return $this->belongsTo(User::class, 'uidx', 'uidx'//user의 primarykey);
    }
}

```

# 1:N 관계

일대다 relationship은 하나의 모델이 다른 모델의 어떤 부분이라도 소유할 경우의 relationship을 정의하는데 사용됩니다.

예를 들어, 한 블로그 게시물이 댓글을 무제한으로 가질 수 있습니다.

다른 모든 Eloquent relationship들과 같이, 일대다 relationship들은 Eloquent 모델에 함수를 통해서 정의됩니다.

```

class Post {
    public function comments()
    {
        return $this->hasMay(Comment::class);
    }
}

앞서 언급했듯이 Eloquent는 Comment 모델에 적절한 외래 키를 자동으로 결정합니다.

Eloquent는 관례적으로 소유하는 모델의 "snake case" 이름에 _id를 붙일 것입니다. 

따라서 이 예에서 Eloqent는 Comment 모델의 외래 키가 post_id일 것이라고 추정합니다.

comments의 외래키 pidx

class Post {
    public function commets()
    {
        return $this->hasMany(Comment::class, 'pidx');
    }
}

Post의 primarykey pidx;

class Post {
    public function comments()
    {
        return $this->hasMany(Comment::class, 'pidx', 'pidx');
    }
}

```

# N:N 관계

```

다 대다 관계는 hasOne 및 hasMany 관계보다 약간 더 복잡합니다. 이러한 관계의 예는 많은 역할을 가진 유저이며, 다른 유저도 해당 역할을 공유합니다.

예를 들어 많은 유저가 "관리자" 역할을 할 수 있습니다.

이 관계를 정의하려면 users, roles 및 role_user의 세 가지 데이터베이스 테이블이 필요합니다. 

role_user 테이블은 관련 모델 이름의 알파벳 순서에서 파생되며 user_id 및 role_id 열을 포함합니다.

users

id - integer
name - string

roles

id - integer
name - string

role_user

user_id - integer
role_id - integer


class User {

    public function roles()
    {
        return $this->belongsToMany(Role::class);
    }

}

Eloquent는 relationship-관계의 조인(join) 테이블의 테이블 명을 결정하기 위해 관련된 두 모델 이름을 알파벳 순으로 합칠 것입니다.

(user 와 role 일 경우에 role_user 로 이름을 추정합니다) 하지만 이러한 관례는 재지정 할 수 있습니다. belongsToMany 메소드로 두번째 인자를 전달하면 됩니다.

return $this->belongsToMany('App\Models\Role', 'role_user');


세번째 인자는 관계를 정의하는 모델의 외래 키 이름이고 네번째 인자는 join 하는 모델의 외래 키 이름입니다.

return $this->belongsToMany('App\Models\Role', 'role_user', 'user_id', 'role_id');

근데 이 방법은 user가 user이기도 하면서 관리자이기도 한 것 아닌가?

```