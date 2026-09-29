"""Local identifiers and spreadsheet-safe CSV handling. No device access."""
import csv
import re

def safe_identifier(value):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", value):
        raise ValueError("Use 1–64 letters, digits, underscores or hyphens; no names or paths.")
    return value

def spreadsheet_safe(value):
    if not isinstance(value, str): return value
    candidate = value.lstrip()
    # Keep generated signed numeric measurements machine-readable.
    if re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", value): return value
    if candidate.startswith(("=", "+", "-", "@")) or value.startswith(("\t", "\r", "\n")):
        return "'" + value
    return value

class _SafeWriter:
    def __init__(self, stream, *args, **kwargs): self.writer = csv.writer(stream, *args, **kwargs)
    def writerow(self, row): return self.writer.writerow([spreadsheet_safe(value) for value in row])
    def writerows(self, rows):
        for row in rows: self.writerow(row)

def safe_csv_writer(stream, *args, **kwargs): return _SafeWriter(stream, *args, **kwargs)
