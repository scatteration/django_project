from django.shortcuts import render, HttpResponse
from .models import Blog
from .forms import IletisimForm


def post_list(request):
    posts = Blog.objects.all()
    icerik = {"posts": posts}
    return render(request, "blog/post-list.html", context=icerik)


def post_update(request):
    guncel = ' Burada gonderi guncellencek'
    return HttpResponse(guncel)


def post_delete(request):
    delete = "Burada gonderi silinecek"
    return HttpResponse(delete)


def post_create(request):
    create = '<b>Burada gonderi olusturulacaktir</b>'
    return HttpResponse(create)


def iletisim(request):
    form = IletisimForm()
    return render(request, "blog/iletisim.html", context={"form": form})
