import "../src/index.css";

export const parameters = {
  // actions(= mocked callbacks)이 처리되는 방식 구성
  // 임의의 버튼 생성할 때, 버튼 클릭이 성공적이었는지 테스트UI에서 확인 가능
  actions: { argTypesRegex: "^on[A-Z].*" },
};
