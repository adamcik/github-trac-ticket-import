#!/usr/bin/env python

import csv
import json
import urllib

USERNAME = ''
ORGNAME = ''
PROJECT = ''
AUTH_TOKEN = ''
TRAC_URL = 'http://example.com/trac/report/1?format=csv'

if (ORGNAME == ''):
    ORGNAME = USERNAME

github_url = 'https://github.com/api/v2/json/issues/'
csv_data = urllib.urlopen(TRAC_URL)
reader = csv.DictReader(csv_data)
tickets = []

url = github_url + 'list/%s/%s/open' % (ORGNAME, PROJECT)
data = urllib.urlencode({
    'login': USERNAME,
    'token': AUTH_TOKEN,
})
response = urllib.urlopen(url, data)
content = response.read()
issues = json.loads(content)['issues']

for row in reader:
    for key, value in row.items():
        row[key] = row[key].decode('utf-8')

    if filter(lambda i: i['title'] == row['summary'], issues):
        continue

    tickets.append({
        'title': row['summary'],
        'description': row['_description'],
        'tags': [u'ime', row['type'], row['component']],
    })

for ticket in tickets:
    url = github_url + 'open/%s/%s' % (ORGNAME, PROJECT)
    data = urllib.urlencode({
        'login': USERNAME,
        'token': AUTH_TOKEN,
        'title': ticket['title'],
        'body': ticket['description'].encode('utf-8'),
    })

    urllib.urlopen(github_url, data)
    response = urllib.urlopen(url, data)
    content = response.read()

    try:
        issue = json.loads(content)['issue']
    except KeyError:
        raise Exception(content)

    data = urllib.urlencode({
        'login': USERNAME,
        'token': AUTH_TOKEN,
    })

    for tag in ticket['tags']:
        url = github_url + 'label/add/%s/%s/%s/%s' % (
            ORGNAME, PROJECT, tag, issue['number'])
        urllib.urlopen(url, data)
