# AWS DCO Internship Learning Portfolio
## 생성형 AI를 활용한 Data Center Operations(DCO) 학습 프로젝트

## 프로젝트 소개

이 저장소는 **AWS Data Center Operations(DCO) 인턴십 직무를 이해하기 위한 교육용 학습 포트폴리오**입니다.

공개된 DCO 직무 정보와 교육용 샘플 데이터를 기반으로 생성형 AI를 활용하여 로그 분석, Python 코드 작성, Incident Report 작성, Ticket 우선순위 판단 및 Shift Handover 작성 과정을 학습한 결과물을 정리했습니다.

생성형 AI를 단순히 답을 생성하는 도구로 사용하지 않고,

- DCO 용어 학습
- Python 코드 작성
- 로그 분석
- Incident Report 초안 작성
- Ticket 우선순위 분석
- Shift Handover 작성
- 결과 검증 및 수정

과 같은 업무를 보조하는 도구로 활용했습니다.

> **NOTICE**
>
> 본 프로젝트는 교육용 학습 자료입니다.
> 실제 AWS 내부 시스템, 실제 운영 로그, 실제 Ticket, 실제 데이터센터 장비 또는 실제 운영 절차를 사용하지 않았습니다.
> 모든 장비명, Ticket ID, IP 주소와 장애 상황은 교육용 샘플 데이터입니다.

---

# 차시별 학습 내용

| 차시 | 학습 내용 |
|------|-----------|
| 1차시 | AWS DCO 직무와 생성형 AI 활용 이해 |
| 2차시 | 개인 강점 및 협업 유형 분석 |
| 3차시 | DCO 기초 용어 정리 |
| 4차시 | 교육용 SOP 분석 및 체크리스트 작성 |
| 5차시 | VS Code, Python, Git, GitHub 개발환경 구성 |
| 6차시 | Antigravity CLI(agy) 설치 및 실행 |
| 7차시 | agy를 활용한 로컬 프로젝트 자동화 |
| 8차시 | agy 기반 교육용 로그 분석 |
| 9차시 | Google AI Studio와 ChatGPT를 활용한 Python 로그 분석 및 Dashboard 제작 |
| 10차시 | CRC Error 및 Link Down Incident 분석 |
| 11차시 | 교육용 Incident Report 작성 및 검증 |
| 12차시 | Ticket 우선순위 판단 및 Shift Handover 작성 |

---

# 프로젝트에서 수행한 주요 활동

- 공개 직무 정보를 기반으로 DCO 핵심 업무 분석
- DCO 직무 협업 유형 리포트 작성
- Rack, Server, Ticket, SOP, SLA, NIC, ToR Switch 등 핵심 용어 정리
- 교육용 SOP를 절차와 체크리스트 형태로 재구성
- Python, Git, GitHub, VS Code, Antigravity CLI 실습 환경 구축
- agy를 활용한 로컬 파일 생성 및 자동화
- Google AI Studio를 활용한 Python 로그 분석 코드 작성
- 로그 분석 결과 Dashboard 제작
- CRC Error와 Link Down 사건 분석
- Incident Report 작성
- Ticket Priority Matrix 작성
- Shift Handover Memo 작성
- Git과 GitHub를 활용한 프로젝트 버전 관리

---

# 사용 기술 및 도구

| 기술 | 활용 내용 |
|-------|-----------|
| ChatGPT | DCO 용어 이해, 문서 구조화, 코드 검토 및 보고서 작성 |
| Google AI Studio | Python 로그 분석 코드 생성 |
| Antigravity CLI (agy) | 로컬 파일 자동화 및 Incident Report 작성 |
| Python | 로그 분석 프로그램 작성 |
| Markdown | 보고서 작성 |
| VS Code | 프로젝트 개발 환경 |
| Git | 버전 관리 |
| GitHub | 포트폴리오 관리 |
| Notion | 실습 결과 제출 |

---

# Repository Structure

```text
AWS-DCO-GenAI-Portfolio/
│
├── 01_dco_job_understanding/
├── 02_teamwork_profile/
├── 03_dco_terms/
├── 04_environment_setup/
├── 05_ai_prompt/
├── 06_agy_practice/
├── 07_log_analysis/
├── 08_dashboard/
├── 09_log_analysis_script/
├── 10_incident_analysis/
├── 11_incident_report/
├── 12_ticket_triage_handover/
└── README.md
```

---

# 주요 산출물

- DCO 직무 키워드 정리
- DCO 협업 유형 리포트
- DCO 용어 사전
- 교육용 SOP 체크리스트
- Python 로그 분석 프로그램
- 로그 분석 Dashboard
- CRC Error · Link Down Incident 분석
- 교육용 Incident Report
- Ticket Priority Matrix
- Shift Handover Memo

---

# 생성형 AI 활용 원칙

본 프로젝트에서는 생성형 AI를 다음 원칙에 따라 활용했습니다.

- AI 결과를 최종 정답으로 사용하지 않았습니다.
- 원본 로그와 AI 결과를 비교하여 직접 검증했습니다.
- 로그에서 확인되는 사실과 가능한 추정을 구분했습니다.
- Root Cause를 로그만으로 단정하지 않았습니다.
- Ticket 우선순위는 AI가 아닌 학습자가 직접 판단했습니다.
- 실제 AWS 내부 정보나 고객 정보를 입력하지 않았습니다.
- 모든 데이터는 교육용 샘플 데이터입니다.

---

# 프로젝트를 통해 배운 점

이번 프로젝트를 수행하면서 다음과 같은 내용을 학습했습니다.

- 생성형 AI는 로그 분석과 문서 작성 시간을 크게 줄여줄 수 있습니다.
- AI가 생성한 결과는 반드시 원본 자료와 비교하여 검증해야 합니다.
- 로그 분석에서는 확인된 사실과 가능한 추정을 구분해야 합니다.
- 장애가 복구되었다고 해서 Root Cause가 확인된 것은 아닙니다.
- Priority는 Severity만으로 결정되지 않습니다.
- 서비스 영향, 반복 여부, 영향 범위, 복구 여부를 함께 고려해야 합니다.
- Incident Report는 다른 담당자가 이해할 수 있도록 작성해야 합니다.
- Shift Handover는 다음 담당자가 바로 업무를 이어받을 수 있도록 작성해야 합니다.
- AI 활용 과정과 직접 수정한 내용을 기록하는 것이 중요합니다.

---

# Skills Demonstrated

- Linux Basics
- Python Programming
- Log Parsing
- Incident Analysis
- Ticket Triage
- Shift Handover
- Git & GitHub
- Markdown Documentation
- Prompt Engineering
- AI-assisted Documentation
- Data Center Operations Fundamentals

---

# 프로젝트 범위

본 프로젝트는 AWS Data Center Operations(DCO) 직무 이해를 위한 학습 포트폴리오입니다.

다음 내용은 포함하지 않습니다.

- 실제 AWS 운영 환경
- 실제 데이터센터 운영 절차
- 실제 고객 정보
- 실제 Ticket
- 실제 장애 대응
- 실제 장비 운영

공개된 직무 정보와 교육용 샘플 데이터를 이용한 학습 결과만 포함합니다.

---

# Educational Sample Data

> **EDUCATIONAL SAMPLE DATA**
>
> All logs, device names, Ticket IDs, IP addresses, incident scenarios, and reports contained in this repository are fictional educational samples created solely for learning purposes.
>
> This repository does **not** contain any AWS internal documents, production systems, customer information, or confidential operational procedures.
>
> ![Python](https://img.shields.io/badge/Python-3.x-blue)
![Git](https://img.shields.io/badge/Git-Version%20Control-red)
![AI](https://img.shields.io/badge/Generative%20AI-ChatGPT%20%7C%20Gemini-green)
![License](https://img.shields.io/badge/License-Educational-lightgrey)
