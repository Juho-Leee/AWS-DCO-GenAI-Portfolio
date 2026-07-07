import os

# 1. 파일 경로 설정
# 분석할 입력 파일과 결과를 저장할 출력 파일의 경로를 정의합니다.
INPUT_FILE_PATH = "07_log_analysis_script/sample_dco_log.txt"
OUTPUT_FILE_PATH = "07_log_analysis_script/incident_summary.md"

def analyze_dco_logs():
    # 분석 결과를 담을 변수들을 준비합니다.
    total_lines = 0                     # 1. 전체 로그 줄 수
    severity_counts = {}                # 2. 심각도별 개수를 세기 위한 사전(Dictionary)
    event_counts = {}                   # 3. 이벤트별 개수를 세기 위한 사전(Dictionary)
    warning_critical_logs = []          # 4. WARNING 및 CRITICAL 로그를 모아둘 리스트(List)
    major_events_summary = []           # 5. 주요 장애 키워드 관련 로그를 모아둘 리스트

    # 주요 감시 대상 키워드 정의
    target_keywords = ["CRC_ERROR", "LINK_DOWN", "TICKET_ESCALATED"]

    # 2. 파일 읽기 작업 시작 (예외 처리 구문 적용)
    try:
        with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as file:
            for line in file:
                # 각 줄 끝의 줄바꿈 문자('\n')를 제거합니다.
                line = line.strip()
                
                # 빈 줄은 건너뜁니다.
                if not line:
                    continue
                
                # 전체 줄 수를 하나씩 올립니다.
                total_lines += 1
                
                # 로그 형식 구분자인 ' | '를 기준으로 데이터를 쪼갭니다.
                # 예: "시간 | 장비 | 심각도 | 이벤트 | 메시지"
                parts = [part.strip() for part in line.split('|')]
                
                # 분할된 데이터가 5개 필드를 정상적으로 가졌는지 검증합니다.
                if len(parts) < 5:
                    continue
                
                # 가독성을 위해 각 필드에 이름을 붙여 줍니다.
                timestamp, device, severity, event, message = parts
                
                # [분석 2] 심각도별 개수 카운트
                # 사전에 이미 등록되어 있으면 +1, 없으면 기본값 0에서 +1을 합니다.
                severity_counts[severity] = severity_counts.get(severity, 0) + 1
                
                # [분석 3] 이벤트별 개수 카운트
                event_counts[event] = event_counts.get(event, 0) + 1
                
                # [분석 4] WARNING 또는 CRITICAL 로그 추출
                if severity in ["WARNING", "CRITICAL"]:
                    warning_critical_logs.append(line)
                
                # [분석 5] 주요 이벤트 요약 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED 포함 여부 확인)
                # event 이름에 감시 대상 키워드가 포함되어 있는지 체크합니다.
                if any(keyword in event for keyword in target_keywords):
                    major_events_summary.append({
                        "timestamp": timestamp,
                        "device": device,
                        "severity": severity,
                        "event": event,
                        "message": message
                    })

    except FileNotFoundError:
        print(f"[오류] '{INPUT_FILE_PATH}' 파일을 찾을 수 없습니다.")
        print("경로가 올바르게 설정되었는지 혹은 샘플 로그 파일이 존재하는지 확인해 주세요.")
        return
    except Exception as e:
        print(f"[오류] 로그를 읽는 동안 문제가 발생했습니다: {e}")
        return

    # 3. 마크다운 보고서 저장 폴더 생성 확인
    # '07_log_analysis_script' 폴더가 없다면 자동으로 만들어 줍니다.
    output_dir = os.path.dirname(OUTPUT_FILE_PATH)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 4. 분석 결과 마크다운(MD) 파일로 내보내기
    try:
        with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as out_file:
            out_file.write("# 데이터 센터(DCO) 교육용 로그 분석 보고서\n\n")
            
            # (1) 전체 로그 요약
            out_file.write("## 1. 전체 로그 요약\n")
            out_file.write(f"- **분석 파일**: `{INPUT_FILE_PATH}`\n")
            out_file.write(f"- **총 분석 대상 라인**: {total_lines}개\n\n")
            
            # (2) 심각도별 통계
            out_file.write("## 2. 심각도(Severity)별 발생 통계\n")
            out_file.write("| 심각도 (Severity) | 빈도 (Count) |\n")
            out_file.write("| :--- | :--- |\n")
            # 알파벳 혹은 정렬된 순서대로 표시합니다.
            for sev, count in sorted(severity_counts.items()):
                out_file.write(f"| {sev} | {count} |\n")
            out_file.write("\n")
            
            # (3) 이벤트별 통계
            out_file.write("## 3. 이벤트(Event)별 통계\n")
            out_file.write("| 이벤트 (Event) | 빈도 (Count) |\n")
            out_file.write("| :--- | :--- |\n")
            # 빈도수가 높은 이벤트가 위에 나오도록 내림차순 정렬하여 출력합니다.
            sorted_events = sorted(event_counts.items(), key=lambda x: x[1], reverse=True)
            for evt, count in sorted_events:
                out_file.write(f"| {evt} | {count} |\n")
            out_file.write("\n")
            
            # (4) WARNING / CRITICAL 로그 목록
            out_file.write("## 4. WARNING 및 CRITICAL 로그 목록\n")
            if warning_critical_logs:
                for idx, log in enumerate(warning_critical_logs, 1):
                    out_file.write(f"{idx}. `{log}`\n")
            else:
                out_file.write("- 해당 항목 없음\n")
            out_file.write("\n")
            
            # (5) 주요 장애 이벤트 요약
            out_file.write("## 5. 주요 인시던트(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) 요약\n")
            if major_events_summary:
                out_file.write("| 발생 일시 | 장비 | 심각도 | 이벤트 유형 | 메시지 |\n")
                out_file.write("| :--- | :--- | :--- | :--- | :--- |\n")
                for item in major_events_summary:
                    out_file.write(
                        f"| {item['timestamp']} | {item['device']} | {item['severity']} | "
                        f"{item['event']} | {item['message']} |\n"
                    )
            else:
                out_file.write("- 대상 키워드와 일치하는 주요 인시던트가 발견되지 않았습니다.\n")
            
        print(f"로그 분석이 완료되었습니다. 보고서가 다음 경로에 생성되었습니다:\n -> {OUTPUT_FILE_PATH}")
        
    except Exception as e:
        print(f"[오류] 보고서 파일을 작성하는 중에 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    analyze_dco_logs()