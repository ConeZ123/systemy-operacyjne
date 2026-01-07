#!/usr/bin/env python3

import sys
import time

file = sys.argv[1]

with open(file, "w") as f:
       i = 0 
       while True:
              f.write(f"{i}\n")
              f.flush()
              i+=1
              time.sleep(1)
