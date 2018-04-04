import matplotlib.pyplot as plt
import json

# l = list(range(0, 11))
# ltwo = [x ** 2 for x in l]
# b = list(range(0, 11))
# bthree = [x ** 3 for x in b]
#
# plt.plot(l, ltwo, b, bthree)
# plt.show()

with open('C:/Users/ccrud/PycharmProjects/reddit_bot/praw_post_growth/Files/scores.json', 'r') as f:
    data = json.load(f)

csv_data = []

for id in data:
    inner_x = []
    inner_y = []
    for dp in data[id]:
        if dp != '0':
            inner_x.append(data[id][dp][1])
            inner_y.append(data[id][dp][0])
    plt.plot(inner_x, inner_y)

plt.show()

