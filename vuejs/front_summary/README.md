
> SPA
- Single Page Application
- 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 어플리케이션
- 서버로부터 최초에만 페이지를 다운로드하고, 이후에는 동적으로 DOM 구성
- 연속되는 페이지 간 사용자경험 향상

> SFC
- Single File Component
- Vue의 컴포넌트 기반 개발의 핵심특
- 하나의 컴포넌트는 `.vue` 확장자를 가진 하나의 파일 안에서 작성되는 코드의 결과물이다.
- 화면의 특정 영역에 대한 HTML, CSS, JavaScript 코드를 하나의 파일에서 관리한다.
- Vue 컴포넌트 === Vue 인스턴스 === .vue 파일

> Vue CLI Quick Start
```
$ npm install -g @vue/cli
$ vue --version
$ vue create my-first-app
```

> Vue Router
- 라우팅의 결정권을 가진 Vue.js에서 라우팅을 편리하게 할 수 있는 Tool 을 제공해주는 라이브러리
- CSR: 라우팅에 대한 결정권을 클라이언트가 가진다.
```
$ npm i vue-router
$ vue add router
```

> Vuex
- 상태관리 패턴 + 라이브러리 for vue.js
- 상태를 전역저장소로 관리할 수 있도록 지원하는 라이브러리
- Mutations: 실제 state 를 변경하는 유일한 방법
  - mutation 핸들러는 반드시 동기적이어야 한다.
  - 첫번째 인자로 항상 state를 받는다.
  - Actions 에서 `commit()` 메서드에 의해 호출된다.

- Actions: mutations 를 호출한다.
  - 비동기 작업이 포함될 수 있다.
  - context 객체 인자를 받는다.
  - context 객체를 통해 store/index.js 파일 내 모든 요소의 속성 접근 & 메서드 호출 가능
  - 단, (가능하지만) state를 직접 변경하지 않는다.
  - 컴포넌트에서 `dispatch()` 메서드에 의해 호출된다.

> Init project
```
// add vuex plugin in vue cli
// store 디렉토리 생성 및 index.js 생성
$ vue add vuex
```
  - `index.js`: Vuex core concepts 가 작성되는 곳

