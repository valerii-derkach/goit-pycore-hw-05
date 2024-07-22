import sys
from servise import load_logs, count_logs_by_level, display_log_counts, filter_logs_by_level

def main():
    if len(sys.argv) < 2:
        print("Використовуйте наступний формат: python main.py <path_to_log_file>(logs.txt) [log_level](optional)")
        return
    
    try:
      file_path = sys.argv[1]
      log_level = sys.argv[2] if len(sys.argv) > 2 else None

      logs = load_logs(file_path)
      counts = count_logs_by_level(logs)
      display_log_counts(counts)

      if log_level:
          filtered_logs = filter_logs_by_level(logs, log_level)
          print(f"\nДеталі логів для рівня '{log_level.upper()}':\n")
          for log in filtered_logs:
              print(f"{log['date']} {log['time']} - {log['message']}")
    
    except Exception as e:
        print(f"Виникла помилка під час обробки логів: {e}")

if __name__ == "__main__":
    main()