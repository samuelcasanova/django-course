import csv
import datetime
from zoneinfo import ZoneInfo

from polls.models import Question, Choice


def run():
    file_handler = open('scripts/questions.csv')
    reader = csv.reader(file_handler)
    next(reader)  # Advance past the header

    Question.objects.all().delete()
    Choice.objects.all().delete()

    for row in reader:
        print(row)

        pub_date = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S') \
                                    .astimezone(ZoneInfo('UTC'))
        question = Question.objects.get_or_create(question_text=row[0],
                                                  pub_date=pub_date)[0]

        choice = Choice(question=question, choice_text=row[2], votes=0)
        choice.save()
