from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartPageView.as_view(), name="start-page"),
    path("blogs", views.AllPostsView.as_view(), name="blogs-page"),
    path("blogs/read_later", views.ReadLaterView.as_view(), name="read-later-page"),
    path("blogs/<slug:slug>", views.PostDetailsView.as_view(), name="blog-details-page")
]
