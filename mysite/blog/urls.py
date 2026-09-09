from django.urls import path
from .views import post_list, post_detail

app_name = 'blog'

urlpatterns = [
    # представление поста
    path('', post_list, name='post_list'),
    # path('<int:id>/', post_detail, name='post_detail')
    path('<int:year>/<int:month>/<int:day>/<slug:post>', post_detail, name='post_detail')
]