from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.html import escape
from django.views import View


def index(request):
    return HttpResponse("<html><body><h1>Hello, world</h1>"
                        "<p>Welcome to the polls index page.</p>"
                        "<p>You requested with"
                        f" param={escape(request.GET['param'])}"
                        " query parameter.</p>"
                        "</body></html>")


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
