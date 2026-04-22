import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'githire.settings')
django.setup()

import google.generativeai as genai
from django.conf import settings
from analyzer.services.ai_service import analyze_profile_with_ai

api_key = getattr(settings, 'GEMINI_API_KEY', os.getenv('GEMINI_API_KEY'))
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-flash-latest')

data = {
    'user': {'login': 'torvalds', 'bio': '', 'public_repos': 10, 'followers': 100},
    'languages': {'C': 5},
    'total_stars': 500
}

result = analyze_profile_with_ai(data, 80)
print(result.get('hiring_recommendation'))
print(result.get('summary'))
