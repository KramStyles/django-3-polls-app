from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:ques_id>', views.details, name='detail'),
    path('<int:ques_id>/results', views.results, name='result'),
    path('<int:ques_id>/vote', views.vote, name='votes')
]