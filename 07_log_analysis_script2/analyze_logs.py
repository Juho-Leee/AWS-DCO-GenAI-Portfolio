#!/usr/bin/env python3
"""
Log analysis script to count the occurrences of CRC error and Link Down
per server from server*.log files.
"""

import glob
import os
import re

def analyze_server_logs(file_pattern="server*.log"):
    # Find all log files matching the pattern
    log_files = sorted(glob.glob(file_pattern))
    
    if not log_files:
        print("No log files matching pattern 'server*.log' found in the current directory.")
        return
    
    results = {}
    
    # Regex patterns for matching
    # We look for lines containing 'ERROR' level and the specific error term
    crc_pattern = re.compile(r'\bcrc\s+error\b', re.IGNORECASE)
    link_down_pattern = re.compile(r'\blink\s+down\b', re.IGNORECASE)
    
    for file_path in log_files:
        # Extract server name from filename (e.g. server01 from server01.log)
        server_name = os.path.splitext(os.path.basename(file_path))[0]
        
        crc_errors = 0
        link_downs = 0
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Check for ERROR level log entries
                # This prevents counting INFO messages like "CRC error recovered"
                if "ERROR" in line:
                    if crc_pattern.search(line):
                        crc_errors += 1
                    if link_down_pattern.search(line):
                        link_downs += 1
                        
        results[server_name] = {
            "crc_errors": crc_errors,
            "link_downs": link_downs
        }
        
    # Print the formatted results
    print("====================================================")
    print("             Server Log Analysis Results            ")
    print("====================================================")
    print(f"{'Server Name':<15} | {'CRC Error Count':<15} | {'Link Down Count':<15}")
    print("-" * 52)
    for server, counts in results.items():
        print(f"{server:<15} | {counts['crc_errors']:<15} | {counts['link_downs']:<15}")
    print("====================================================")

if __name__ == "__main__":
    analyze_server_logs()
