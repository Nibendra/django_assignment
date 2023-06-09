from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.post_list),
    path('posts/<int:post_id>', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])