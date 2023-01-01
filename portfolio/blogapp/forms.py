from django import forms
from .models import Blog, Comment


class Create_Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('author',)


class Edit_Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'blog_pic', 'content',)


class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
