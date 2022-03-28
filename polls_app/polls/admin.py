from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ['published_date', 'txt_question']
    
    # To show only one or certain fields
    # fields = ['txt_question']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
