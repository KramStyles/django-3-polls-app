from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='home'),
    # path('<int:ques_id>', views.details, name='detail'),
    # path('<int:ques_id>/results', views.results, name='result'),
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='result'),
    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),
    path('<int:ques_id>/vote/', views.vote, name='vote')
]