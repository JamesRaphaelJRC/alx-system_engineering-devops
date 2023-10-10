#!/usr/bin/python3
''' Querries the Reddit API '''
import requests


def top_ten(subreddit):
    ''' Prints the titles of the first 10 hot posts listed for  given subreddit
    '''
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"USer-Agent": "MyALXAdvancedAPiProjectBot (by /u/jamesrc)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()['data']['children']
        i = 0
        for i in range(10):
            print(response[i]['data'].get('title'))
    else:
        print('None')
