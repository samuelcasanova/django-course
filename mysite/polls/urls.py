from django.urls import path

from . import views

# namespace for the polls app, this allows us to refer to
# urls unambiguously, i.e. 'polls:index' in templates
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("api/<int:id>", views.api, name="api"),
    path("class", views.ClassBasedView.as_view(), name="class"),
    path("bounce", views.bounce, name="bounce"),
    path("templated/<str:param>", views.TemplatedView.as_view(),
         name="templated"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
