import os
import json
import google.generativeai as genai
from django.conf import settings

def analyze_profile_with_ai(github_data, score):
    # Retrieve Gemini API Key
    api_key = getattr(settings, 'GEMINI_API_KEY', os.getenv('GEMINI_API_KEY'))
    
    prompt = f"""
    Analyze this GitHub profile and provide insights. Use the following data:
    Username: {github_data['user'].get('login')}
    Bio: {github_data['user'].get('bio')}
    Public Repos: {github_data['user'].get('public_repos')}
    Followers: {github_data['user'].get('followers')}
    Total Stars: {github_data['total_stars']}
    Top Languages: {list(github_data['languages'].keys())}
    Calculated Score: {score}/100

    Provide your response strictly as a valid JSON object matching exactly this structure (no markdown fences or extra text):
    {{
        "summary": "2-3 sentence summary evaluating their skills.",
        "strengths": ["string", "string", "string"],
        "weaknesses": ["string", "string"],
        "best_roles": ["string", "string"],
        "hiring_recommendation": "string"
    }}
    """
    
    if api_key:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.0-flash', 
                                          system_instruction="You are an expert technical recruiter and engineering manager. You only output pure JSON format.")
            response = model.generate_content(prompt)
            
            # Clean possible markdown format
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            elif text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
            
            return json.loads(text.strip())
        except Exception as e:
            print(f"DEBUG GEMINI EXCEPTION: {e}")
            pass # Fails safely to fallback
            
    # Dynamic Local Fallback Structure
    top_langs = list(github_data['languages'].keys())[:2]
    lang_str = " and ".join(top_langs) if top_langs else "multiple technologies"
    
    summary = f"Based on the repository analysis, {github_data['user'].get('login')} displays strong proficiency with {lang_str}. With a developer score of {score}/100, they maintain a consistent presence in the open-source ecosystem."
    
    weaknesses_msg = "Provide a free Google Gemini API Key for deep AI insight." if not api_key else "Consider utilizing more descriptive README documentation."
    
    return {
        "summary": summary,
        "strengths": [
            f"Demonstrated experience utilizing {lang_str}",
            f"Maintains a portfolio of {github_data['user'].get('public_repos')} repositories",
            f"Solid architectural footprint with {github_data['total_stars']} total stars earned"
        ],
        "weaknesses": [
            weaknesses_msg,
            "Expand tech stack diversity"
        ],
        "best_roles": [
            "Software Engineer", 
            "Full Stack Developer" if len(top_langs) > 1 else "Backend Developer"
        ],
        "hiring_recommendation": "A capable candidate reflecting stable engineering habits. (Output generated via local algorithm)"
    }
