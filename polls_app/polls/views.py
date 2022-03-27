from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Hello and Welcome to the Polls app</h2>")


def details(request, ques_id):
    response = "<h2>You are looking at Question: %s</h2>" % ques_id
    return HttpResponse(response)


def results(request, ques_id):
    response = "<h2>You are looking at results of Question: %s</h2>"
    return HttpResponse(response % ques_id)


def vote(request, ques_id):
    response = "<h3>You are voting on question: %s</h3>" % ques_id
    return HttpResponse(response)
