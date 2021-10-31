from django.urls import path
from .views import home, picture_upload, category_images,picture_detail


urlpatterns = [
    path("", home, name="home"),
    path("picture_detail/<int:id>", picture_detail, name="picture_detail"),
    path("upload/", picture_upload, name="upload"),
    path("category_images/<str:name>", category_images, name="category_images"),
]
