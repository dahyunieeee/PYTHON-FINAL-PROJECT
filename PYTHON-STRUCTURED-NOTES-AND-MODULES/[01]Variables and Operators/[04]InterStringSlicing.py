"""
INTERMEDIATE | Topic: String Methods & Slicing
Notes: Syntax is text[start:stop:step]. Strings are immutable.
"""

raw_id = "  bsit-1b-2026  "
clean_id = raw_id.strip().upper()

course = clean_id[0:4]      # "BSIT"
section = clean_id[5:7]     # "1B"
reversed_id = clean_id[::-1]

print(f"Clean: {clean_id} | Course: {course} | Section: {section} | Rev: {reversed_id}")