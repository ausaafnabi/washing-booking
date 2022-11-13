
from django.contrib.auth import views as dViews
from django.urls import path

urlpatterns = [
    path('logout/', dViews.LogoutView.as_view(), name='logout'),
    path('password-reset/', dViews.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', dViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', dViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', dViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', dViews.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', dViews.PasswordChangeDoneView.as_view(), name='password_change_done'),
]