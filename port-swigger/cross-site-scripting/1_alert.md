## 🕵️‍♂️ 기본 JS 코드 삽입하기

**목표:** 취약점이 있는 검색창을 사용하여 스크립트 추가 및 XSS 이해 <br />
*(XSS: 공격자가 악성 스크립트를 웹페이지에 주입하여 다른 사용자의 브라우저에서 실행되게 하는 공격)*

<img width="500" height="222" alt="image" src="https://github.com/user-attachments/assets/d12b35c6-d7af-4472-856e-61698fdcaf2a" />

<br />

### 🧪 실습

**1️⃣ 취약점 확인**

검색창에 h1 태그 추가: <br />
<img width="600" height="75" alt="image" src="https://github.com/user-attachments/assets/5590ea6a-eac5-43ab-9112-ee2624915653" />

텍스트 앞뒤로 줄내림 확인 ☑️ <br />
<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/80ccad68-302b-4006-84dd-775268d7507c" />


**2️⃣ script 태그로 alert() 코드 삽입:**

<img width="605" height="75" alt="image" src="https://github.com/user-attachments/assets/ed48fd4a-c777-49c3-8af7-24ca89d07b06" />

**3️⃣ 결과 확인:<br />**

<img width="350" height="120" alt="image" src="https://github.com/user-attachments/assets/e70924f5-a33e-402e-a67a-82d3d0f4e91f" />


<br />


### 🛡️ 방어책

**입력 검증**: <br />
허용한 문자만 받도록 화이트리스트 사용 

**출력 인코딩**: <br />
HTML, JS, CSS 등 문맥에 따라 적절하게 이스케이프 처리 

**CSP (Content Security Policy)**: <br />
브라우저가 외부 스크립트나 인라인 스크립트를 실행하지 못하도록 제한 

**DOM 기반 XSS 방지**: <br />
클라이언트에서 DOM 조작 시 innerHTML 대신 textContent, setAttribute 사용 

**라이브러리, 프레임워크 활용**: <br />
React, Vue 등 프레임워크는 기본적으로 HTML 이스케이프 처리  <br />
외부 라이브러리 사용 시 최신 보안 패치 적용 
