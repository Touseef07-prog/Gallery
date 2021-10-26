from django.db import models
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Picture(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=60, null=True)
    image = models.ImageField(
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
        blank=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
