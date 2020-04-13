from django.urls import path, include
from UserApp import views as UserApp_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', UserApp_views.signup, name="SignUP"),
    path('', include('django.contrib.auth.urls')),
    path('profile/', UserApp_views.profile, name="Profile"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
