"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# Including app/urls.py
from django.urls import path, include

# Login and logout
from django.contrib.auth import views as auth_views

# Users (Signup)
from users import views as users_views

# Media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin url path
    path('admin/', admin.site.urls),

    # Signup, login and logout url paths
    path('signup/', users_views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),

    # Reset password url paths
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='users/resetpassword.html'),
         name='reset_password'),
    path('reset-password/requested/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/resetpassword_requested.html'),
         name='password_reset_done'),
    path('reset-password-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/resetpassword_confirm.html'),
         name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/resetpassword_complete.html'),
         name='password_reset_complete'),

    # Including app.urls url paths
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
