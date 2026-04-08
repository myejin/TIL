## AI 에이전트의 우아한 스트리밍 설계: Async Generator

### 0. Summary

```ts
export async function* query(
  params: QueryParams,
): AsyncGenerator<
  | StreamEvent
  | RequestStartEvent
  | Message
  | TombstoneMessage
  | ToolUseSummaryMessage,
  Terminal  // 반환값: 종료 이유
>
```

<br /><br />

### 1. 기존 방식의 한계 (EventEmitter & Callback)

연속적인 데이터(이벤트)를 처리할 때 전통적으로 사용하던 두 가지 방식은 흐름이 파편화된다는 단점이 있다.

**A. 이벤트 이미터(EventEmitter) 방식** <br />
라디오 주파수를 맞추고 방송을 기다리는 것과 같다.

```ts
const agent = new Agent();

// 각각의 채널(이름)에 콜백 함수를 달아줍니다.
agent.on("message", (msg) => console.log(msg));
agent.on("end", (reason) => console.log("종료:", reason));
agent.on("error", (err) => console.error("에러 발생:", err));

agent.start();
```

<br />

**B. 콜백 (Callback) 기반 방식** <br />
함수를 실행할 때, "성공하면 이거 해주고, 끝나면 저거 해줘" 하고 함수들을 바리바리 싸서 넘긴다.

```ts
query(
  params,
  (msg) => console.log(msg), // onEvent
  (reason) => console.log(reason), // onDone
  (err) => console.error(err), // onError
);
```

문제점: <br />
두 방식 모두 데이터 받는 곳, 끝나는 곳, 에러 나는 곳이 제각각 흩어진다. <br />
코드가 복잡해질수록 "에러 처리 핸들러를 깜빡하는" 버그가 생기기 쉽고, 실행 흐름을 추적하기 매우 까다롭다. <br />

<br /><br />

### 해결책: Async Generator로 흐름 통합하기

Async Generator는 흩어져 있던 ① 스트리밍(이벤트), ② 정상 종료, ③ 에러 처리를 우리가 가장 익숙한 "하나의 함수 흐름(for await...of + try-catch)" 안으로 깔끔하게 통합해 준다. <br />

- 일반 함수 (async function): 요리가 다 끝날 때까지 기다렸다가 한 번에 서빙. (한 번에 완성된 챗봇 답변)

- Async Generator (async function\*): 요리가 하나씩 완성될 때마다 바로바로 서빙(yield)하고, 다음 요리를 비동기로 준비(await).

<br /><br />

**소비자(Consumer) 측 코드의 변화:**

```ts
async function runAgent() {
  try {
    // ③ 에러 처리가 자연스럽게 통합됨
    const agentStream = query(params);

    // ① 스트리밍 이벤트를 for문으로 하나씩 받음
    for await (const event of agentStream) {
      console.log("방금 도착한 이벤트:", event);
    }

    // ② 정상 종료 (for문이 끝나면 자동으로 도달)
    console.log("에이전트 작업 무사히 완료!");
  } catch (error) {
    console.error("에이전트 실행 중 문제 발생:", error);
  }
}
```

결과적으로 "스트리밍 이벤트 → 정상 종료 → 에러 전파"라는 세 가지 흐름을 하나의 함수 시그니처로 깔끔하게 표현합니다. 복잡한 상태 머신을 다뤄야 하는 에이전틱 루프에 특히 잘 맞는 패턴입니다.

<br /><br />

### 3. 코드 시그니처 분석

복잡한 상태 머신을 다뤄야 하는 에이전트 루프에서 이 패턴이 어떻게 쓰이는지 시그니처를 뜯어보았다.

```ts
export async function* query(
  params: QueryParams,
): AsyncGenerator<
  /* 1. yield: 중간중간 계속 내보낼 이벤트들의 타입 */
  | StreamEvent
  | RequestStartEvent
  | Message
  | TombstoneMessage
  | ToolUseSummaryMessage,
  /* 2. return: 마지막에 딱 한 번 반환할 최종 상태 타입 */
  Terminal
>
```

yield (과정): AI 에이전트는 단순 텍스트뿐만 아니라 "나 지금 도구(검색 등) 사용할게!"(ToolUseSummaryMessage) 같은 중간 상태를 계속 방출해야 한다.

return (결과): 모든 작업이 완전히 끝났을 때, "왜 종료되었는지"(답변 완료, 토큰 초과 등)를 Terminal 타입으로 반환하여 최종 상태를 명확히 알린다.

"스트리밍 이벤트 → 정상 종료 → 에러 전파" 세 가지 복잡한 흐름을 단 하나의 함수 시그니처로 표현할 수 있다.

<br /><br />

### 참고 문서:

- [Claude Code 내부 아키텍처 분석](https://bits-bytes-nn.github.io/insights/agentic-ai/2026/03/31/claude-code-source-map-leak-analysis.html)
