import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'githire.settings')
django.setup()

import google.generativeai as genai
from django.conf import settings

api_key = getattr(settings, 'GEMINI_API_KEY', os.getenv('GEMINI_API_KEY'))
genai.configure(api_key=api_key)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
