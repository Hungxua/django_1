from django.shortcuts import render
from django.http import  HttpResponse
from .models import Question, Choice
# Create your views here.
def index(request):
    myname = 'XuanHung'
    taisan = ['dien thoai', 'may tinh', 'may bay']
    context = {'name': myname, 'taisan': taisan}
    return render(request, "polls/index.html", context)

def viewlist(request):
    list_question = Question.objects.all()
    context = {'list_question': list_question}
    print(list_question)
    return render(request, 'polls/question_list.html', context)

def detaiView(request, question_id):
    q = Question.objects.get(pk = question_id)
    context = {'qs': q}
    return render(request, 'polls/detail_question.html', context)