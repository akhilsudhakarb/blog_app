from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Blogs(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    image = models.ImageField(upload_to='blog-image', default='blog-image/blog.png')
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    # likes = models.ManyToManyField(User, related_name='blog_post')

    class Meta:
        verbose_name_plural = 'Blogs'



    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):

        return reverse('home')



