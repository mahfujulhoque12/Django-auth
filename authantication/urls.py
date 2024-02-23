
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('loginUser/', views.userLogin, name='loginUser'),
    path('logout/', views.userLogout, name='logout'),
    path('signup/', views.registration, name='signup'),
    path('passcng/', views.change_password, name='passcng'),

    path('reset/password/', PasswordResetView.as_view(template_name='reset_pass.html'), name='password_reset'),

    path('reset/password/done/', PasswordResetDoneView.as_view(template_name='reset_pass_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reset_pass_confirm.html'), name='password_reset_confirm'),

      path('reset/done/', PasswordResetCompleteView.as_view(template_name='pass_reset_complate.html'), name='password_reset_complete'), 



]


# from django.urls import path
# from . import views
# from django.contrib.auth.views import PasswordResetDoneView, PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('home/', views.home, name='home'),
#     path('loginUser/', views.userLogin, name='loginUser'),
#     path('logout/', views.userLogout, name='logout'),
#     path('signup/', views.registration, name='signup'),
#     path('passcng/', views.change_password, name='passcng'),

#     path('reset/password/', PasswordResetView.as_view(template_name='reset_pass.html'), name='password_reset'),

#     path('reset/password/done/', PasswordResetDoneView.as_view(template_name='reset_pass_done.html'), name='password_reset_done'),

#     path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reset_pass_confirm.html'), name='password_reset_confirm'),

#     path('reset/done/', PasswordResetCompleteView.as_view(template_name='pass_reset_complate.html'), name='password_reset_complete'), 

# ]
