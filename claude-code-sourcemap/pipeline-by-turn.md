## Claude Code 설계 분석: 6단계 파이프라인

에이전트가 한 턴(Turn)을 수행할 때 거치는 정교한 실행 공정을 정리한다.<br />
단순히 '질문하고 듣는 것'을 넘어 성능, 비용, 안정성을 극대화하는 설계가 핵심이다.

<br /><br />

### 1. Pre-Request Compaction: 지능적인 컨텍스트 압축

에이전트에게 과거 히스토리를 무작정 다 전달하면 토큰 제한(Context Window)에 걸리거나 비용이 폭증한다. <br />
질문을 던지기 전, 저비용에서 고비용 순서로 압축 메커니즘을 적용한다. <br />

- Tool Result Budget: 수천 줄의 로그나 파일 읽기 결과를 예산 내로 커팅

- Snip Compact: 가장 오래된 메시지를 과감히 삭제 (가장 저렴하고 과격함)

- Microcompact: 프롬프트 캐시(Prompt Cache)를 깨뜨리지 않는 선에서 개별 도구 실행 결과를 선택적으로 제거

- Context Collapse: 원본은 유지하되 메시지 블록 단위로 축소된 뷰를 생성

- Auto-Compact: 위 단계로도 부족할 때만 LLM을 사용해 전체 내용을 요약 (가장 비싸지만 효과적인 방법)

Note: 압축으로 메시지가 날아가면 서버는 소비된 토큰을 알 수 없다. 클라이언트가 직접 잔여 예산을 계산해 서버에 알려주는 상태 동기화가 에이전틱 시스템의 까다로운 지점이다.

<br /><br />

### 2. API Call & Streaming: 도구 병렬 실행 (Concurrency)

StreamingToolExecutor를 통해 모델이 응답을 생성하는 동안 실행 가능한 도구를 미리 실행하여 대기 시간을 줄인다. <br />

- isConcurrencySafe: 모든 도구에는 동시 실행 가능 여부 플래그가 있다.
  - FileReadTool, GlobTool: true (병렬 실행 가능)

  - FileWriteTool, BashTool: false (환경 변화 방지를 위해 반드시 순차 실행)

- Tombstone(묘비) 메시지: 모델 폴백(Fallback) 발생 시, 이전 모델이 요청했던 도구 호출 자리에 "무효화됨" 마커를 남겨 히스토리의 정합성을 유지한다.

- Error Handling: 한 도구가 에러를 내면 병렬로 실행 중이던 형제 도구들도 sibling_error로 즉시 취소하여 자원 낭비를 막는다.

<br /><br />

### 3. Error Recovery Cascade: 저비용 중심의 복구 전략

API 호출 실패(413 에러, 토큰 초과 등) 시 사용자에게 즉시 에러를 던지지 않고 단계별 복구를 시도한다.<br />
**첫 번째 시도는 항상 무료(Free)**여야 한다는 철학이 담겨 있다.<br />

예: Prompt-too-long (413 에러) 복구 <br />

- 1단계 (비용 0): Context Collapse를 즉시 확정(Commit)하여 컨텍스트 축소

- 2단계 (유료 API): Reactive Compact를 통해 전체 대화 요약 및 이미지 스트리핑 후 재시도

- 3단계: 모든 시도 실패 시 에러 표출

<br /><br />

### 4. Stop Hooks & Token Budget: 에이전트 무한 루프 방지

에이전트가 정답을 찾지 못하고 무의미하게 반복 작업을 수행하는 '고집'을 꺾는 장치다. <br />

- Stop Hooks: "테스트 통과 전까지 멈추지 마" 같은 검증 로직을 주입하여 작업의 완결성을 보장한다.

- Diminishing Returns (감소 수익 감지): 3회 연속 시도했으나 생성된 토큰이 미미하다면 "삽질 중"으로 판단하고 예산이 남았더라도 스스로 중단한다.
  <br />

```ts
// 삽질 감지 로직의 핵심
const isDiminishing =
  continuationCount >= 3 && // 3회 이상 연속 시도
  deltaSinceLastCheck < 500 && // 직전 체크 대비 진전 미비
  lastDeltaTokens < 500; // 그 전에도 진전 미비
```

<br /><br />

### 5. Tool Execution & UI Feedback: 결과 수거 및 배치 실행

2단계에서 미리 실행해 둔 도구들의 결과를 수집하고, 병렬로 돌리지 못한 나머지 도구들을 처리한다. <br />

- 결과 수확: StreamingToolExecutor가 이미 완료한 작업들을 수거하여 응답 속도를 높인다.

- UX 안정성: 도구가 실행되는 동안 UI 상에서 스피너(Spinner)나 진행 상태를 실시간으로 업데이트(progressAvailableResolve)하여 사용자의 심리적 불안을 해소한다.

<br /><br />

### 6. Post-Tool & Prefetch: 다음 턴을 위한 선제적 준비

- Prefetch 패턴: 1단계(압축) 시점에 비동기로 미리 시작해둔 '스킬 목록 조회'나 '메모리 로드' 결과를 여기서 수확한다. 네트워크 레이턴시를 백그라운드에서 상쇄하는 기법

- 상태 전이: 모든 결과(Messages + Tool Results)를 하나로 합쳐 Continue Site Pattern에 따라 다음 턴의 상태로 원자적으로 전이시킨다.

<br /><br />

### 참고 문서:

- [Claude Code 내부 아키텍처 분석](https://bits-bytes-nn.github.io/insights/agentic-ai/2026/03/31/claude-code-source-map-leak-analysis.html)
