from django.urls import path
from blogging.views import stub_view, PubPostListView, PostDetailView, add_model

urlpatterns = [
    path("", PubPostListView.as_view(), name="blog_index"),
    path("add/", add_model, name="add_post"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
]
