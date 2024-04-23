from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import include

router = DefaultRouter()
router.register(r"authors", AuthorViewSet, "authors")
router.register(r"categories", CategoryViewSet, "categories")
router.register(r"posts", PostViewSet, "posts")
router.register(r"comments", CommentViewSet, "comments")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
