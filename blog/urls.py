from django.urls import path
from blog.views import(
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
)

urlpatterns = [

    path('',blog_post_list_view),
    path('<str:post_slug>/',blog_post_detail_view),
    path('<str:post_slug>/edit/',blog_post_update_view),
    path('<str:post_slug>/delete/',blog_post_delete_view),
]