from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    Blog_Categories = (
        ("Science", "Science"),
        ("Technology", "Technology"),
        ("Health", "Health"),
        ("Fitness", "Fitness"),
        ("Buissness", "Buissness"),
        ("Education", "Education"),
        ("News", "News"),
        ("Entertainment", "Entertainment"),
        ("Gaming","Gaming"),
        ("Lifestyle_and_hobbies", "Lifestyle_and_hobbies"),
        ("Other", "Other"),
    )

    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_blog')
    title = models.CharField(max_length=100)
    blog_pic = models.ImageField(upload_to='blog_pic')
    content = models.TextField()
    category = models.CharField(max_length=500,choices=Blog_Categories,default='Other')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (f'{self.author} wrote {self.title}, in {self.category}') 


class Comment(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    comment = models.TextField()

    def __str__(self):
        return (f'{self.user.username} commented on {self.blog.title} by {self.blog.author}')

class Contact(models.Model):
    name  = models.CharField(max_length=50,verbose_name='Name ')
    email = models.EmailField(verbose_name='Email ')
    message = models.TextField(verbose_name='Feedback ')

    def __str__(self):
        return (f'{self.name} sent a message through the email {self.email}')
