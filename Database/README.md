# DB에 락이 걸린다면?

1. https://dorumugs.tistory.com/entry/MSSQL-DB-Lock

# DB 속도가 느리면?

1. 인덱스가 걸려있지 않을 가능성이 있다.

2. Explain 해당 쿼리 조회해서 속도가 너무 오래 걸리거나 인덱스가 잡혀있지 않으면 해당 인덱스 설정

3. 그리고 그 인덱스를 운영 DB에도 적용

4. 서비스에서 해당 쿼리를 불러올 때 딜레이가 있는지 확인하기 위해 쿼리 호출 바로전에 Start Query Time을 설정해서 해당 서비스가 언제 끝나는지 조회한다.

# DB에서 중요한 것?

1. https://khj93.tistory.com/entry/Database-RDBMS%EC%99%80-NOSQL-%EC%B0%A8%EC%9D%B4%EC%A0%90

1. 비 관계형 데이터 베이스(Not Only Sql, NoSql) Vs 관계형 데이터 베이스(Relational DataBase Management System, RDBMS)

# 비 관계형 데이터 베이스

1. 키 - 밸류 : Redis, Memcached, Coherence

2. 열 지향 와이드 컬럼 스토어 : Cassandra, HBASE, Cloud Database

3. 문서형 : MongoDB, Couchbase, MarkLogic, DynamicDB MS-DocumentDB

4. 그래프형 : Neo4j
