# logger.py

import json
import os
from datetime import datetime

LOG_FILE = "hogwarts_log.json"

def log_event(event_type, details):
    log_entry = {
        "Timestamp": datetime.now().isoformat(),
        "Event_Type": event_type,
        "Details": details
    }
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            json.dump([log_entry], f, indent=4)
    else:
        with open(LOG_FILE, 'r+') as f:
            data = json.load(f)
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=4)
