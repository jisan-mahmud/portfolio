import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def github_data():
    url = 'https://api.github.com/users/jisan-mahmud'
    token = os.getenv('github_access_token')
    headers = {
        'Authorization': f'token {token}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        created_at = datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        context = {
            'name': data['name'],
            'image': data['avatar_url'],
            'username': data['login'],
            'bio': data['bio'],
            'joining_date': created_at.strftime('%d %b %Y'),
            'repos': data['public_repos'],
            'followers': data['followers'],
            'following': data['following'],
        }
        return context
    else:
        return 0
    
github_data()