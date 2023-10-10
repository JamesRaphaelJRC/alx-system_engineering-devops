#!/usr/bin/python3
''' Querries the Reddit API '''
import requests


def top_ten(subreddit):
    ''' Prints the titles of the first 10 hot posts listed for  given
        subreddit
    '''
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"USer-Agent": "MyALXAdvancedAPiProjectBot (by /u/jamesrc)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts[:10]:
            print(post['data'].get('title'))
    else:
        print('None')
