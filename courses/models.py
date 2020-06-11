from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()

    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'courses/')

 
  def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def save_course(self):
        self.save()

    def delete_course(self):
        self.delete()




class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bio = models.TextField(default="")
    contact_info = models.CharField(max_length=200,blank=True)
    profile_Id = models.IntegerField(default=0)
    all_projects = models.ForeignKey('courses',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()
