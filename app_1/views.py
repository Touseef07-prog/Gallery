from django.http import response
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.views.generic import View
from .models import Category, Picture


def home(request):
    get_categories = Category.objects.all().order_by("-timestamp")
    get_pictures = Picture.objects.all().order_by("-timestamp")
    return render( request, "app_1/home.html",{"pictures": get_pictures, "categories": get_categories})

def picture_detail(request,id):
    get_detail=Picture.objects.get(id=id)
    return render(request,
    "app_1/picture_detail.html",
    {"get_detail":get_detail})


    
    


def picture_upload(request):
    get_categories = Category.objects.all().order_by("-timestamp")
    if request.method == "POST":
        get_category = Category.objects.get(name=request.POST["category"])
        Picture.objects.create(
            title=request.POST["title"],
            category=get_category,
            image=request.FILES["image"],
            description=request.POST["description"],
        )
        return redirect("app_1:home")
    return render(request, "app_1/picture_upload.html", {"categories": get_categories})


def category_images(request, name):
    get_categories = Category.objects.all().order_by("-timestamp")
    get_category = Category.objects.get(name=name)
    get_pictures = Picture.objects.filter(category=get_category).order_by("-timestamp")
    return render(
        request,
        "app_1/home.html",
        {"pictures": get_pictures, "categories": get_categories},
    )
