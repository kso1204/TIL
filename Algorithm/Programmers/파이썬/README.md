# 신고 결과 받기

```

answer = [0] * len(id_list)

리스트를 0으로 초기화 하는 방법

reports = {x : 0 for x in id_list}

딕셔너리를 0으로 초기화 하는 방법

answer[id_list.index(r.split()[0])] += 1

++은 사용이 되지 않는 것 같았는데 += 1은 작동됨

r.split()[0]

스플릿하면서 특정 값 바로 사용하기

list.index로 해당 위치 찾기

```

