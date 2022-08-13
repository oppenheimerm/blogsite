# URL patterns allow you to map URLs to views.  Django runs
# through each URL pattern and stops at the first one that
# matched the requested URL.

from django.urls import path
from . import views

# application namespace, that allows us to organize URLs by
# application and use the name when referring to them.
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # Not using the class based view
    #path('', views.PostListView.as_view(), name='post_list'),
    
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
            views.post_detail,
            name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]