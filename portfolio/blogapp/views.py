from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .forms import Create_Blog_Form, Comment_Form,Edit_Blog_Form
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView,UpdateView,TemplateView
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


class BlogHome(ListView):
    model = Blog
    template_name = 'blogapp/home.html'


class BlogDetails(DetailView):
    model = Blog
    template_name = 'blogapp/blog_details.html'


def searched_blogs(request):
    search = request.GET['search']
    searched_blogs = Blog.objects.filter(title__icontains=search)
    dict = {'searched_blogs':searched_blogs}
    return render(request,'blogapp/search.html',dict)

    
class Edit_Blog(UpdateView):
    model = Blog
    fields = ('title','blog_pic','content')
    template_name = 'blogapp/edit_blog.html'

    def get_success_url(self):
        return reverse_lazy('blogapp:myblogs')


class MyBlog(LoginRequiredMixin,TemplateView):
    template_name = 'blogapp/myblogs.html'
# def Edit_Blog(request):
#     form = Edit_Blog_Form
#     if request.method =='POST':
#         form = Edit_Blog_Form(request.POST)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user
#             blog.save()
#             messages.success(request,'Your Blog is Updated!')
#     dict = {'form':form}
#     return render(request,'blogapp/edit_blog.html',dict)    

# def My_Blogs(request):
#     return render(request,'blogapp/myblogs.html')         
    # def add_comment(request, pk):
    #     form = Comment_Form(request.POST or None)
    #     if request.method == 'POST':
    #         if form.is_valid():
    #             commentboi = form.save(commit=False)
    #             commentboi.blog = Blog.objects.get(pk=pk)
    #             commentboi.user = request.user
    #             commentboi.save()
    #             return HttpResponse(request, 'good')
    #     return render(request, 'blogapp/blog_details.html', {'form': form})

# def Comment_View(request):
#     form = Comment_Form
#     if request.method =='POST':
#         form = Comment_Form(request.POST)
#         if form.is_valid():
# class Comment_View(CreateView):
#     model = Comment
#     form_class = Comment_Form
#     template_name = 'blogapp/comments.html'

#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super(Comment_View, self).form_valid(form)

#     def get_success_url(self):
#         blog = Blog.objects.get(pk=self.kwargs.get('pk'))
#         return HttpResponseRedirect(reverse('blogapp:bloghome'))


# def add_comment(request):
#     form = Comment_Form
#     if request.method =='POST':
#         form = Comment_Form(request.POST)
#         def form_valid(self,form):
#             form.instance.blog_id = self.kwargs['pk']
#             return super().form_valid(form)
#         return HttpResponseRedirect(reverse('blogapp:blogdetails'))
#     return rend
