# AWS DCO 교육용 로그 분석 보고서

본 보고서는 AWS DCO(Data Center Operations) 인턴십 직무 이해를 돕기 위해 작성된 교육용 샘플 로그 분석 결과입니다.

## 1. 로그 전체 통계
- **전체 로그 라인 수:** 140개

## 2. 심각도(Severity)별 집계
| 심각도 | 로그 개수 | 점유율 |
| :--- | :---: | :---: |
| **INFO** | 135개 | 96.4% |
| **WARNING** | 3개 | 2.1% |
| **ERROR** | 2개 | 1.4% |

## 3. 이벤트 유형(Event Type)별 집계
| 순위 | 이벤트명 | 발생 횟수 |
| :---: | :--- | :---: |
| 1 | Normal heartbeat | 125회 |
| 2 | Ticket opened | 3회 |
| 3 | Ticket escalated | 3회 |
| 4 | Maintenance completed | 3회 |
| 5 | Fan Alert | 1회 |
| 6 | Temperature warning | 1회 |
| 7 | SSD failure warning | 1회 |
| 8 | CRC error 증가 | 1회 |
| 9 | Link Down | 1회 |
| 10 | Link Up | 1회 |

## 4. 고위험(WARNING / CRITICAL) 로그 목록
| 시간 | 장비명 | 심각도 | 이벤트 | 메시지 |
| :--- | :--- | :---: | :--- | :--- |
| 2026-07-03 01:05:00 | DEMO_CORE_SW_02 | `WARNING` | Fan Alert | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2 |
| 2026-07-03 02:05:00 | EDU_SRV_R04_N12 | `WARNING` | Temperature warning | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12 |
| 2026-07-03 03:05:00 | SAMPLE_TOR_SW_01 | `WARNING` | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |

## 5. 핵심 장애 및 운영 이벤트 요약
### 📌 A) CRC_ERROR (네트워크 전송 오류)
- **[2026-07-03 03:05:00]** SAMPLE_TOR_SW_01 -> Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1
- **[2026-07-03 03:30:00]** SAMPLE_TOR_SW_01 -> System status is healthy. Interface Gi0/1 running with 0 CRC errors. IP: 192.0.2.1

### 📌 B) LINK_DOWN (연결 끊김)
- **[2026-07-03 03:06:00]** SAMPLE_TOR_SW_01 -> Interface Gi0/1 status changed to DOWN. Connection to server lost.

### 📌 C) TICKET_ESCALATED (티켓 에스컬레이션)
- **[2026-07-03 01:10:00]** DEMO_CORE_SW_02 -> Ticket EDU-TKT-2026-0001 escalated to Local Infrastructure Team.
- **[2026-07-03 02:15:00]** EDU_SRV_R04_N12 -> Ticket EDU-TKT-2026-0002 escalated to DCO Hardware Support.
- **[2026-07-03 03:12:00]** SAMPLE_TOR_SW_01 -> Ticket EDU-TKT-2026-0003 escalated to Onsite Cabling Team.

