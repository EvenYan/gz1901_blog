from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from blog.models import Post


def index(request):
    post_list = Post.objects.all()
    print(post_list)
    context = {"post_list": post_list}
    return render(request, "index.html", context)


def post(request, id):
    post = Post.objects.get(id=id)
    print(post)
    context = {"post": post}
    return render(request, 'detail.html', context)


def new_post(request):
    return render(request, "new_post.html")


def save_post(request):
    title = request.POST.get("title")
    body = request.POST.get("body")
    Post.objects.create(title=title, body=body)
    return HttpResponse("文章保存成功！")