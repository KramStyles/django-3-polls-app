from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Hello and Welcome to the Polls app</h2>")
