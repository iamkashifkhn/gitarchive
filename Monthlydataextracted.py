import pandas as pd
import re
import os
import glob

userlist = []

# 'E:\compyvantage\GitArchiveData\February2015'
# path = str(input("Enter the path to the directory: "))
# os.chdir(path)

for file in os.listdir(r'E:\compyvantage\GitArchiveData\February2015'):
    if file.endswith('.json'):
        with open(f'E:\compyvantage\GitArchiveData\February2015\{file}', 'r' , encoding='utf-8') as f:
            for line in f:
                pattern = r'login":"(.*?)"'
                matches = re.findall(pattern, line)
                for match in matches:
                    userlist.append(match)
                    print(match)
userlist = set(userlist)
pd.DataFrame(userlist).to_csv('febUsers.csv', index=False)
print(len(userlist))
    