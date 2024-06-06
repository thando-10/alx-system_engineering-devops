#!/usr/bin/python3


import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("No posts match or the subreddit is invalid.")
        return

    data = response.json()
    children = data['data']['children']

    for child in children:
        title = child['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                counts[word.lower()] = counts.get(word.lower(), 0) + 1

    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

# Example usage:
count_words("python", ["python", "java", "javascript", "reddit"])

