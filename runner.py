#!/usr/bin/python3

import subprocess as sp
import sys
from difflib import ndiff

code_path = sys.argv[1]
expected_output_path = sys.argv[2]
p = sp.run(["python3", code_path], capture_output=True, check=True)

output_str = p.stdout.decode("utf-8").splitlines()
with open(expected_output_path, "r") as file:
    a = [l.strip() for l in output_str]
    b = [l.strip() for l in file]
    for d in ndiff(a, b):
        if d[0] != " ":
            print(d)
