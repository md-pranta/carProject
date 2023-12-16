from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',SignUp.as_view(),name="signup"),
    path('login/',LogIn.as_view(),name="login"),
    path('profile/',profile,name="profile"),
    path('profile/edit/',edit,name="edit"),
    path('logout/',LogOut.as_view(),name="logout"),
    # path('detail/<int:id>',Details.as_view(),name="detail"),
    path('detail/<int:id>',details,name="detail"),
]
