import json
import re

file = 'ReplayCodeWallsRaw.txt'
with open(file, "r") as data_file:
    data = data_file.read()
pattern = "(?s)g_gamelogs\s*=\s*(\{.*?\})\n;"
moves = re.findall(pattern, data)
data = json.loads(moves[0])
mlist = list()
for item in data["data"]["data"]:
    ptype = item["data"][0]['type']
    if((ptype == 'playToken') or (ptype == 'playWall')):
        mlist.append(item["data"][0]["args"]["quoridorstrats_notation"])
        # print(item["data"][0]["args"]["player_name"]+ ":")
        # print(item["data"][0]["args"]["quoridorstrats_notation"])
i = 0
for play in mlist:
    if(i > 0):
        print ", ",
    print play,
    i = i + 1
