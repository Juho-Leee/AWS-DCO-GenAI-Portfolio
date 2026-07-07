# [교육용 샘플 데이터 / FOR EDUCATIONAL USE ONLY]
본 문서는 교육용 목적으로 작성된 샘플 데이터이며, 실제 시스템, 장비, IP 주소 또는 고객 정보와 일치하지 않는 가상의 시나리오입니다.

---

## 교육용 샘플 티켓 (EDU-SAMPLE-TICKET-20260707)

*   **티켓 ID**: EDU-SAMPLE-TICKET-20260707-001
*   **발생 시간**: 2026-07-07 15:10:00 (KST)
*   **샘플 장비명**: SAMPLE_TOR_SW_01
*   **이벤트**: Interface CRC Error Increment & Link Down
*   **심각도**: Severity-2 (Major)
*   **Escalation 필요 여부**: 필요 (Yes)
*   **보안 주의사항**:
    *   본 정보는 교육 목적의 테스트 정보입니다.
    *   실제 장비의 IP, 계정 패스워드, 개인 신상 정보 등을 티켓 본문 및 로그 파일에 기입하지 마십시오.
    *   임의의 외부 IP 또는 검증되지 않은 외부 도구로의 접속 및 스캔을 금지합니다.

### 1. 관찰 내용 (Observations)
*   샘플 스위치 `SAMPLE_TOR_SW_01`에서 가상의 인터페이스 `SAMPLE-Eth1/1` 상의 CRC 에러 카운터가 지속적으로 증가하는 것이 관찰됨.
*   에러 누적 이후 해당 포트의 링크가 다운(`Link Down`) 상태로 천이됨.
*   물리 계층(Physical Layer) 상의 연결 불안정 또는 가상의 광케이블/트랜시버(SFP) 접촉 불량이 의심되는 교육용 시뮬레이션 상황임.
