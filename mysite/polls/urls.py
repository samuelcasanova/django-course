from django.urls import path

from . import views

# namespace for the polls app, this allows us to refer to
# urls unambiguously, i.e. 'polls:index' in templates
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api/<int:id>", views.api, name="api"),
    path("class", views.ClassBasedView.as_view(), name="class"),
    path("bounce", views.bounce, name="bounce"),
    path("templated/<str:param>", views.TemplatedView.as_view(),
         name="templated"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
