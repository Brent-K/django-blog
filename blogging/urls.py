
from django.urls import path
from blogging.views import stub_view, PubPostListView, PostDetailView

urlpatterns = [
        path('', PubPostListView.as_view(), name="blog_index"),
        path('posts/<int:pk>/', PostDetailView.as_view(), name="blog_detail"),
        ]
