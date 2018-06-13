from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('pub_date', 'question_text', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['choice']

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)
