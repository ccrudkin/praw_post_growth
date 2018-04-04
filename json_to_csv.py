import json
import csv

with open('C:/Users/ccrud/PycharmProjects/reddit_bot/praw_post_growth/Files/scores.json', 'r') as f:
    data = json.load(f)

csv_data = [['Submission ID', 'Age (minutes)', 'Karma']]

for id in data:
    for dp in data[id]:
        if dp != '0':
            csv_data.append([id, data[id][dp][1], data[id][dp][0]])

with open('C:/Users/ccrud/PycharmProjects/reddit_bot/karma_temp.csv', 'w', newline='') as c:
    outputwriter = csv.writer(c)
    for line in csv_data:
        outputwriter.writerow(line)


