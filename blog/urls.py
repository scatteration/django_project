from django.urls import path
from .views import post_create, post_delete, post_list, post_update

urlpatterns = [
    path('post-create/', post_create),
    path('post-list/', post_list),
    path('post-update/', post_update),
    path('post-delete/', post_delete)
]
