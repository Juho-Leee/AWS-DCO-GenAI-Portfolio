# 데이터 센터(DCO) 교육용 로그 분석 보고서

## 1. 전체 로그 요약
- **분석 파일**: `07_log_analysis_script/sample_dco_log.txt`
- **총 분석 대상 라인**: 140개

## 2. 심각도(Severity)별 발생 통계
| 심각도 (Severity) | 빈도 (Count) |
| :--- | :--- |
| ERROR | 2 |
| INFO | 135 |
| WARNING | 3 |

## 3. 이벤트(Event)별 통계
| 이벤트 (Event) | 빈도 (Count) |
| :--- | :--- |
| Normal heartbeat | 125 |
| Ticket opened | 3 |
| Ticket escalated | 3 |
| Maintenance completed | 3 |
| Fan Alert | 1 |
| Temperature warning | 1 |
| SSD failure warning | 1 |
| CRC error 증가 | 1 |
| Link Down | 1 |
| Link Up | 1 |

## 4. WARNING 및 CRITICAL 로그 목록
1. `2026-07-03 01:05:00 | DEMO_CORE_SW_02 | WARNING | Fan Alert | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2`
2. `2026-07-03 02:05:00 | EDU_SRV_R04_N12 | WARNING | Temperature warning | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12`
3. `2026-07-03 03:05:00 | SAMPLE_TOR_SW_01 | WARNING | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1`

## 5. 주요 인시던트(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) 요약
- 대상 키워드와 일치하는 주요 인시던트가 발견되지 않았습니다.
