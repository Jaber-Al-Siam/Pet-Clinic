from typing import List, Any
from django.urls import path, include
from UserApp import views as userapp_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns: List[Any] = [
    path('signup/', userapp_views.signup_request, name="signup_page"),
    path('', include('django.contrib.auth.urls')),
    path('profile/', userapp_views.profile_request, name="profile_page"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout_page'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset_page'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done_page'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm_page'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
