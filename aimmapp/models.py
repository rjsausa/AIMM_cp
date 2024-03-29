from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100, default='Napa,CA')

    def __str__(self):
        return self.name
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Project, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    date = models.DateField()
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} for {self.project}"

class Income(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)