from datetime import datetime


def add_logs(message):
    with open('logs/logs.txt','a') as log:
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        log.write(f"[{time}] {message}\n")
    return

def view_logs():
    try:
        with open("logs/logs.txt", "r") as log:
            logs = log.read()

        if logs:
            print("\n========== ACTIVITY LOGS ==========")
            print(logs)
            print("===================================")
        else:
            print("No logs found.")

    except Exception:
        print("Log file does not exist.")