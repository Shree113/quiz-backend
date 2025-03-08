from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option')

admin.site.register(Question, QuestionAdmin)
