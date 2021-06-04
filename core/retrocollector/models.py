from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=25, default="Computer")

    def __str__(self):
        return f"{self.name}"


class Collectible(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date_manufactured = models.DateField()
    date_added = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}-{self.type}"
