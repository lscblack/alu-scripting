#!/usr/bin/python3
"""Print the titles of the first 10Hot Posts"""
import requests


def top_ten(subreddit):
    """The top ten titles"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(
                    json_data.get('data')
                    .get('children')[i]
                    .get('data')
                    .get('title')
                )
    else:
        print(None)
