from django.shortcuts import render, HttpResponse

# Create your views here.

# Create your views here.
def post_list(request):
    gonderi = "Burada gonderiler listelenecek"
    return render(request, "blog/post-list.html")


def post_update(request):
    guncel = ' Burada gonderi guncellencek'
    return HttpResponse(guncel)


def post_delete(request):
    delete = "Burada gonderi silinecek"
    return HttpResponse(delete)


def post_create(request):
    create = '<b>Burada gonderi olusturulacaktir</b>'
    return HttpResponse(create)

