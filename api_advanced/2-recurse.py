#!/usr/bin/python3
"""Script that fetch all hot post for a given subreddit with recursive call."""

import requests

headers = {'User-Agent': 'MyAPI/0.0.1'}


def recurse(subreddit, after="", hot_list=[], page_counter=0):
    """Return all hot posts in a subreddit."""

    subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)

    parameters = {'limit': 100, 'after': after}
    response = requests.get(subreddit_url, headers=headers, params=parameters)

    if response.status_code == 200:
        json_data = response.json()
        # get the 'after' value from the response to pass it on the request

        # get title and append it to the hot_list
        for child in json_data.get('data').get('children'):
            title = child.get('data').get('title')
            hot_list.append(title)

        # variable after indicates if there is data on the next pagination
        # on the reddit API after holds a unique name for that subreddit page.
        # if it is None it indicates it is the last page.
        after = json_data.get('data').get('after')
        if after is not None:

            page_counter += 1
            # print(len(hot_list))
            return recurse(subreddit, after=after,
                           hot_list=hot_list, page_counter=page_counter)
        else:
            return hot_list

    else:
        return None


if __name__ == '__main__':
    print(recurse("zerowastecz"))
