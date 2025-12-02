<!--
This file is generated/maintained to help AI coding agents (Copilot-like) work productively
in this small Python scripts repository. Keep this short, concrete and repo-specific.
-->

# Copilot / AI agent instructions (project-specific)

요약
- 이 저장소는 독립적으로 실행되는 작은 Python 스크립트(`hello.py`, `output.py`, `string_operator02.py`)들의 모음입니다.
- 패키지/모듈 구조나 테스트 프레임워크가 없습니다. 변경은 가능한 한 작고 명확하게 하세요.

핵심 컨텍스트
- 파일 위치: 최상위에 스크립트 파일들이 존재합니다. 예: `hello.py`, `output.py`, `string_operator02.py`.
- 실행: 각 스크립트는 직접 실행되는 형태(탑레벨 코드)를 사용합니다. 실행 예:

```powershell
python .\hello.py
python .\output.py
python .\string_operator02.py
```

코드패턴 및 관습 (이 리포지토리에만 적용)
- 대부분 파일은 탑레벨에서 `print`로 결과를 출력합니다 (한 줄 또는 여러 인자 전달).
- 파일 내 주석은 한국어로 작성되어 있으며, UTF-8 인코딩을 유지해야 합니다.
- 새로운 기능을 추가할 때는 가능하면 함수로 추출하고 `if __name__ == '__main__':` 블록을 추가해
  기존의 탑레벨 실행 방식을 해치지 마세요.

수정 제안 가이드
- 최소 변경 원칙: 기존 스크립트 구조(탑레벨 출력)를 바꾸지 말고, 기능 추가는 작은 함수/헬퍼로 분리하세요.
- 파일을 리팩터링할 경우 예시 실행 명령과 출력(또는 기대 동작)을 커밋 메시지나 PR 설명에 포함시켜 검증을 쉽게 만드세요.
- 외부 의존성 추가는 피하세요. 꼭 필요하면 `requirements.txt`를 추가하고 이유를 명확히 적으세요.

테스트 및 검증
- 현재 유닛 테스트가 없습니다. 변경을 검증하려면 해당 스크립트를 직접 실행하고 출력 결과를 확인하세요.

예시(작업 흐름)
1. 기능 추가: `string_operator02.py`에 문자열 처리 함수 `def split_and_print(s):` 추가
2. 로컬 실행: `python .\string_operator02.py`로 동작 확인
3. PR: 변경 이유, 로컬 검증 명령, 기대 출력(간단히)을 PR 설명에 포함

참고 파일
- `hello.py`: 간단한 출력 예시
- `output.py`: 여러 `print` 호출 및 한글 주석 예시
- `string_operator02.py`: 산술 연산 및 주석된 문자열 예시

커밋 메시지 스타일 (이 저장소 권장)
- 한 줄 요약: 영어 또는 한글로, 최대 50자 내외로 핵심을 적습니다.
- 빈 줄 한 줄 후 상세 설명(선택): 변경 이유, 로컬 검증 방법, 영향 범위 등을 작성하세요.
- 메시지 시작 규칙(권장 접두어):
  - `feat:` 새로운 기능
  - `fix:` 버그 수정
  - `chore:` 문서/빌드/기타 비기능적 변경
- 예시:

```text
feat: add split_and_print helper to string_operator02.py

추가: `split_and_print` 함수를 도입해 문자열 분할 출력 기능을 제공함.
로컬 검증: `python .\string_operator02.py` 실행 후 출력 확인
```

브랜치 규칙
- 보호 브랜치: `main`(또는 `master`)는 항상 배포 가능한 상태로 유지합니다. 직접 푸시하지 마세요.
- 기능 브랜치: `feat/<짧은-설명>` 예: `feat/split-helper`
- 버그 브랜치: `fix/<짧은-설명>` 예: `fix/print-order`
- 문서 브랜치: `docs/<짧은-설명>`
- 작업 흐름: 로컬에서 브랜치 생성 → 변경 커밋(권장 메시지 스타일) → 원격에 푸시 → PR 생성 → 리뷰 요청

풀 리퀘스트(Pr) 내용 권장 템플릿
- 변경 요약(한두 문장)
- 로컬 검증 방법(명령어): 예 `python .\string_operator02.py`
- 영향 범위: 변경된 주요 파일 목록

머지/리뷰 정책 (권장)
- 최소 리뷰 승인 1회 필요.
- 단순 문법/주석 변경은 1인 승인으로 머지 가능.

마무리
- 추가 규칙(예: 커밋 태그, 이슈 연결 포맷)을 원하시면 알려주시면 반영하겠습니다.

CI / 포맷 & 린트 (GitHub Actions 예시)
- 간단한 CI 워크플로를 추가했습니다: `.github/workflows/ci.yml` (Black + Flake8 검사).
- 워크플로 요약: `black --check .`로 포맷 일관성 검사, `flake8 .`로 린트 검사.
- 로컬에서 동일한 검사를 실행하려면(권장):

```powershell
python -m pip install --upgrade pip
pip install black==23.9.1 flake8
black --check .
flake8 .
```

- 워크플로가 실패하면, 로컬에서 `black .`을 실행해 자동 포맷을 적용한 다음 변경을 커밋하세요.

파일 위치: `.github/workflows/ci.yml`
This file is generated/maintained to help AI coding agents (Copilot-like) work productively
-->
# Copilot / AI agent instructions (project-specific)

요약
- 이 저장소는 독립적으로 실행되는 작은 Python 스크립트(`hello.py`, `output.py`, `string_operator02.py`)들의 모음입니다.
- 패키지/모듈 구조나 테스트 프레임워크가 없습니다. 변경은 가능한 한 작고 명확하게 하세요.

핵심 컨텍스트
- 파일 위치: 최상위에 스크립트 파일들이 존재합니다. 예: `hello.py`, `output.py`, `string_operator02.py`.
- 실행: 각 스크립트는 직접 실행되는 형태(탑레벨 코드)를 사용합니다. 실행 예:

```powershell
python .\hello.py
python .\output.py
python .\string_operator02.py
```

코드패턴 및 관습 (이 리포지토리에만 적용)
- 대부분 파일은 탑레벨에서 `print`로 결과를 출력합니다 (한 줄 또는 여러 인자 전달).
- 파일 내 주석은 한국어로 작성되어 있으며, UTF-8 인코딩을 유지해야 합니다.
- 새로운 기능을 추가할 때는 가능하면 함수로 추출하고 `if __name__ == '__main__':` 블록을 추가해
  기존의 탑레벨 실행 방식을 해치지 마세요.

수정 제안 가이드
- 최소 변경 원칙: 기존 스크립트 구조(탑레벨 출력)를 바꾸지 말고, 기능 추가는 작은 함수/헬퍼로 분리하세요.
- 파일을 리팩터링할 경우 예시 실행 명령과 출력(또는 기대 동작)을 커밋 메시지나 PR 설명에 포함시켜 검증을 쉽게 만드세요.
- 외부 의존성 추가는 피하세요. 꼭 필요하면 `requirements.txt`를 추가하고 이유를 명확히 적으세요.

테스트 및 검증
- 현재 유닛 테스트가 없습니다. 변경을 검증하려면 해당 스크립트를 직접 실행하고 출력 결과를 확인하세요.

예시(작업 흐름)
1. 기능 추가: `string_operator02.py`에 문자열 처리 함수 `def split_and_print(s):` 추가
2. 로컬 실행: `python .\string_operator02.py`로 동작 확인
3. PR: 변경 이유, 로컬 검증 명령, 기대 출력(간단히)을 PR 설명에 포함

참고 파일
- `hello.py`: 간단한 출력 예시
- `output.py`: 여러 `print` 호출 및 한글 주석 예시
- `string_operator02.py`: 산술 연산 및 주석된 문자열 예시

질문할 것
- 변경이 스크립트 형태(탑레벨 실행)를 바꾸어도 되는지, 패키징으로 전환해도 되는지 사전에 확인하세요.

---
원하시면 이 초안을 조정해 더 상세한 개발자 워크플로(예: 린트, 테스트, CI 명령)를 추가하겠습니다.
