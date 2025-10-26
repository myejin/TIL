## 🕵️‍♂️ 브라우저에서 DOM 에 JS 코드 추가하기

**목표:** innerHTML 사용하여 코드에 악성 검색어 추가 <br />

<img width="500" height="220" alt="image" src="https://github.com/user-attachments/assets/fb91ccf0-b3ac-44f2-91b3-da1bd2f26a88" />

<br />

### 🧪 실습

**1️⃣ HTML Elements 에서 취약점 확인:** <br />

<img width="550" height="150" alt="image" src="https://github.com/user-attachments/assets/b1bff5bc-eace-4af5-82cf-a03beedf7fbf" />

<img width="628" height="199" alt="image" src="https://github.com/user-attachments/assets/a9345a58-5d6b-4681-9924-0aedf20145a2" />

<br /><br />

**2️⃣ script 태그 동작 확인:** <br />
script 는 HTML 을 파싱해서 DOM 노드로 변환할 때 즉시 실행되지 않는다.  

<img width="620" height="205" alt="image" src="https://github.com/user-attachments/assets/f7e04697-00b7-49d1-b6f9-443b46b08aaf" />

<br /><br />

**3️⃣ img 태그로 alert 실행 확인:** <br />
이벤트 핸들러 속성은 파싱된 직후 실행될 수 있다.
  
<img width="600" height="80" alt="image" src="https://github.com/user-attachments/assets/159b4572-dd6e-4cfe-95b6-ef7c2df98e56" />

<img width="300" height="100" alt="image" src="https://github.com/user-attachments/assets/e04b7e29-d6a0-4837-8cd3-79d966b20135" />

<br />
