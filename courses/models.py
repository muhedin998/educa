from curses.ascii import US
from enum import unique
from turtle import title
from unittest.util import _MAX_LENGTH
from xml.etree.ElementTree import TreeBuilder
from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='course_created')

    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE,
                                related_name='courses')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-created']
    
    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course,
                                related_name='modules',
                                on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
