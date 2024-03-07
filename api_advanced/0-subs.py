#!/usr/bin/python3
""" Return the number of subscribers """


import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ Return  subscribers"""
    if len(sys.argv) < 2:
        return 0
    else:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0"}
        result = requests.get(url, headers=headers, allow_redirects=False)
        if result.status_code != 200:
            return 0
        body = json.loads(result.text)
        return body["data"]["subscribers"]