from django.contrib import admin
from .models import SearchHistory, Report, SavedProfile, Feedback

admin.site.register(SearchHistory)
admin.site.register(Report)
admin.site.register(SavedProfile)
admin.site.register(Feedback)
