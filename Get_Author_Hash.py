from git import Repo
from datetime import datetime
from operator import itemgetter
import time
import os
import urllib.request
import zipfile
import sys
import re

YEAR = 0
WEEK = 1
DAY = 2
TIME = 3
SHA = 4
DATE = 5
AUTHOR = 6

repo = Repo('D:/sonarqube/projects/cassandra-dtest')
commits = list(repo.iter_commits('master'))

commits_in_week = {}
list_allweek = []
list_eachday = []
for each in commits:
    each_time = datetime.fromtimestamp(each.committed_date)
    each_date = datetime.date(each_time)
    each_hour = datetime.time(each_time)
    hash = each.hexsha
    author = each.author

    list_each = [each_time.isocalendar()[YEAR], each_time.isocalendar()[WEEK], each_time.isocalendar()[DAY], each_hour,
                 hash, each_date, author]
    list_allweek.append(list_each)

list_allweek.sort(key=itemgetter(YEAR, WEEK, DAY, TIME))
len_list_allweek = len(list_allweek)

list_eachday.sort(reverse=False)
for each in list_eachday:
    print(each)

i = 0

while i + 1 < len_list_allweek:
    if ((list_allweek[i][YEAR] == list_allweek[i + 1][YEAR]) and (list_allweek[i][WEEK] == list_allweek[i + 1][WEEK])):
        list_allweek.pop(i)
        len_list_allweek -= 1
    else:
        i += 1

counter = 0

for each in list_allweek:
    print(each)
    commit_hash = str(each[SHA])
    commit_author = str(each[AUTHOR])

    author_all = repr(each[AUTHOR])
    author = str(author_all)
    commit_email = re.split('<|>',author)[-3]
    print(commit_email)

    print(author)
#    print(commit_hash,commit_author)
