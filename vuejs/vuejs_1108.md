> Component

- 기본 HTML 엘리먼트를 확장해 재사용 가능한 코드를 캡슐화 하는데 도움을 준다.
- 즉, 유지보수 + 재사용성
- Vue 컴포넌트 === Vue 인스턴스



> SFC (Single Fiel Component)

- `.vue` 확장자를 가진 하나의 파일 안에서 작성되는 코드의 결과물
- Vue 컴포넌트 === Vue 인스턴스 === .vue 파일



> Vue CLI

- Vue.js 개발을 위한 표준 도구
- VUe 개발 생태계에서 표준 tool 기준을 목표로 함
- 확장 플러그인, GUI, ES2015 구성 요소 제공 등 `다양한 tool 제공`



> Node.js

- JS를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 JS 런타임 환경
- `Chrome V8` 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경 제공
  - JS를 SSR 아키텍쳐에서도 사용할 수 있게 되었다.



> NPM (Node Package Manage)

- Node.js의 기본 패키지 관리자
- Node.js 설치 시 함께 설치된다.



> Babel

- "JavaScript compiler"
- ECMAScript 2015+ 코드를 이전 버전으로 번역/변환해 주는 도구
- 원시코드(최신 버전)을 목적코드(구 버전)으로 옮기는 번역기



> Webpack

- "static module bundler"
- 모듈 간 의존성 문제를 해결하기 위한 도구

- 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함



> Bundler

- Bundling : 모듈 의존성 문제를 해결해주는 작업
- Webpack이 다양한 Bundler 중 하나
- 여러 모듈을 하나로 묶어주고, 묶인 파일은 하나로 합쳐짐



> package-lock.json

- node-modules에 설치되는 모듈과 관련된 모든 의존성 설정 및 관리
- 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장



> 컴포넌트 작성

- `Pass props` : 부모가 자식에게 데이터를 전달
- `Emit event` : 자식은 자신에게 일어난 이벤트를 메세지 형태로 부모에게 알림
  - 부모와 자식이 명확히 정의된 인터페이스를 통해 격리된 상태 유지
- `"props는 아래로, events는 위로"`
- 주의
  - 자식 컴포넌트의 템플릿에서 상위 데이터를 직접 참조할 수 없다.



> Props 이름 컨벤션

- 선언 시 `camelCase`
- HTML 템플릿에서 `kebab-case`



> 컴포넌트의 'data'는 반드시 함수여야 한다.

- 기본적으로 각 인스턴스는 모두 같은 data 객체를 공유한다.
- scope를 줘서 각 컴포넌트 마다 data를 활용하도록 한다.



> 숫자 전달

- `<comp some-prop="1"></comp>` : 문자열 "1" 전달
- `<comp :some-prep="1"></comp>` : 숫자 전달



> Emit event

- `$emit(eventName)`
- `v-on`을 사용해 자식 컴포넌트가 보낸 이벤트를 청취한다. (사용자 지정 이벤트)



> event 이름 컨벤션

- 컴포넌트 및 props와 달리, 이벤트는 자동 대소문자 변환을 제공하지 않음
- `v-on` 이벤트 리스너는 `v-on:myEvent`를 `v-on:myevent`로 변환
- 이벤트 이름은 항상 `kebab-case` 를 사용하는 것을 권장



> Vue Router

- 라우트(route)에 컴포넌트를 매핑한 후, 어떤 주소에서 렌더링할 지 알려줌
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공



> Vue Router - "router-link"

- `<router-link>`
- 사용자 네이게이션을 가능하게 하는 컴포넌트
- 목표 경로 : `to`
- HTML5 히스토리 모드에서 클릭 이벤트를 차단 -> 브라우저 re-load X
  - a 태그지만 우리가 알고 있는 GET 요청을 보내는 a태그와 조금 다르다.



> Vue ROuter - "router-view"

- `<router-view>`
- router-link를 클릭하면 해당 경로와 연결되어 있는 index.js에 정의한 컴포넌트가 위치



> History mode

- 브라우저의 히스토리는 남기지만 실제 페이지는 이동하지 않는 기능을 지원
- 페이지를 re-load하지 않고 URL을 탐색/변경할 수 있다.
  - SPA 단점 중 하나인 'URL이 변경되지 않는다' 는 것 해결



> Vue Router가 필요한 이유

1. SPA 등장 이전

- 서버가 모든 라우팅을 통제
- 요청 경로에 맞는 HTML 제공

2. SPA 등장 이후

- 서버는 index.html 하나만 제공
- 이후 모든 처리는 HTML 위에서 JS 코드를 활용해 진행
- 즉, 요청에 대한 처리를 더 이상 서버가 하지 않아도 된다.

