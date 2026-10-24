# 논문 보관함

나중에 제목이 기억나지 않아도 내용과 키워드로 다시 찾기 위한 개인 논문 목록입니다.

현재 2편, 미독 2편. 최근 수정일 2026-10-24.

논문 링크만 보내면 기본으로 미독 등록, 대략 분류, 짧은 요약과 검색 키워드 작성을 거쳐 이 공개 GitHub 보관함에 추가합니다. 이미 보관한 논문은 기존 읽기 상태와 메모를 유지합니다.

## 전체 목록

| 상태 | 논문 | 유형 | 주분류 | 기억할 단서 |
| --- | --- | --- | --- | --- |
| 미독 | [Reading, Writing, Sharing, and Interacting with the World through Video](papers/2610.31668.md) | 서베이 | 비디오 월드 모델 | 비디오 이해·생성·월드모델 전반을 네 축으로 정리한 서베이 |
| 미독 | [Self-Improving Video-to-Action Models (Mirror)](papers/2610.24177.md) | 방법론 | 행동 학습과 에이전트 | 영상 계획을 따라 직접 시행착오하며 행동 모델을 개선하는 Minecraft Mirror 논문 |

초록과 공식 프로젝트 페이지를 바탕으로 초벌 분류했습니다. 읽기 상태는 사용자의 상태입니다.

## 주제별 보기

한 논문이 여러 주제에 속할 수 있습니다. 서베이와 방법론은 유형으로, 미독과 완독은 읽기 상태로 따로 관리합니다.

- [비디오 월드 모델](topics/video-world-models.md): 1편. 영상으로 세계 상태와 시간에 따른 변화를 모델링하는 연구.
- [비디오 이해](topics/video-understanding.md): 1편. 영상의 의미, 공간, 시간, 물리 및 인과 관계를 이해하는 연구.
- [비디오 생성](topics/video-generation.md): 2편. 영상을 생성하거나 편집하고 미래 장면을 예측하는 연구.
- [행동 학습과 에이전트](topics/embodied-agents.md): 1편. 관측과 영상 계획을 실제 행동, 제어, 환경 상호작용으로 연결하는 연구.

## 내용으로 다시 찾기

이 프로젝트의 채팅에서는 ‘보관한 논문 중 마인크래프트에서 영상으로 행동을 배우는 거 찾아줘’처럼 말하면 됩니다. 다른 채팅에서는 이 공개 저장소 링크를 함께 주고 검색을 요청하세요. 내용을 읽을 수 있는 웹 도구, GitHub 연결 또는 로컬 파일 접근이 필요합니다.

로컬에서 키워드로 찾으려면:

```bash
python3 scripts/archive.py search "마인크래프트 행동"
python3 scripts/archive.py search "월드모델 서베이"
```

## 기록과 수정

`catalog.json`에 제목, 저자, 원문 링크, 한글 요약, 분류, 검색 키워드, 읽기 상태, 사용자 메모를 저장합니다. 새 논문을 등록할 때 arXiv ID가 같은 항목은 중복 생성하지 않고 갱신합니다. 원문은 arXiv 및 PDF 링크로 보관합니다.

분류표와 논문별 메모는 아래 명령으로 갱신합니다:

```bash
python3 scripts/archive.py build
python3 scripts/archive.py check
```

[엑셀 내려받기](paper_archive.xlsx)는 2026-10-24에 만든 초기 스냅샷입니다. 최신 목록은 이 페이지와 `catalog.json`에서 확인합니다.
