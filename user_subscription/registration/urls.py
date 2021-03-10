from django.urls import path, include
from registration.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView
from registration import views as registration_views


urlpatterns = [
    # Other URL patterns ...
    path('accounts/register/',
        RegistrationView.as_view(form_class= CustomUserForm,success_url='/profile/'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/',registration_views.ProfilePage.as_view(),name='profile'),
    path('accounts/login/profile/',registration_views.ProfilePage.as_view()),
    path('loggedout/',registration_views.logout_view,name = 'logoutpage'),
    path('accounts/login/profile/loggedout/',registration_views.logout_view),
    path('profile/loggedout/',registration_views.logout_view),
    path("create-sub", registration_views.create_sub, name="create sub"),
    path("complete", registration_views.complete, name="complete"),
    # path('complete/', registration_views.SuccessView.as_view()),
    # More URL patterns ...
]