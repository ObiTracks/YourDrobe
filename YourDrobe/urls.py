"""YourDrobe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingPage, name='landingpage'),
    path('home', home, name='home'),
    path('profile/<str:pk>/', profile, name='profile'),
    path('discover/', discover, name='discover'),
    path('discover/search/', search, name='search'),
    path('stylepost/', post, name='post'),
    path('createpost/', createPost, name='create'),
    path('deletepost/<str:pk>', deletePost, name='delete'),
    
    path('signup/', registerUserPage, name='signup'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)