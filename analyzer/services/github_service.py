import requests
import os
from django.conf import settings

def fetch_github_profile(username):
    headers = {}
    token = getattr(settings, 'GITHUB_TOKEN', os.getenv('GITHUB_TOKEN'))
    if token:
        headers['Authorization'] = f'token {token}'
        
    user_url = f'https://api.github.com/users/{username}'
    repos_url = f'https://api.github.com/users/{username}/repos?per_page=100&sort=updated'

    user_response = requests.get(user_url, headers=headers)
    
    if user_response.status_code != 200:
        return None
        
    user_data = user_response.json()
    
    repos_response = requests.get(repos_url, headers=headers)
    repos_data = repos_response.json() if repos_response.status_code == 200 else []
    
    # Process basic aggregate data
    languages = {}
    total_stars = 0
    
    for repo in repos_data:
        lang = repo.get('language')
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
        total_stars += repo.get('stargazers_count', 0)
        
    top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        'user': user_data,
        'repos': repos_data,
        'languages': dict(top_languages),
        'total_stars': total_stars
    }
