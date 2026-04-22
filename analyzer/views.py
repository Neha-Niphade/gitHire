from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SearchHistory, Report
from .services.github_service import fetch_github_profile
from .services.ai_service import analyze_profile_with_ai
from .utils.scoring import calculate_score

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            SearchHistory.objects.create(
                user=request.user if request.user.is_authenticated else None,
                github_username=username
            )
            return redirect('report', username=username)
    
    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]
    return render(request, 'index.html', {'recent_searches': recent_searches})

def report(request, username):
    github_data = fetch_github_profile(username)
    if not github_data:
        messages.error(request, f"Could not find GitHub user: {username}")
        return redirect('index')
        
    score = calculate_score(github_data)
    ai_insights = analyze_profile_with_ai(github_data, score)
    
    report_obj, created = Report.objects.update_or_create(
        github_username=username,
        defaults={
            'score': score,
            'ai_summary': ai_insights.get('summary', ''),
            'raw_data_json': {
                'github_data': github_data,
                'ai_insights': ai_insights
            }
        }
    )
    
    context = {
        'github_data': github_data,
        'github_user': github_data['user'],
        'repos': github_data['repos'][:5],
        'languages': github_data['languages'],
        'total_stars': github_data['total_stars'],
        'score': score,
        'ai': ai_insights,
        'report_obj': report_obj
    }
    
    return render(request, 'report.html', context)
