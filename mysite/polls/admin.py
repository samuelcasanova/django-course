from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['question_text', 'pub_date'] This just defines the list of fields and their order
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Date', {'fields': ['pub_date']}),
    ]


admin.site.register(Question)
admin.site.register(Choice)
