from django.urls import path
from . import  views
urlpatterns =[
    path('',views.index, name = 'index'),
    path('question_list/', views.viewlist, name = 'viewlist'),
    path('detail_question/<int:question_id>/', views.detaiView, name='detailView')
]