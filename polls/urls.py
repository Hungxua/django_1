from django.urls import path
from . import  views

app_name = 'polls'
urlpatterns =[
    path('',views.index, name = 'index'),
    path('question_list/', views.viewlist, name = 'viewlist'),
    path('detail_question/<int:question_id>/', views.detaiView, name='detailView'),
    path('<int:question_id>',views.vote, name='vote')
]