# TODO: Check privacy of Git uploads; put files back where they belong to avoid breaking things.
# TODO: organize repository while script isn't running. See ^^^

import praw
import time
from time import sleep
import os
import json

cwd = os.getcwd()
with open(cwd + '/Files/config.json', 'r') as c:
    config = json.load(c)
reddit = praw.Reddit(client_id=config['client_id'],
                     client_secret=config['client_secret'],
                     user_agent=config['user_agent'])

subreddit = reddit.subreddit('mildlyinteresting')
harvests = 0
submission_dict = {}
# Internal format: 'post_id_nnn': {'datapoint_nnn': [score, age]}
# NOTE: for 'post_id_nnn'[0], age == created (time in seconds UTC); exclude from data analysis

for submission in subreddit.new(limit=100):  # up to 1000
    submission_dict[submission.id] = {}
    submission_dict[submission.id][0] = [submission.score, submission.created]
    # print(dir(submission))  # for debugging and finding possible methods
    # break


def get_age(created):
    age = (time.time() - created + (8 * 3600)) / 60  # correct for TZ and convert to minutes
    # clean up by using module methods to get correct TZ
    return age


def score_age(dict, datapoint):  # datapoint is a rolling count for each collection iteration
    for post in dict:
        dict[post][datapoint] = [reddit.submission(id=post).score, round(get_age(
            submission_dict[post][0][1]), 2)]


while harvests < 144:  # Multiply by sleep duration for total harvest window.
    harvests += 1
    print('Harvest no.: {}'.format(harvests))
    score_age(submission_dict, harvests)
    with open(cwd + '/Files/scores.json', 'w') as f:
        json.dump(submission_dict, f)
    sleep(295)  # Time between harvests (here, 5 minutes minus est. fetch time)


# print(submission_dict)
# for each in submission_dict:
#     print(each)
#     for data in submission_dict[each]:
#         print(data, submission_dict[each][data])
#     print()
# ^ make data human-readable for debugging
