from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader, RequestContext

from polls.models import Question


def index(request):
    # 根据发布时间降序查询,并过滤前5条记录
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list
    })
    return HttpResponse(template.render(context))


def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)


def result(request, question_id):
    return HttpResponse("You are looking at the result of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You voting on question %s" % question_id)
