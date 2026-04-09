## AI Agent의 상태 관리: Continue Site Pattern
Anthropic의 Claude Code 분석 사례를 통해 배운 에이전틱 루프(Agentic Loop) 내에서의 견고한 상태 관리 설계 패턴을 정리한다.

<br /><br />

### 1. Data Separation: 불변 파라미터 vs 가변 상태
에이전트 설계의 핵심은 루프를 도는 동안 **"절대 변하지 않는 것"**과 **"매 순간 갱신되는 것"**을 엄격히 분리하는 데 있다.<br />

**불변 파라미터(Immutable Params)** <br />
에이전트가 초기화될 때 주입되는 '제약 사항'이자 '지시서'다. 실행 도중 값이 변질되면 시스템 전체의 일관성이 깨진다. <br />
예시: taskBudget(예산), maxTurns(최대 턴수), systemPrompt 등

```ts
type QueryParams = {
  messages: Message[]
  systemPrompt: SystemPrompt
  canUseTool: CanUseToolFn       // 권한 검사 콜백
  toolUseContext: ToolUseContext   // 도구 실행 컨텍스트
  taskBudget?: { total: number }  // API task_budget (beta)
  maxTurns?: number               // 최대 턴 제한
  fallbackModel?: string          // 폴백 모델
  querySource: QuerySource        // 쿼리 출처 (REPL, agent 등)
  // ...
}
```

<br /><br />

**가변 상태(Mutable State)**
매 이터레이션(Iteration)마다 갱신되는 데이터다. 에이전트의 현재 상황을 대변한다. <br />
예시: 현재까지의 대화 기록(messages), 현재 턴 수(turnCount), 다음 액션의 근거 (transition) 

<br /><br />

### 2. Continue Site Pattern: Atomic State Update
상태를 업데이트할 때 개별 필드를 하나씩 수정하는 것이 아니라, 새로운 객체로 통째로 교체하는 방식이다.

```ts
type State = {
  messages: Message[]
  turnCount: number
  transition: Continue | undefined  // 이전 이터레이션의 계속 사유
  // ... 기타 가변 필드
}
```

<br />

왜 통째로 교체(Re-assignment)하는가?
원자성(Atomicity) 보장: 9개의 필드를 하나씩 수정하다가 3번째에서 에러가 나면, 데이터가 '반만 바뀐' 오염된 상태가 된다. 객체 전체를 새로 할당하면 "전부 성공하거나, 아예 안 바뀌거나" 둘 중 하나만 존재하게 된다.

React의 setState 철학: React의 불변성 유지 패턴을 백엔드 루프에 이식한 형태다. 상태 추적이 용이해진다.

<br /><br />

3. Transition: 상태 전이의 명시적 기록

transition 필드는 단순히 다음 단계로 넘어가는 것이 아니라, **"왜 이 다음 단계로 이동하는가"**에 대한 사유를 기록한다. 

- reason: 'next_turn': 정상적인 대화 흐름

- reason: 'error_recovery': 에러 발생에 따른 복구 시도

- reason: 'fallback': 모델 교체 및 재시도

```ts
type State = {
  messages: Message[]
  toolUseContext: ToolUseContext
  autoCompactTracking: AutoCompactTrackingState | undefined
  maxOutputTokensRecoveryCount: number
  hasAttemptedReactiveCompact: boolean
  maxOutputTokensOverride: number | undefined
  pendingToolUseSummary: Promise<ToolUseSummaryMessage | null> | undefined
  stopHookActive: boolean | undefined
  turnCount: number
  transition: Continue | undefined  // 이전 이터레이션의 계속 사유
}
```

이 패턴을 통해 복잡한 로그를 다 뒤져보지 않고도, 에이전트가 왜 특정 시점에 특정 행동을 했는지 상태 객체만 보고도 디버깅이 가능해진다.

<br /><br />

### 4. 에이전트 설계에서 이 패턴이 중요한 이유

- 비용 효율성: 상태 관리 버그는 곧 불필요한 API 호출(토큰 낭비)로 이어진다. 엄격한 상태 관리는 곧 비용 절감이다.

- 안정성: 에이전트가 무한 루프에 빠지거나, 이전 턴의 잘못된 컨텍스트를 참조하는 것을 방지한다.

- 확장성: 루프가 복잡해지더라도 상태 업데이트 로직이 한 곳(state = { ... })에 집중되어 있어 유지보수가 쉽다.

<br />

에이전트를 개발할 때 변수를 개별적으로 관리하려는 유혹을 버리자. **단일 상태 객체(Single Source of Truth)**를 유지하고, 불변성을 지키며 업데이트하는 연습이 고도화된 AI 서비스를 만드는 첫걸음이다.


<br /><br />

### 참고 문서:

- [Claude Code 내부 아키텍처 분석](https://bits-bytes-nn.github.io/insights/agentic-ai/2026/03/31/claude-code-source-map-leak-analysis.html)
