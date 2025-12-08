from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from polls.models import Question, Choice
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))