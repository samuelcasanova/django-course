from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/<int:id>", views.api, name="api"),
    path("class", views.ClassBasedView.as_view(), name="class"),
    path("bounce", views.bounce, name="bounce"),
    path("templated/<str:param>", views.TemplatedView.as_view(),
         name="templated"),
]
