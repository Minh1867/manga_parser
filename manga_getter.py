import requests

subreddit = 'manga'
limit = 100
timeframe = 'week'
listing = 'new'
file_name = 'last-post.txt'
last_id = ''

with open(file_name, 'r') as file:
    last_id = file.read()

## Makes a get request to reddit
def get_reddit(subreddit, listing, limit, timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'MangaBot'})
    except:
        print('Error with get request')
    
    return request.json()

# Parses a json for post info
def get_post_info(r):
    post_info = {}
    for post in r['data']['children']:
        data = post['data']
        if data['link_flair_text'] == 'DISC':
            print(data['id'])
            post_info[data['title']] = {'url': data['url'], 'score': data['score']}
    
    return post_info


if __name__ == '__main__':
    r = get_reddit(subreddit, listing, limit, timeframe)
    info = get_post_info(r)

    print(f'Posts found: {len(info)}')

    for key, value in info.items():
        print(f'Title: {key}')
        print(f'URL: {value["url"]}')
        print(f'Score: {value["score"]}')

        
    
