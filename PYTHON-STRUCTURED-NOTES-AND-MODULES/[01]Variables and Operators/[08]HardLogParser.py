"""
HARD | Topic: String Indexing & Extraction Pipeline
Notes: Extracts structured fields from a raw log string using find() and slicing.
"""

log_entry = "[2026-11-20 15:00] USER=bsit_student STATUS=200"

ts_start = log_entry.find("[") + 1
ts_end = log_entry.find("]")
timestamp = log_entry[ts_start:ts_end]

user_start = log_entry.find("USER=") + 5
user_end = log_entry.find(" STATUS=")
username = log_entry[user_start:user_end]

status_code = int(log_entry[log_entry.find("STATUS=") + 7:])
print(f"Time: {timestamp} | User: {username} | OK: {status_code == 200}")