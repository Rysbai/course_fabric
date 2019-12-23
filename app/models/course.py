from django.db import models

NAME_MAX_LENGTH = 200


class CategoryORM(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)


class CourseORM(models.Model):
    category = models.ForeignKey(CategoryORM, on_delete=models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    price = models.PositiveIntegerField()
