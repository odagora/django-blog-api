from .views import *
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r"authors", AuthorViewSet, "authors")
router.register(r"categories", CategoryViewSet, "categories")
router.register(r"posts", PostViewSet, "posts")
router.register(r"comments", CommentViewSet, "comments")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs", include_docs_urls(title="Blog API")),
]
