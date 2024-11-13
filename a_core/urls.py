"""
URL configuration for a_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.urls import path, include, re_path
from a_posts.views import *
from a_users.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secure-admin/', admin.site.urls),
    path('theboss/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_view, name='home'),
    path('category/<tag>/', home_view, name='category'),
    path('post/create/', post_create_view, name='post-create'),
    path('post/delete/<pk>/', post_delete_view, name='post-delete'),
    path('post/edit/<pk>/', post_edit_view, name='post-edit'),
    path('post/<pk>/', post_read_view, name='post'),
    path('post/like/<pk>/', like_post, name='like-post'),
    path('comment/like/<pk>/', like_comment, name='like-comment'),
    path('reply/like/<pk>/', like_reply, name='like-reply'),
    path('profile/', profile_view, name='profile'),
    path('<username>/', profile_view, name='userprofile'),
    path('profile/edit/', profile_edit_view, name='profile-edit'),
    path('profile/delet/', profile_delete_view, name='profile-delete'),
    path('profile/onboaring/', profile_edit_view, name='profile-onboarding'),
    path('commentsent/<pk>/', comment_sent, name='comment-sent'),
    path('comment/delete/<pk>/', comment_delete_view, name='comment-delete'),
    path('reply-sent/<pk>/', reply_sent, name='reply-sent'),
    path('reply/delete/<pk>/', reply_delete_view, name='reply-delete'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)