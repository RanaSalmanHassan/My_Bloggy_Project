from django.urls import path
from . import views
app_name ='loginapp'
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'),
]