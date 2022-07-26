import json
import pandas as pd
import os

tweets = []
users = []
errorlist = []
for file in os.listdir('January2015/'):
    if file.endswith('.json'):
        for line in open(f'january2015/{file}' , encoding='utf-8'):
            print("Working on file: ", file)
            tweet = json.loads(line)
            tweets.append(tweet)

for username in tweets:
    if 'actor' in username:
        # users.append(username['actor']['login'])
        users.append(username['actor']['login'])
        print(username['actor']['login'])
    else:
        errorlist.append("Hello")
gitusers = set(users)
df = pd.DataFrame(gitusers)
df.to_csv('jan2015-21-07.csv', index=False)
# dict1 = json.dumps(gitusers)
# # print(dict1)
# with open("jan2015-1.json", "w") as outfile:
#     outfile.write(dict1)
# print(len(users))
        # users.append(username['actor'])
# for i in range(0,len(tweets)):
#     if 'actor' in tweets[i]:
#         # print(tweets[i]['actor']['login'])
#         users.append((tweets[i]['actor']))
#     else:
#         pass
# setofusers = set(users)
# print(len(setofusers))
# print(len(users))
# print(tweets[1]['actor']['login'])
# print(tweets)
