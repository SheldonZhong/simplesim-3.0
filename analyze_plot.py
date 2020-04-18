#!/usr/bin/env python
import re
import matplotlib.pyplot as plt

regex = re.compile(r'(\d+)-th 5 million cycles:\s*(\d+\.\d{4})')

x = []
y = []

with open("./equake.stdout", "r") as output:
    for line in output:
        line_result = regex.search(line)
        x.append(int(line_result.group(1)))
        y.append(float(line_result.group(2)))

plt.plot(x, y)
plt.xlabel('i-th 5 million cycles')
plt.ylabel('IPC value')
plt.title('Variation of IPC value with window size 5 million cycles')

plt.grid()
plt.savefig("proj2-fig.png", dpi=300)
