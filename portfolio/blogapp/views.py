from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .forms import Create_Blog_Form, Comment_Form, Edit_Blog_Form, Contact_Form
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from .models import Blog, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def create_blog(request):
    form = Create_Blog_Form
    if request.method == 'POST':
        form = Create_Blog_Form(request.POST, request.FILES)
        if form.is_valid():
            blogboi = form.save(commit=False)
            blogboi.author = request.user
            blogboi.save()
            # form.save()
            messages.success(request, 'Blog Created Successfully')
            # return HttpResponse('Blog Created')
            return HttpResponseRedirect(reverse('blogapp:bloghome'))

    dict = {'form': form}
    return render(request, 'blogapp/create_blog.html', dict)


def BlogHome(request):
    buissness_blogs = Blog.objects.filter(category='Buissness')
    technology_blogs = Blog.objects.filter(category='Technology')
    health_blogs = Blog.objects.filter(category='Health')
    fitness_blogs = Blog.objects.filter(category='Fitness')
    science_blogs = Blog.objects.filter(category='Science')
    education_blogs = Blog.objects.filter(category= 'Education')
    news_blogs = Blog.objects.filter(category='News')
    entertainment_blogs = Blog.objects.filter(category='Entertainment')
    gaming_blogs = Blog.objects.filter(category='Gaming')
    lifestyle_and_hobbies_blogs = Blog.objects.filter(
        category='Lifestyle and hobbies')
    other_blogs = Blog.objects.filter(category='Other')
    dict = {'buissness_blogs': buissness_blogs,
            'technology_blogs': technology_blogs,
            'health_blogs': health_blogs,
            'fitness_blogs': fitness_blogs,
            'science_blogs': science_blogs,
            'education_blogs': education_blogs,
            'news_blogs': news_blogs,
            'entertainment_blogs': entertainment_blogs,
            'gaming_blogs': gaming_blogs,
            'lifestyle_and_hobbies_blogs': lifestyle_and_hobbies_blogs,
            'other_blogs': other_blogs,
            }
    return render(request, 'blogapp/home.html', dict)


# class BlogDetails(DetailView):
#     model = Blog
#     template_name = 'blogapp/blog_details.html'

def BlogDetails(request, pk):
    blog_model = Blog.objects.get(pk=pk)
    comment_model = Comment.objects.filter(blog = blog_model)
    form = Comment_Form()
    if request.method == 'POST':
        form = Comment_Form(request.POST)
        if form.is_valid():
            comment_boi = form.save(commit=False)
            comment_boi.user = request.user
            comment_boi.blog = blog_model
            comment_boi.save()
            messages.success(
                request, 'Congratulation! Your Comment Has Been Added!!')
            return HttpResponseRedirect(reverse('blogapp:blogdetails', kwargs={'pk': pk}))

    dict = {'blog_model': blog_model, 'form': form,
        'comment_model': comment_model}
    return render(request, 'blogapp/blog_details.html', dict)


def searched_blogs_by_title(request):
    search = request.GET['search']
    searched_blogs = Blog.objects.filter(title__icontains=search)
    dict = {'searched_blogs': searched_blogs}
    return render(request, 'blogapp/search_by_title.html', dict)


def searched_blogs_by_category(request):
    search = request.GET['search']
    searched_blogs = Blog.objects.filter(category__icontains=search)
    dict = {'searched_blogs': searched_blogs}
    return render(request, 'blogapp/searched_by_category.html', dict)


class Edit_Blog(UpdateView):
    model = Blog
    fields = ('title', 'blog_pic', 'content')
    template_name = 'blogapp/edit_blog.html'

    def get_success_url(self):
        return reverse_lazy('blogapp:myblogs')


class Delete_Blog(DeleteView):
    model = Blog
    template_name = "blogapp/blog_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('blogapp:myblogs')



class MyBlog(LoginRequiredMixin,TemplateView):
    template_name = 'blogapp/myblogs.html'



def about_us(request):
    return render(request,'blogapp/about_us.html')

def contact(request):
    form = Contact_Form
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thanks for your feeedback!')
            return HttpResponseRedirect(reverse('blogapp:bloghome'))
    dict = {'form':form}
    return render(request,'blogapp/contact.html',dict)