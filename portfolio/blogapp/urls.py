from django.urls import path
from . import views
app_name = 'blogapp'
urlpatterns = [
    path('create_blog',views.create_blog,name='create_blog'),
    path('edit_blog/<pk>/', views.Edit_Blog.as_view(), name='edit_blog'),
    path('delete_blog/<pk>/', views.Delete_Blog.as_view(), name='delete_blog'),
    path('myblogs', views.MyBlog.as_view(), name='myblogs'),
    path('',views.BlogHome,name='bloghome'),
    path('blogdetails/<pk>/',views.BlogDetails,name='blogdetails'),
    path('searched_blogs_by_title',views.searched_blogs_by_title, name='searched_blogs_by_title'),
    path('searched_blogs_by_category', views.searched_blogs_by_category,name='searched_blogs_by_category'),
    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
]
