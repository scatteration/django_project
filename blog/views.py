from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


# Create your views here.
def post_list(request):
    gonderi = "Burada gonderiler listelenecek"
    return HttpResponse(gonderi)


def post_update(request):
    guncel = ' Burada gonderi guncellencek'
    return HttpResponse(guncel)


def post_delete(request):
    delete = "Burada gonderi silinecek"
    return HttpResponse(delete)


def post_create(request):
    create = '<b>Burada gonderi olusturulacaktir</b>'
    return HttpResponse(create)

