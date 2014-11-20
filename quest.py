import json
import time

f = open("quests.json")
allQuests = json.loads(f.read())

currTime = time.time()
availQuests = []
for q in list(allQuests):
	if q['endTime'] > currTime:
		availQuests.append(q)

str = json.dumps(availQuests, indent=4)
print(str)
