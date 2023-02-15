from django.urls import path
from account.views import *


app_name = "account"

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),

]
