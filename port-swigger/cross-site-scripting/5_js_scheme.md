## 🕵️‍♂️ jQuery 취약점 이용하여 DOM 조작하기
**목표:** 백링크 href 속성에 javascript 스킴 사용하여 악성 코드 추가 <br />

<img width="600" height="80" alt="image" src="https://github.com/user-attachments/assets/fe1223b6-48cb-4f51-b6cc-a71e30b65150" />


<br />

### 🧪 실습

**1️⃣ HTML Elements 에서 취약점 확인:** <br />
`$()` 를 사용하는 것을 보아 jQuery 를 사용하고 있고, 쿼리파람을 파싱하여 href 속성에 주입하고 있다. <br />

<img width="350" height="37" alt="image" src="https://github.com/user-attachments/assets/c170d635-815b-42dd-99e6-d67fe5c9fe3c" />

<img width="1573" height="252" alt="image" src="https://github.com/user-attachments/assets/130b4dba-4822-42f6-8e84-9161d1753061" />

<br /><br />

**2️⃣ 쿼리파람에 javascript 코드 추가:** <br />

```
/feedback?returnPath=javascript:alert("hello")
```

<br /><br />

**3️⃣ 결과 확인:** <br />
다른 URL 을 방문하는 대신 href 속성에 포함된 js 를 직접 실행한다.

<img width="423" height="61" alt="image" src="https://github.com/user-attachments/assets/7460e1c3-c0dd-43a5-b7c5-ef863bd8a20d" />
<br />
<img width="432" height="156" alt="image" src="https://github.com/user-attachments/assets/c1ac0ac9-2e8b-4b92-b475-e4d3284cd36f" />

<br />
