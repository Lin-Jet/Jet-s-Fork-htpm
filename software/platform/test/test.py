#!/usr/bin/env python3

import requests
from datetime import datetime
import pytz

print("teams: ")
r = requests.post(
	"http://127.0.0.1:8080/api/manage/teams",
	data={"action": "create", "name": "foo", "password": "bar"}
)
print(r.status_code)
print(r.content)

r = requests.post(
	"http://127.0.0.1:8080/api/manage/players",
	data={"action": "create", "team": 1, "name": "John Doe"}
)
print(r.status_code)
print(r.content)

r = requests.get(
	"http://127.0.0.1:8080/api/manage/players",
)
print(r.status_code)
print(r.content) 

r = requests.post(
	"http://127.0.0.1:8080/api/manage/players",
	data={"action": "update", "team": 1, "name": "John Doe",
		"newTeam": 2, "newName": "Jane Doe"}
)
print(r.status_code)
print(r.content)

# r = requests.post(
# 	"http://127.0.0.1:8080/api/manage/players",
# 	data={"action": "delete", "team": 2, "name": "Jane Doe"}
# )
# print(r.status_code)
# print(r.content)

print("challenges")

r = requests.post(
	"http://127.0.0.1:8080/api/manage/challenges",
	data={"action": "create", "points": 30, "title": "test challenge", "instructions": "this is a test challenge instruction"}
)
print(r.status_code)
print(r.content)

r = requests.get(
	"http://127.0.0.1:8080/api/manage/challenges",
)
print(r.status_code)
print(r.content) 

r = requests.post(
	"http://127.0.0.1:8080/api/manage/challenges",
	data={"action": "update", "points": 30, "title": "test challenge", "instructions": "this is a test challenge instruction",
	"newPoints": 50, "newTitle": "test challenge updated", "newInstructions": "this is a test challenge instruction but updated"}
)
print(r.status_code)
print(r.content)

# r= requests.post(
# 	"http://127.0.0.1:8080/api/manage/challenges",
# 	data={"action": "delete", "points": 30, "title": "test challenge", "instructions": "this is a test challenge instruction"}
# )
# print(r.status_code)
# print(r.content)

print("solves: ")

pacific = pytz.timezone('America/Los_Angeles')

timestamp = datetime.utcnow().strftime('%m-%d-%Y %H:%M')
timestamp = pacific.localize(datetime.strptime(timestamp, '%m-%d-%Y %H:%M'))  # Convert the timestamp to PDT
r = requests.post(
    "http://127.0.0.1:8080/api/manage/solves",
    data={"action": "create", "team": 1, "challenge": "test challenge updated", "timestamp": timestamp}
)
print(r.status_code)
print(r.content)

timestamp = datetime.utcnow().strftime('%m-%d-%Y %H:%M')
timestamp = pacific.localize(datetime.strptime(timestamp, '%m-%d-%Y %H:%M'))
r = requests.post(
    "http://127.0.0.1:8080/api/manage/solves",
    data={"action": "update", "team": 1, "challenge": "test challenge updated", "timestamp": timestamp,
    "newTeam": 1, "newChallenge": "test challenge with updated solve", "newTimestamp": timestamp
    }
)
print(r.status_code)
print(r.content)


print("/api/info: ")

r = requests.get(
	"http://127.0.0.1:8080/api/info",
)
print(r.status_code)
print(r.content) 