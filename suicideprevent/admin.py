from django.contrib import admin
from .models import Mood, MoodTracker

# Register your models here.
admin.site.register(Mood)
admin.site.register(MoodTracker)

