import os
from typing import List, Any

import csv

list_issue = []
list_commit = []
file_name = r'airavata-django-portal'
csv_file = open(r'D:\PhD Groningen\data\New work\experiment' + '\\'+ file_name + r'.csv')

file_author = file_name + r'_author'
csv_author = open(r'D:\PhD Groningen\data\New work\experiment' + '\\'+ file_author + r'.csv')


csv_issue = csv.reader(csv_file)
csv_commit = csv.reader(csv_author)

for row_issue in csv_issue:
    list_issue.append(row_issue)

print(len(list_issue))


for row_commit in csv_commit:
    list_commit.append(row_commit)
print(len(list_commit))



#for row_issue in csv_issue:
#    for row_commit in csv_commit:

i = 0

while i + 1 < len(list_issue):
    j = 0
    while j + 1 < len(list_commit):

        if (list_issue[i][8] == list_commit[j][2]):
            print(list_commit[j][0])
            #print(list_commit[j][1])
            i+=1
        else:
            j+=1



csv_file.close()
csv_author.close()



