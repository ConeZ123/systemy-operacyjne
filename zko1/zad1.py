#!/usr/bin/env python3
import os
import pwd

def list_processes():
       for pid in os.listdir('/proc'):
              if pid.isdigit():
                     status = f"/proc/{pid}/status"
                     comm = f"/proc/{pid}/comm"

                     with open(status) as file:
                            for line in file:
                                if line.startswith('Uid:'):
                                    uid = int(line.split()[1])
                                    break
                            user = pwd.getpwuid(uid).pw_name

                     with open(comm) as file:
                            comm = file.read().strip()

                     print(user, pid, comm)

if __name__ == "__main__":
    print("USER PID COMMAND")
    list_processes()