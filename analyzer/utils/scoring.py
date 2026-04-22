def calculate_score(github_data):
    user = github_data.get('user', {})
    languages = github_data.get('languages', {})
    total_stars = github_data.get('total_stars', 0)
    
    score = 0
    
    # 1. Profile Completeness (max 15 pts)
    if user.get('name'): score += 5
    if user.get('bio'): score += 5
    if user.get('company') or user.get('blog') or user.get('location'): score += 5
        
    # 2. Repo Count (max 20 pts)
    public_repos = user.get('public_repos', 0)
    if public_repos >= 50:
        score += 20
    elif public_repos >= 20:
        score += 15
    elif public_repos >= 5:
        score += 10
    elif public_repos > 0:
        score += 5
        
    # 3. Stars (max 30 pts)
    if total_stars > 500:
        score += 30
    elif total_stars > 100:
        score += 25
    elif total_stars > 50:
        score += 20
    elif total_stars > 10:
        score += 10
    elif total_stars > 0:
        score += 5
        
    # 4. Followers (max 15 pts)
    followers = user.get('followers', 0)
    if followers > 100:
        score += 15
    elif followers > 20:
        score += 10
    elif followers > 0:
        score += 5
        
    # 5. Language Diversity (max 20 pts)
    lang_count = len(languages)
    if lang_count >= 5:
        score += 20
    elif lang_count >= 3:
        score += 15
    elif lang_count >= 1:
        score += 10
        
    return min(100, score)
