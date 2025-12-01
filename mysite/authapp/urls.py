from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'authapp'
urlpatterns = [
    path('', TemplateView.as_view(template_name='authapp/main.html')),
    path('open', views.OpenView.as_view(), name='open'),
    path('manual', views.ManualProtect.as_view(), name='manual'),
    path('protect', views.ProtectView.as_view(), name='protect'),
    path('python', views.DumpPython.as_view(), name='python'),
]
