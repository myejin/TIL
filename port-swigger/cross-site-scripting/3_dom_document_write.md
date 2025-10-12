## 🕵️‍♂️ 브라우저에서 DOM 에 JS 코드 추가하기

**목표:** document.write 사용하는 코드에 악성 검색어 추가 <br />
*(DOM 기반 XSS: 서버를 거치지 않고 클라이언트(브라우저) 쪽 JS 에 의해 DOM 에 삽입되어 실행되는 공격)*

<img width="500" height="220" alt="image" src="https://github.com/user-attachments/assets/fb91ccf0-b3ac-44f2-91b3-da1bd2f26a88" />

<br />

### 🧪 실습

**1️⃣ HTML Elements 에서 취약점 확인:**

<img width="550" height="150" alt="image" src="https://github.com/user-attachments/assets/b1bff5bc-eace-4af5-82cf-a03beedf7fbf" />

h1 태그에서 사용 확인 ☑️ <br />
<img width="363" height="61" alt="image" src="https://github.com/user-attachments/assets/233b8358-b929-4d72-bbe6-f57c36f1ee69" />

img 태그에서 사용 확인 ☑️ <br />
<img width="430" height="180" alt="image" src="https://github.com/user-attachments/assets/e25d1c3b-13d3-4ff9-ab4d-3e9c8d8c8963" />

<br />

**2️⃣ img 태그를 활용하여 alert() 코드 삽입:**

<img width="600" height="80" alt="image" src="https://github.com/user-attachments/assets/6219b126-0336-4c91-a309-e7d94656a417" />


**3️⃣ 결과 확인:<br />**

<img width="550" height="30" alt="image" src="https://github.com/user-attachments/assets/455f6b4f-8fb7-4650-a7c2-fce7538b89f7" />

<img width="350" height="145" alt="image" src="https://github.com/user-attachments/assets/c46c8b5b-e660-4181-a7d3-c9b125b23477" />


<br />
