from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_student(self):
        self.save()


class Notes(models.Model):
    course = models.CharField(max_length=60)
    notes = models.TextField()
    student = models.ForeignKey(User,on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now_add=True)
    notes_image = models.ImageField(upload_to='notes/')

    @classmethod
    def todays_notes(cls):
        today = dt.date.today()
        courses = cls.objects.filter(pub_date__date=today)
        return courses

    @classmethod
    def search_by_title(cls, search_term):
        courses  = cls.objects.filter(title__icontains=search_term)
        return courses
