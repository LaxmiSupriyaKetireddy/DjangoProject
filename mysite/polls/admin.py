from django.contrib import admin
from .models import Question
from .models import Choice
from .models  import Review

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Review)


