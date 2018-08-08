from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, null=True, db_index=True)
    slug = models.SlugField(max_length=100, null=True, db_index=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%s' % self.titleclear

    def get_absolute_url(self):
        return reverse('view_blog_category', args=[self.slug])


class Post(models.Model):
    title = models.CharField(max_length=255, default='0000000')
    body = models.TextField(default='0000000')
    slug = models.SlugField(max_length=100, default='0000000', db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('view_blog_post', args=[self.slug])


