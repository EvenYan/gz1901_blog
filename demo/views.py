from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"str": "<script>alert('Hi')</script>"}
    return render(request, "demo/home.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        print(username)
        print(passwd)
        response = HttpResponse("登录成功")
        response.set_cookie("name", username, max_age=60)
        return response
    return render(request, "demo/login.html")


def home(request):
    username= request.COOKIES.get("name")
    context = {"username": username}
    return render(request, 'homepage.html', context)