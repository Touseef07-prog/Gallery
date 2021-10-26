from django.urls import path
from .views import home, picture_upload, category_images


urlpatterns = [
    path("", home, name="home"),
    path("upload/", picture_upload, name="upload"),
    path("category_images/<str:name>", category_images, name="category_images"),
]
