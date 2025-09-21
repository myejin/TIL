# 🔐 WHERE — Login Bypass

**목표:** 어드민 계정의 Username을 알고 있을 때 로그인 시도

<br />

## 🧪 실습

### 엉터리 Username & Password 시도:

"Invalid username or password." 메세지 → 시스템이 사용자 이름을 열거한다는 것을 의미할 수 있다.

<img width="280" height="330" alt="image" src="https://github.com/user-attachments/assets/6cb36e6b-d9f9-4f6b-bda8-208a4f423359" />

<br />

### Username에 `'` 입력

백엔드에서 앱 중단 → SQL 주입에 취약하다는 징후

<img width="220" height="100" alt="image" src="https://github.com/user-attachments/assets/be7b1cd2-d662-422f-9825-724263b26309" />

<br />


```sql
-- 쿼리 구문 오류 예시
SELECT firstname
FROM users
WHERE username=''' and password='xxx';
```

<br />

### 🏹 Username에 `admin'--` 입력

실제 Username = `admin` 인 정보가 없어서 발생한 오류일 수 있다. 

<img width="300" height="320" alt="image" src="https://github.com/user-attachments/assets/e9806bd7-03ad-49ef-a91e-f00cdd0f508c" />

<br />

### 🏹 Username에 `administrator'--` 입력

비밀번호와 관계 없이 Username 을 알아냈다면 관리자 계정으로 로그인 가능 🤨

<img width="300" height="320" alt="image" src="https://github.com/user-attachments/assets/b4726545-5376-4601-af42-950cf6421f7c" />

<br />

## ⚠️ 취약 원리

* 입력값이 SQL 쿼리에 그대로 삽입됨
* `'--`로 비밀번호 조건 무력화
* 입력 검증/파라미터화 없음

<br />

## 🛡️ 방어책

* 입력 검증(허용 목록) + 길이 제한
* 파라미터화 쿼리(Prepared Statements)
* 2단계 인증(2FA) 적용
* 보안 모니터링: 비정상 로그인 탐지/알림
