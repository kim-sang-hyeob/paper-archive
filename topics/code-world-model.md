# Code World Model

코드로 실행되는 세계·규칙과 생성 렌더러를 다루는 논문 읽기 목록.

[전체 목록](../README.md)

## 읽기 순서

1–8번은 사용자가 지정한 읽기 순서입니다. 이어서 제시한 ContextRenderer와 Zing-1.0은 9·10번에 두었습니다. 확인 메모는 사용자가 제공한 내용입니다.

| 순서 | 논문 | 읽으면서 확인할 것 (사용자 메모) |
| --- | --- | --- |
| 1 | [Code World Model: Coding Agent as World Brain](../papers/2608.25927.md) | Fig. 2, §4.1, §5를 먼저 보세요. 기존 엔진이 이미 제공한 기능과 LLM이 작성한 기능이 어디서 갈리는지가 중요합니다. 저자들도 복잡한 게임 메커니즘을 처음부터 안정적으로 구현하는 능력을 한계로 명시합니다. |
| 2 | [Programmable World Model](../papers/2609.10540.md) | 자연어 규칙 → 실행 코드 → 전역 상태 → 3D box → 영상으로 이어지는 구조입니다. 엔진에는 존재하지만 proxy를 만드는 순간 사라지는 정보가 무엇인지 보세요. |
| 3 | [WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis](../papers/2606.01869.md) | 생성된 3D 프로그램에 숨겨진 행동 테스트를 실행합니다. 가장 좋은 모델도 Robust 세트에서 검증 조건의 19.9%를 충족했고, 주요 오류는 상태 표현의 불일치와 상호작용 연쇄의 단절이었습니다. 코딩 에이전트 자체를 연구하고 싶다면 중요한 논문입니다. |
| 4 | [World Editing: Intervening on Executable Worlds at Increasing Depth](../papers/2610.02331.md) | Minecraft와 Terraria에서 기존 규칙을 수정하게 합니다. 실패한 수정의 대부분도 빌드와 로딩에는 성공했습니다. 한 규칙을 바꿨을 때 다른 동작까지 깨지는 문제를 어떻게 평가하는지 보세요. |
| 5 | [PROWBench: Do Video Models Render What the Program Specifies?](../papers/2610.02205.md) | 엔진에 기록된 사건과 생성 영상을 대조합니다. 문이 열리고 캐릭터가 통과해야 할 때, 영상에 문과 캐릭터가 모두 그럴듯하게 보여도 사건 순서는 틀릴 수 있습니다. Interaction Success Rate와 Logic-Render Alignment가 무엇을 잡는지 보세요. |
| 6 | [WorldDraft: If Code Builds the World, Can Video Models Just Render It?](../papers/2611.16217.md) | 렌더러 쪽 연구라면 가장 먼저 볼 벤치마크입니다. 같은 동작에서 proxy 디테일과 목표 외형을 독립적으로 바꿉니다. 더 자세한 proxy가 움직임을 잘 고정하면서도, proxy의 원치 않는 색과 모양까지 결과에 남기는 현상을 보여 줍니다. |
| 7 | [Code World Model 2.0: Towards Infinite Controllable Video Generation](../papers/2611.22925.md) | 1.0의 실시간 생성 문제에 어떤 진전이 있었는지 보고, §7에서 남은 한계를 읽으세요. 여러 세밀도의 proxy를 지원하지만 학습할 때 한 rollout window 안의 세밀도는 고정합니다. 오랫동안 보지 않은 장소를 재방문할 때 외형을 기억하는 문제도 남습니다. |
| 8 | [WorldRuler: Interactive World Modeling under Configurable Rules](../papers/2611.24869.md) | “규칙상 문은 열렸는데 영상에는 닫혀 있다”는 예시가 핵심입니다. 규칙이 요구한 값과 화면에서 관측한 값을 따로 저장하고 다음 생성을 보정합니다. 시각 피드백을 제안하려면 이 논문과 RIGen이 이미 어디까지 했는지 같이 봐야 합니다. |
| 9 | [ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds](../papers/2611.25838.md) | 추가 읽기 목록 |
| 10 | [Zing-1.0: A Playable World System Built on Controllable Rendering](../papers/2611.27336.md) | 추가 읽기 목록 |

## 논문 목록

| 상태 | 논문 | 유형 | 주분류 | 기억할 단서 |
| --- | --- | --- | --- | --- |
| 미독 | [Code World Model: Coding Agent as World Brain](../papers/2608.25927.md) | 방법론 | Code World Model | Code World Model 읽기 01 — Code World Model |
| 미독 | [Programmable World Model](../papers/2609.10540.md) | 방법론 | Code World Model | Code World Model 읽기 02 — Programmable World Model |
| 미독 | [WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis](../papers/2606.01869.md) | 벤치마크 | Code World Model | Code World Model 읽기 03 — WorldCoder-Bench |
| 미독 | [World Editing: Intervening on Executable Worlds at Increasing Depth](../papers/2610.02331.md) | 벤치마크 | Code World Model | Code World Model 읽기 04 — World Editing |
| 미독 | [PROWBench: Do Video Models Render What the Program Specifies?](../papers/2610.02205.md) | 벤치마크 | Code World Model | Code World Model 읽기 05 — PROWBench |
| 미독 | [WorldDraft: If Code Builds the World, Can Video Models Just Render It? (WorldDraft)](../papers/2611.16217.md) | 벤치마크 | Code World Model | Code World Model 읽기 06 — WorldDraft |
| 미독 | [Code World Model 2.0: Towards Infinite Controllable Video Generation (Invoker-Render)](../papers/2611.22925.md) | 방법론 | Code World Model | Code World Model 읽기 07 — Code World Model 2.0 |
| 미독 | [WorldRuler: Interactive World Modeling under Configurable Rules (WorldRuler)](../papers/2611.24869.md) | 방법론 | Code World Model | Code World Model 읽기 08 — WorldRuler |
| 미독 | [ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds (ContextRenderer)](../papers/2611.25838.md) | 방법론 | Code World Model | Code World Model 읽기 09 — ContextRenderer |
| 미독 | [Zing-1.0: A Playable World System Built on Controllable Rendering (Zing-1.0)](../papers/2611.27336.md) | 기술 보고서 | Code World Model | Code World Model 읽기 10 — Zing-1.0 |
