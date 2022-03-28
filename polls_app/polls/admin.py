from django.contrib import admin

from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    # You can use admin.StackInline to stack
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # To change the order of columns
    # fields = ['published_date', 'txt_question']

    # To show only one or certain fields
    # fields = ['txt_question']

    fieldsets = [
        ('Question', {'fields': ['txt_question']}),
        ('Date Information', {'fields': ['published_date']})
    ]
    inlines = [ChoiceInLine]

    list_display = ('txt_question', 'published_date', 'recently_published')
    list_filter = ['published_date']
    search_fields = ['txt_question']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
