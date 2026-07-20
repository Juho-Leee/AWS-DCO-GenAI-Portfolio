#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AWS DCO 인턴십 직무 이해를 위한 교육용 로그 분석 스크립트
(비전공자 및 입문자를 위한 상세한 주석 포함)
"""

import os
from collections import Counter
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "sample_dco_log.txt"
OUTPUT_FILE = BASE_DIR / "incident_summary.md"

def analyze_dco_logs():
    if not os.path.exists(INPUT_FILE):
        print(f"오류: '{INPUT_FILE}' 파일이 존재하지 않습니다.")
        return

    print("==================================================")
    print("      AWS DCO 교육용 로그 분석을 시작합니다       ")
    print("==================================================")

    total_lines = 0
    severity_counter = Counter()
    event_counter = Counter()
    high_severity_logs = []
    
    major_events = {
        "CRC_ERROR": [],
        "LINK_DOWN": [],
        "TICKET_ESCALATED": []
    }

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            
            total_lines += 1
            parts = [part.strip() for part in line.split("|")]
            
            if len(parts) < 5:
                continue
                
            timestamp = parts[0]
            device = parts[1]
            severity = parts[2].upper()
            event = parts[3]
            message = parts[4]
            
            severity_counter[severity] += 1
            event_counter[event] += 1
            
            if severity in ["WARNING", "CRITICAL"]:
                high_severity_logs.append({
                    "line_num": line_num,
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })
                
            event_lower = event.lower()
            msg_lower = message.lower()
            
            if "crc" in event_lower or "crc" in msg_lower:
                major_events["CRC_ERROR"].append({
                    "timestamp": timestamp, "device": device, "severity": severity, "message": message
                })
                
            if "link down" in event_lower or "link_down" in event_lower or "status changed to down" in msg_lower:
                major_events["LINK_DOWN"].append({
                    "timestamp": timestamp, "device": device, "severity": severity, "message": message
                })
                
            if "escalat" in event_lower or "escalat" in msg_lower or "ticket escalated" in event_lower:
                major_events["TICKET_ESCALATED"].append({
                    "timestamp": timestamp, "device": device, "severity": severity, "message": message
                })

    print(f"1. 전체 로그 수: 총 {total_lines}줄")
    print("\n2. 심각도별 개수:")
    for sev, count in severity_counter.items():
        print(f"   - {sev}: {count}개")
        
    print("\n3. 이벤트별 개수 (상위 5개):")
    for ev, count in event_counter.most_common(5):
        print(f"   - {ev}: {count}개")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("# AWS DCO 교육용 로그 분석 보고서\n\n")
        out.write("본 보고서는 AWS DCO(Data Center Operations) 인턴십 직무 이해를 돕기 위해 작성된 교육용 샘플 로그 분석 결과입니다.\n\n")
        out.write("## 1. 로그 전체 통계\n")
        out.write(f"- **전체 로그 라인 수:** {total_lines}개\n\n")
        
        out.write("## 2. 심각도(Severity)별 집계\n")
        out.write("| 심각도 | 로그 개수 | 점유율 |\n")
        out.write("| :--- | :---: | :---: |\n")
        for sev, count in severity_counter.items():
            percentage = (count / total_lines) * 100
            out.write(f"| **{sev}** | {count}개 | {percentage:.1f}% |\n")
        out.write("\n")
        
        out.write("## 3. 이벤트 유형(Event Type)별 집계\n")
        out.write("| 순위 | 이벤트명 | 발생 횟수 |\n")
        out.write("| :---: | :--- | :---: |\n")
        for idx, (ev, count) in enumerate(event_counter.most_common(), 1):
            out.write(f"| {idx} | {ev} | {count}회 |\n")
        out.write("\n")
        
        out.write("## 4. 고위험(WARNING / CRITICAL) 로그 목록\n")
        if high_severity_logs:
            out.write("| 시간 | 장비명 | 심각도 | 이벤트 | 메시지 |\n")
            out.write("| :--- | :--- | :---: | :--- | :--- |\n")
            for log in high_severity_logs:
                out.write(f"| {log['timestamp']} | {log['device']} | `{log['severity']}` | {log['event']} | {log['message']} |\n")
        else:
            out.write("- 고위험 로그가 발견되지 않았습니다.\n")
        out.write("\n")
        
        out.write("## 5. 핵심 장애 및 운영 이벤트 요약\n")
        out.write("### 📌 A) CRC_ERROR (네트워크 전송 오류)\n")
        if major_events["CRC_ERROR"]:
            for item in major_events["CRC_ERROR"]:
                out.write(f"- **[{item['timestamp']}]** {item['device']} -> {item['message']}\n")
        else:
            out.write("- 관련 이벤트 없음\n")
        out.write("\n")
        
        out.write("### 📌 B) LINK_DOWN (연결 끊김)\n")
        if major_events["LINK_DOWN"]:
            for item in major_events["LINK_DOWN"]:
                out.write(f"- **[{item['timestamp']}]** {item['device']} -> {item['message']}\n")
        else:
            out.write("- 관련 이벤트 없음\n")
        out.write("\n")
        
        out.write("### 📌 C) TICKET_ESCALATED (티켓 에스컬레이션)\n")
        if major_events["TICKET_ESCALATED"]:
            for item in major_events["TICKET_ESCALATED"]:
                out.write(f"- **[{item['timestamp']}]** {item['device']} -> {item['message']}\n")
        else:
            out.write("- 관련 이벤트 없음\n")
        out.write("\n")

    print("\n분석 완료! 결과가 'incident_summary.md' 파일로 저장되었습니다.")

if __name__ == '__main__':
    analyze_dco_logs()
