from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Question

def index(request):
    myname = "Huu Khanh"
    taisan = ["dien thoai", "may tinh", "may bay", "nhieu tien"]
    context = {"name": myname, "taisan": taisan}
    return render(request, "polls/index.html",context )

def viewlist(request):
    list_question = Question.objects.all()
    context  = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})