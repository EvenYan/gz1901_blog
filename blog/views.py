from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def post(request):
    return HttpResponse("文章1")