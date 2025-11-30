# Heavily inspired in https://medium.com/@muhashharoon/running-standalone-python-script-having-a-dependency-on-django-apps-like-models-views-etc-6f38b737d97f
import os
import sys
from django.utils import timezone

project_path = "/home/samuel/git/personal/django-course/mysite"
sys.path.append(project_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

django.setup()
from polls.models import Question

question = Question(question_text="What's your satisfaction level?", pub_date=timezone.now())
question.save()
print(f"Created Question id: {question.id}")

print("Different ways to query the Question model:")
print(Question.objects.get(id=1))
print(Question.objects.filter(question_text__startswith="What"))
print(Question.objects.filter(pub_date__year=timezone.now().year))

print("Calling a custom method on the Question instance:")
print(question.was_published_recently())

print("Creating a choice set for the question:")
choice1 = question.choice_set.create(choice_text="Very Satisfied", votes=0)
choice2 = question.choice_set.create(choice_text="Satisfied", votes=0)
choice3 = question.choice_set.create(choice_text="Not Satisfied", votes=0)

print("Accessing the parent question from a choice:")
print(choice1.question)

print("All Choice objects related to the question:")
print(question.choice_set.all())
print(f"Question has a total of {question.choice_set.count()} choices.")

print("All Question objects in the database:")
print(Question.objects.all())
