from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import (MyChangePasswordForm)

urlpatterns = [
    path('admincreateuser/', views.adminCreateUser, name="admincreateuser"),
    path('userprofile/<int:id>/', views.userProfile, name="userprofile"),
    path('authadmin/allusers/', views.allUsers, name='allusers'),
    path('authadmin/deleteuser/<int:id>/', views.delete_user, name="deleteuser"),

    path("auth/signup/", views.user_signup, name="signup"),
    path('auth/login/', views.user_login, name="login"),
    path('auth/logout/', views.user_logout, name="logout"),

        # ---------------------------- CHANGE PASSWORD -----------------------
    # for changing user password used built-in 'PasswordChangeView' also giving custom created template, form and after password is changed then it redirects to "/passwordchangedone/"
    path(
        "pass/changepass/",
        auth_views.PasswordChangeView.as_view(
            template_name="changepassword.html",
            form_class=MyChangePasswordForm,
            success_url="/auth/pass/passwordchangedone/",
        ),
        name="changepass",
    ),

    # after password is changed then it redirects here. for showing that password change is done used built-in 'PasswordChangeDoneView'. Here shows only a template . 
    path(
        "pass/passwordchangedone/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="passwordchangedone.html"
        ),
        name="passwordchangedone",
    ),
    # ---------------------------- END CHANGE PASSWORD -----------------------

   
]