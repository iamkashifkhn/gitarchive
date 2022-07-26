# tup = (['Java', 'Vue', 'JavaScript', 'CSS', 'Dockerfile', 'Shell'])
# print(len(tup))
# for i in range(len(tup)):
#     print(tup[i])
# https://data.gharchive.org/2015-01-01-15.json.gz
import requests
import os
download_dir = 'april_2015'
for date in range(15,31):
    for hours in range(1, 24):
        date = str(date)
        if len(date) == 1:
            date = '0' + date
            # print("this is single digit", hour)
            resp = requests.get(f'https://data.gharchive.org/2015-04-{date}-{hours}.json.gz')
            if resp.ok:
                with open(f'{download_dir}/2015-04-{date}-{hours}.json.gz', 'wb') as f:
                    print("working on", f'2015-04-{date}-{hours}.json.gz')
                    f.write(resp.content)
                    print(f'Downloaded 2015-04-{date}-{hours}.json.gz')
        elif len(date) == 2:
            # print("this is 2nd digit",hour)
            resp = requests.get(f'https://data.gharchive.org/2015-04-{date}-{hours}.json.gz')
            if resp.ok:
                with open(f'{download_dir}/2015-04-{date}-{hours}.json.gz', 'wb') as f:
                    print("working on", f'2015-04-{date}-{hours}.json.gz')
                    f.write(resp.content)
                    print(f'Downloaded 2015-04-{date}-{hours}.json.gz')

            # resp = requests.get(f'https://data.gharchive.org/2015-01-{date}-{hour}.json.gz')
            # if resp.ok:
            #     with open(f'{download_dir}/2015-01-{date}-{hour}.json.gz', 'wb') as f:
            #         f.write(resp.content)
    #     resp = requests.get(f'https://data.gharchive.org/2015-01-{date}-{hours}.json.gz')
    #     if resp.status_code == 200:
    #         with open(os.path.join(download_dir, f'{date}-{hours}.json.gz'), 'wb') as f:
    #             f.write(resp.content)
    # if not os.path.isdir(download_dir):
    #     os.mkdir(download_dir)
    #     with open(f'{download_dir}') as fh:
    #         fh.write(resp.content)
    