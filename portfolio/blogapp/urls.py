from django.urls import path
from . import views
app_name = 'blogapp'
urlpatterns = [
    path('create_blog',views.create_blog,name='create_blog'),
    path('edit_blog/<pk>/', views.Edit_Blog.as_view(), name='edit_blog'),
    path('myblogs', views.MyBlog.as_view(), name='myblogs'),
    path('',views.BlogHome.as_view(),name='bloghome'),
    path('blogdetails/<pk>/',views.BlogDetails.as_view(),name='blogdetails'),
    path('searched_blogs', views.searched_blogs, name='searched_blogs'),
    # path('blogcomment/<pk>/',views.Comment_View.as_view(),name='blogcomment'),
]
