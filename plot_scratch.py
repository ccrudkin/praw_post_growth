import matplotlib.pyplot as plt
import json
import os

# l = list(range(0, 11))
# ltwo = [x ** 2 for x in l]
# b = list(range(0, 11))
# bthree = [x ** 3 for x in b]
#
# plt.plot(l, ltwo, b, bthree)
# plt.show()

with open(os.getcwd() + '/Files/scores.json', 'r') as f:
    data = json.load(f)

csv_data = []

for id in data:
    inner_x = []
    inner_y = []
    for dp in data[id]:
        if dp != '0':
            inner_x.append(data[id][dp][1])
            inner_y.append(data[id][dp][0])
    lines = plt.plot(inner_x, inner_y)
    plt.setp(lines, linewidth=2.0)

plt.title('Karma over time for 100 r/mildlyinteresting posts')
plt.axis([0, 1100, 0, 100000])  # to visualize the little guys.
plt.xticks(range(0, 1200, 60))
plt.ylabel('Karma')
plt.xlabel('Post age (minutes)')
plt.show()

