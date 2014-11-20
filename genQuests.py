import json
import time
import random

currTime = time.time()

allQuests = []
allQuests.append({'desc' : "do 100 push ups"})
allQuests.append({'desc' : "do 200 push ups"})
allQuests.append({'desc' : "do 300 push ups"})
allQuests.append({'desc' : "do 400 push ups"})

quests = []

for idx in range(0, 10):
	num = int(currTime*idx)%(len(allQuests))
	q = allQuests[num]
	q['startTime'] = currTime
	q['endTime'] = (currTime)+10*random.random()
	quests.append(q)

str = json.dumps(quests)
print(str)
