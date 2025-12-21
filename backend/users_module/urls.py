from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import *

from .REST.views.users_views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    # API:
    path('register/', RegisterView.as_view(), name="register"),
    path('register_done/', RegisterDoneView.as_view(), name="register_email_link"),

    path('reset/', ResetView.as_view(), name="reset"),
    path('reset_ok/', ResetOKView.as_view(), name="reset_email_link"),
    path('reset_done/', ResetDoneView.as_view(), name="enter_new_password"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),

    path('user/', BasicUserView.as_view()),
    path('edit/', EditUserView.as_view()), #edits everything
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('promote/<uuid:id>/', PromoteView.as_view()),


]
