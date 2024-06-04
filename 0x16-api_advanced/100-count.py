#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively query the Reddit API, parse the titles of all hot articles, and print a sorted count of given keywords.

    Args:
    subreddit (str): The name of the subreddit.
    word_list (list): A list of keywords to count occurrences of.
    after (str): The name of the last post fetched (default is None).
    word_count (dict): A dictionary to store the count of each keyword (default is an empty dictionary).

    Returns:
    None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        if data['data']['children']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for word in word_list:
                    if f" {word.lower()} " in title or title.startswith(f"{word.lower()} ") or title.endswith(f" {word.lower()}") or title == word.lower():
                        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
            after = data['data']['children'][-1]['data']['name']
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")
    else:
        print(None)

# Example usage:
subreddit = "python"
word_list = ['python', 'reddit', 'programming']
print(f"Count of keywords in r/{subreddit}:")
count_words(subreddit, word_list)

