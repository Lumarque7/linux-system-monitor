from datetime import datetime
import platform
import subprocess

print("=== SYSTEM MONITOR ===")
print("Date:", datetime.now())
print("Hostname:", platform.node())

commands = {
    "UPTIME": ["uptime"],
    "MEMORY": ["free", "-h"],
    "DISK": ["df", "-h", "/"]
}

for title, command in commands.items():
    print(f"\n=== {title} ===")
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    print(result.stdout)


