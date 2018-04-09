from django.urls import path, include

from . import views

app_name = 'frac'
urlpatterns = [
    # example /polls/
    path('', views.home, name='home'),
    path('new-project/', views.new_project, name='new-project'),
    path('project/<int:pk>/injections/', views.injections, name='injections')
]
