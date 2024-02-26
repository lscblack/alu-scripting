#!/usr/bin/python3
"""A script that counts the number of occurrences of list of words
in a given subreddit."""

from audioop import reverse
import requests

headers = {'User-Agent': 'MyAPI/0.0.1'}


def count_words(subreddit, word_list, after="", hot_list=[]):
    """print the sorted count of word_list."""

    subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)

    parameters = {'limit': 100, 'after': after}
    response = requests.get(subreddit_url, headers=headers, params=parameters)

    if response.status_code == 200:

        # print(response.status_code)
        json_data = response.json()
        if (json_data.get('data').get('dist') == 0):
            return
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
            # print("got next page")
            # print(len(hot_list))
            return count_words(subreddit, word_list,
                               after=after, hot_list=hot_list)
        else:
            # put the initial words counter dictionary
            counter = {}
            for word in word_list:
                word = word.lower()
                if word not in counter.keys():
                    counter[word] = 0
                else:
                    counter[word] += 1
            # loop through the hot_list to check if word is found in the list
            for title in hot_list:
                title_list = title.lower().split(' ')
                for word in counter.keys():
                    search_word = "{}".format(word)
                    if search_word in title_list:
                        counter[word] += 1
            sorted_counter = dict(
                sorted(counter.items(),
                       key=lambda item: item[1], reverse=True))
            for key, value in sorted_counter.items():
                if value > 0:
                    print("{}: {}".format(key, value))
            # print(hot_list)

    else:
        return


if __name__ == '__main__':
    count_words("hello", ['REDDIT', 'german', 'HI', 'whynot'])
    count_words('unpopular', ['down', 'vote', 'downvote',
                              'you', 'her', 'unpopular', 'politics'])
    # count_words("hello", ['hello', 'hello', 'hello'])
    # count_words("unpopular", ["react", "python", "java",
    # "javascript", "scala", "no_result_for_this"])

    # count_words('hello', ['hello', 'hello', 'hello'])
