from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_blog')
    title = models.CharField(max_length=100)
    blog_pic = models.ImageField(upload_to='blog_pic')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{}'.format(self.author)) 


class Comment(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_comment')
    blog = models.OneToOneField(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    comment = models.TextField()

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username