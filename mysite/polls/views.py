from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.html import escape
from django.views import View
from polls.models import Question


def index(request):
    latest_question_list = Question.objects \
                           .order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def api(request, id):
    return HttpResponse(f"<html><body><h1>API Endpoint</h1>"
                        f"<p>You requested the API with id={escape(id)}.</p>"
                        "</body></html>")


class ClassBasedView(View):
    def get(self, request):
        return HttpResponse("<html><body><h1>Class Based View</h1>"
                            "<p>This is from a class-based view.</p>"
                            f"<p>You requested with url={request.path}.</p>"
                            "</body></html>")


def bounce(request):
    return HttpResponseRedirect("/polls/?param=redirected")


class TemplatedView(View):
    def get(self, request, param):
        info = {'param': param}
        return render(request, 'templated.html', info)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # alternative, get_object_or_404:
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
