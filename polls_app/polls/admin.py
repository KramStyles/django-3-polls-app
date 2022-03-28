from django.contrib import admin

from .models import Question, Choice


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['published_date', 'txt_question']

    # To show only one or certain fields
    # fields = ['txt_question']

    fieldsets = [
        ('Question', {'fields': ['txt_question']}),
        ('Date Information', {'fields': ['published_date']})
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
