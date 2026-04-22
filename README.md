# GitHire AI

An AI-powered GitHub profile analyzer built with Django, Tailwind CSS, and gemini.

## Features
- Search any GitHub username
- Fetch profile and repository statistics via GitHub API
- Calculate a practical 0-100 Developer Score
- Advanced AI insights, strengths, weaknesses, and best-fit roles via gemini
- Beautiful Shareable Dashboard with interactive charts

## Tech Stack
- Python 3 / Django 6
- MySQL (Fallback to SQLite)
- Tailwind CSS
- Chart.js
- Gemini API
- GitHub REST API

## Getting Started

### 1. Prerequisites
- Python 3.10+
- MySQL Server

### 2. Setup Database
Create a MySQL database:
```sql
CREATE DATABASE githire CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/githire.git
cd githire

# Create virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate
# Activate it (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the project root containing:
```env
SECRET_KEY=your-secret-key
DEBUG=True

# MySQL Config
DB_NAME=githire
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=3306

# API Keys
GITHUB_TOKEN=your_github_token
GEMINI_API_KEY=your_gemini_api_key
```

*Note: If `DB_NAME` is omitted, the app will automatically fall back to local SQLite.*

### 5. Running the Application
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver
```
Visit http://127.0.0.1:8000 to use GitHire AI!
