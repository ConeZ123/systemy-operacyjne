 #!/usr/bin/env python3

import os

print("USER PID COMMAND")

for pid in os.listdir('/proc'):
    if pid.isdigit():
        with open(f"/proc/{pid}/status") as f:
            for line in f:
                if line.startswith("Uid: "):
                    uid = line.split()[1]
                    break
        
        with open(f"/proc/{pid}/comm") as f:
            comm = f.readline()

        user = pid
        with open(f"/etc/passwd") as f:
            for line in f:
                parts = line.split(":")
                if parts[2] == pid:
                    user = parts[0]
                    break
        print(user, pid, comm)