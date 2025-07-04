import json
from datetime import datetime
import os

LOG_FILE = "static/docs/logs.json"

def pseudonymize_data(data: dict) -> dict:
    """
    Pseudonymize sensitive fields (email/IP).
    """
    result = {}
    for key, value in data.items():
        if "@" in value:  # likely an email
            local, domain = value.split("@")
            result[key] = local[:4] + "****@" + domain
        elif value.count(".") == 3:  # likely an IP address
            result[key] = ".".join(value.split(".")[:2]) + ".***.***"
        else:
            result[key] = value[0] + "****" + value[-1]
    log_action("pseudonymize", data)
    return result

def delete_data(data: dict) -> dict:
    """
    Simulate deletion by returning masked values.
    """
    result = {key: "❌ [deleted]" for key in data}
    log_action("delete", data)
    return result

def log_action(action_type: str, data: dict):
    """
    Log actions to a JSON file with timestamp.
    """
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    log_entry = {
        "action": action_type,
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"[Log Error] {e}")

def get_logs() -> list:
    """
    Retrieve all logs safely, ignoring bad lines.
    """
    logs = []
    if not os.path.exists(LOG_FILE):
        return logs
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                if line.strip():
                    try:
                        logs.append(json.loads(line.strip()))
                    except json.JSONDecodeError:
                        continue
    except Exception as e:
        print(f"[Read Error] {e}")
    return logs
