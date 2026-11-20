"""
INTERMEDIATE | Topic: Structural Pattern Matching (match-case, Python 3.10+)
Notes: Clean alternative to long elif chains for exact value matching.
"""

http_status = 404

match http_status:
    case 200:
        print("200 OK: Request succeeded.")
    case 403 | 404:
        print("Client Error: Resource forbidden or not found.")
    case 500:
        print("500 Internal Server Error.")
    case _:
        print("Unhandled status code.")