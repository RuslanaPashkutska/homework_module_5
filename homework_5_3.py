import os
import sys
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None
    return {"date": parts[0], "time": parts[1], "level": parts[2].upper(), "message": parts[3]}

def load_logs(file_path: str) -> list:
    file_path = os.path.expanduser(file_path)
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [log for line in file if (log := parse_log_line(line))]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: No permission to read the file '{file_path}'.")
        sys.exit(1)
    except Exception as e:
        print (f'Error reading file: {e}')
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] +=1
    return dict(counts)

def display_log_counts(counts: dict):
    print("\nLog Level  | Count")
    print("-----------|---------")
    for level in sorted(counts.keys()):
        print(f"{level:<10} | {counts[level]:<9}")

def main():
    # if len(sys.argv) < 2:
    #    print("Usage: python script.py <logfile_path> [log_level]")
    #   sys.exit(1)

    file_path = "/Users/ruslana/Desktop/homework_module_5/logfile.log"
    print(f"Trying to open: {file_path}")
    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nLog details for level '{level}':")
        if filtered_logs:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"No logs found for level '{level}'")

if __name__ == "__main__":
    main()
