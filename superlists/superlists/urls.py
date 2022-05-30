from lists import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$',views.home_page,name='home'),
    re_path(r'^lists/the-only-list-in-the-world/$',views.view_list,name='view_list')
]
